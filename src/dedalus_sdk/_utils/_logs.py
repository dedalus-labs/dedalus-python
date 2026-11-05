from __future__ import annotations

import os
import re
import logging
from typing import Any, cast
from collections.abc import Mapping

REDACTED = "***"

# Credential headers, lower-cased: the conventional ones plus every header this SDK's auth schemes
# write (an `apiKey` scheme names its own, which no fixed list could know).
_REDACTED_HEADERS: frozenset[str] = frozenset(
    ("authorization", "proxy-authorization", "api-key", "x-api-key", "cookie", "set-cookie")
)

# Query parameters this SDK sends a credential in, from its `apiKey` schemes placed in the query.
# A credential there is worse off than one in a header: httpx logs every request URL at `info`.
_REDACTED_QUERY: tuple[str, ...] = ()

# The user part of a URL's authority, where a token often rides (`https://user:token@host`). Stops
# at `/`, `?`, `#` and whitespace, so an `@` in a path or query is left alone.
_USERINFO = re.compile(r"(//)[^/?#@\s]+@")

# How deep `_redact_value` follows nested mappings and sequences before it falls back to masking
# the value's text, so a self-referencing structure cannot recurse without end.
_MAX_DEPTH = 8


def _name_pattern(name: str) -> str:
    """A pattern matching one credential query name in every spelling a URL can carry it in.

    Each character as written or percent-encoded, at any depth and in either hex case (`k`, `%6B`,
    `%6b`, `%256B`), and a space also as `+`. A non-ASCII character is matched as written or as its
    UTF-8 bytes encoded. A lone surrogate has no UTF-8 bytes, so it is matched only as written:
    this runs at import time, and a spec can name a scheme that way. Only the hex ignores case, not
    the name.
    """
    parts: list[str] = []
    for char in name:
        try:
            utf8 = char.encode("utf-8")
        except UnicodeEncodeError:
            utf8 = b""
        encoded = "".join(f"%(?:25)*(?i:{byte:02x})" for byte in utf8)
        alternatives = f"|{encoded}" if encoded else ""
        plus = "|\\+" if char == " " else ""
        parts.append(f"(?:{re.escape(char)}{alternatives}{plus})")
    return "".join(parts)


def _query_pattern() -> re.Pattern[str] | None:
    """The pattern behind `redact()`'s query masking, or `None` when no credential is placed in the query."""
    names = [_name_pattern(name) for name in _REDACTED_QUERY if name]
    if not names:
        return None
    # A name counts after a separator, `?`, `&` or `;`, either literal or percent-encoded any number
    # of times over (`%3F`, `%253F`), since a server can echo a whole URL encoded inside another
    # parameter's value, as a redirect's `return_to` does. `;` also counts as a separator; masking an
    # unrelated `;name=` value as well is harmless. The `=` after it can be encoded the same way. The
    # value then runs to the next literal `&`, `#` or whitespace: an encoded `%26` may end a nested
    # value, but stopping there would leak the rest of a value a sloppy encoder left half-encoded,
    # and masking too much is harmless. `<`, `>` and `"` end it too, since no valid URL carries them
    # unencoded, so a `Link` header's `<url>` keeps its closing delimiter. `'` does not: a query value
    # can hold it raw. A JSON-escaped `\u0026` (hex digits in either case) separates too, since
    # `encoding/json` and others write `&` that way in a URL quoted inside a JSON body. No quantifier
    # nests inside another, so matching stays linear on hostile input.
    return re.compile(
        r"((?:[?&;]|%(?:25)*(?i:3f|26|3b)|\\(?i:u0026))(?:" + "|".join(names) + r")(?:=|%(?:25)*(?i:3d)))[^&#\s<>\"]*"
    )


_QUERY = _query_pattern()

# A header as httpcore's trace logging prints it, `(b'set-cookie', b'session=...')`: the response
# headers of every attempt go out at DEBUG as a list of these byte-string pairs, in whichever quote
# style each bytes repr picks. Matched pair by pair so a value is masked inside its own quotes and the
# trace keeps its `'),` structure. Each quoted part is a run of non-quote, non-backslash characters
# or escapes, so matching stays linear.
_BYTE_PAIR = re.compile(r"""(\(b?['"])([^'"\\]*)(['"],\s*)(b?)(?:'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")(\))""")


def _redact_plain(text: str) -> str:
    """Masks URL userinfo and every credential query value in `text`."""
    text = _USERINFO.sub(r"\1" + REDACTED + "@", text)
    if _QUERY is None:
        return text
    return _QUERY.sub(r"\1" + REDACTED, text)


def _redact_pair(match: re.Match[str]) -> str:
    """One httpcore header pair with its value masked: whole for a credential header, else inside."""
    open_, name, between, prefix, single, double, close = match.groups()
    if name.lower() in _REDACTED_HEADERS:
        return f"{open_}{name}{between}{prefix}'{REDACTED}'{close}"
    if single is not None:
        return f"{open_}{name}{between}{prefix}'{_redact_plain(single)}'{close}"
    return f'{open_}{name}{between}{prefix}"{_redact_plain(double)}"{close}'


def redact(text: str) -> str:
    """Masks URL userinfo, credential header pairs and every credential query value in `text`.

    Works on free text rather than a parsed URL, so it covers a URL quoted in an error message, a
    `Location` or `Link` header, and a credential nested, percent-encoded, in another parameter's
    value (`/login?return_to=%2Fv1%3Fapi_key%3D...`) alike. httpcore's header pairs are masked one
    by one and the text between them on its own, so a masked value cannot run past its pair.
    """
    parts: list[str] = []
    end = 0
    for match in _BYTE_PAIR.finditer(text):
        parts.append(_redact_plain(text[end : match.start()]))
        parts.append(_redact_pair(match))
        end = match.end()
    parts.append(_redact_plain(text[end:]))
    return "".join(parts)


def _is_secret_key(key: object) -> bool:
    """Whether a mapping key names a credential: a redacted header (any case) or query parameter."""
    return isinstance(key, str) and (key.lower() in _REDACTED_HEADERS or key in _REDACTED_QUERY)


def _is_secret_header(name: object) -> bool:
    """Whether `name`, as text or bytes (hpack and httpcore hold headers as bytes), is a credential header."""
    if isinstance(name, (bytes, bytearray)):
        name = bytes(name).decode("latin-1")
    return isinstance(name, str) and name.lower() in _REDACTED_HEADERS


def _masked_like(value: object) -> object:
    """`REDACTED` in the type `value` had, bytes for bytes, so a `b'...'` repr stays one."""
    return REDACTED.encode("ascii") if isinstance(value, (bytes, bytearray)) else REDACTED


def _redact_value(value: object, depth: int = 0) -> object:
    """A log argument with every credential in it masked.

    A mapping (response headers, a request's `headers` or `params`) has the values of credential
    keys replaced whole, and so does a `(name, value)` pair whose name is a credential header, the
    shape hpack logs a header in (`HeaderTuple`, text or bytes). Every string, and every byte string
    read as Latin-1, is passed through `redact()`. Numbers keep their type, so a `%i` or `%f`
    placeholder still formats. Any other object is replaced by its masked text only when that text
    held a credential (an `httpx.URL`, a request's repr), so its own formatting survives otherwise.
    """
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return redact(value)
    if isinstance(value, (bytes, bytearray)):
        text = bytes(value).decode("latin-1")
        masked = redact(text)
        return value if masked == text else masked.encode("latin-1")
    if depth < _MAX_DEPTH:
        if isinstance(value, Mapping):
            return {
                key: REDACTED if _is_secret_key(key) else _redact_value(item, depth + 1)
                for key, item in cast("Mapping[Any, Any]", value).items()
            }
        if isinstance(value, list):
            return [_redact_value(item, depth + 1) for item in cast("list[Any]", value)]
        if isinstance(value, tuple):
            items = cast("tuple[Any, ...]", value)
            if len(items) == 2 and _is_secret_header(items[0]):
                return (items[0], _masked_like(items[1]))
            return tuple(_redact_value(item, depth + 1) for item in items)
    text = str(value)
    masked = redact(text)
    return value if masked == text else masked


# The loggers whose records are masked, each with its children: this package's own, and the HTTP
# libraries under it, which log on loggers of their own: the request URL (httpx, at `info`), every
# response header (httpcore, at `debug`), every header an HTTP/2 connection encodes or decodes
# (hpack, at `debug`), and a websocket handshake's request line and headers (websockets, at `debug`).
_REDACTED_LOGGERS: tuple[str, ...] = ("dedalus_sdk", "httpx", "httpcore", "hpack", "websockets")


def _redacts(name: object) -> bool:
    """Whether a record logged under `name` is one this SDK masks.

    `logging.makeLogRecord` builds its record with no name and fills it in afterwards, so a name
    that is not a string is simply not this SDK's.
    """
    return isinstance(name, str) and any(name == root or name.startswith(root + ".") for root in _REDACTED_LOGGERS)


def _redact_arg(value: object) -> object:
    """`_redact_value`, failing closed: an argument that cannot be masked is logged as `REDACTED`."""
    try:
        return _redact_value(value)
    except Exception:
        return REDACTED


def _redact_text(text: str) -> str:
    """`redact`, failing closed: text that cannot be masked is logged as `REDACTED`."""
    try:
        return redact(text)
    except Exception:
        return REDACTED


# The placeholders a line logging one header as two arguments, its name then its value, joins them
# with: websockets' handshake trace (`> %s: %s`), hpack's `Adding %s=%s to the header table` and
# `Evicting %s: %s from the header table`.
_HEADER_LINE_JOINS: tuple[str, ...] = ("%s: %s", "%s=%s")


def _redact_header_lines(msg: str, args: tuple[object, ...]) -> tuple[object, ...]:
    """Masks the value of a credential header a line logs as a name argument and a value argument.

    The name alone says which value is a secret, so the value is masked whole, in its own type.
    """
    if not any(join in msg for join in _HEADER_LINE_JOINS):
        return args
    masked = list(args)
    for index, arg in enumerate(args[:-1]):
        if _is_secret_header(arg):
            masked[index + 1] = _masked_like(args[index + 1])
    return tuple(masked)


def _is_hpack(name: str) -> bool:
    """Whether a record comes from hpack's own loggers."""
    return name == "hpack" or name.startswith("hpack.")


def _is_byte_string(value: object) -> bool:
    """Whether `value` is raw bytes, the way hpack hands it a header block."""
    return isinstance(value, (bytes, bytearray, memoryview))


def _redact_header_blocks(msg: str, args: tuple[object, ...]) -> tuple[object, ...]:
    """Masks every byte string an hpack record logs other than one header's name and value.

    `Encoded header block to %s` and `Decoding %s` log a whole encoded header block, each header's
    name and value in it as written or Huffman-coded, which is no protection: no pattern can find a
    credential in it, so the block is masked whole. A line that logs one header as a name and a
    value (`_HEADER_LINE_JOINS`) keeps both, its credential values already masked.
    """
    if any(join in msg for join in _HEADER_LINE_JOINS):
        return args
    return tuple(_masked_like(arg) if _is_byte_string(arg) else arg for arg in args)


def _redact_record(record: logging.LogRecord) -> None:
    """Masks every credential a log record carries, in place.

    The arguments are masked one by one rather than the formatted message as a whole, so a header
    mapping is masked by its keys and a URL argument's masked value ends where the URL does, not at
    the next space of the surrounding message. A record with no arguments has its message masked
    instead, whatever it is: a logged `httpx.URL` carries the query too. Each part fails closed: one
    that cannot be masked is replaced by `REDACTED` rather than logged as it was.

    An attached traceback is formatted and masked into `exc_text`, which `logging.Formatter` uses as
    is (httpx quotes the request URL in a status error's message). `exc_info` itself is left alone,
    since a handler may need the exception object, so a formatter that reads `exc_info` rather than
    `exc_text` still sees the raw traceback.
    """
    if isinstance(record.args, Mapping):
        mapping = cast("Mapping[Any, Any]", record.args)
        record.args = {key: REDACTED if _is_secret_key(key) else _redact_arg(item) for key, item in mapping.items()}
    elif isinstance(record.args, tuple) and record.args:
        args = tuple(_redact_arg(arg) for arg in record.args)
        if isinstance(record.msg, str):
            args = _redact_header_lines(record.msg, args)
            if _is_hpack(record.name):
                args = _redact_header_blocks(record.msg, args)
        record.args = args
    elif isinstance(record.msg, str):
        record.msg = _redact_text(record.msg)
    else:
        record.msg = _redact_arg(record.msg)
    if record.exc_info and not record.exc_text:
        try:
            record.exc_text = redact(logging.Formatter().formatException(record.exc_info))
        except Exception:
            record.exc_text = REDACTED
    if isinstance(record.stack_info, str):
        record.stack_info = _redact_text(record.stack_info)


def _blank_record(record: logging.LogRecord) -> None:
    """Replaces everything a record could print with `REDACTED`, for one that could not be masked.

    The traceback goes too, `exc_info` as well as `exc_text`, since a handler that formats the
    exception itself would otherwise print it raw.
    """
    try:
        had_traceback = bool(record.exc_info or record.exc_text)
        record.msg = REDACTED
        record.args = ()
        record.exc_info = None
        record.exc_text = REDACTED if had_traceback else None
        record.stack_info = None
    except Exception:
        return


def _install_record_factory() -> None:
    """Wraps the process's log record factory so this SDK's records are masked as they are made.

    A record factory rather than a logger filter, because a logger's filters see only the records
    logged on that logger itself: every runtime module logs on a child (`<package>._base_client`),
    and httpx, httpcore and websockets on children of their own. Masking at creation also comes
    before every filter and handler, whoever configured them. The factory already installed is
    wrapped, not replaced, so another library's factory keeps working, and records of every other
    logger pass through untouched. A factory installed later that does not chain to this one turns
    the masking off.
    """
    previous = logging.getLogRecordFactory()

    def factory(*args: Any, **kwargs: Any) -> logging.LogRecord:
        """The previous factory's record, masked when it belongs to one of `_REDACTED_LOGGERS`.

        Nothing here may raise: the factory runs inside every `log.debug(...)` in the process, so
        a failure would break the caller's code rather than its logging.
        """
        record = previous(*args, **kwargs)
        try:
            if _redacts(record.name):
                _redact_record(record)
        except Exception:
            # Every part of `_redact_record` already fails closed; this is the last line, for a
            # record a part of which cannot even be read (a mapping whose `.items()` raises).
            _blank_record(record)
        return record

    logging.setLogRecordFactory(factory)


_install_record_factory()

logger: logging.Logger = logging.getLogger("dedalus_sdk")
httpx_logger: logging.Logger = logging.getLogger("httpx")


def _basic_config() -> None:
    # e.g. [2023-10-05 14:12:26 - dedalus_sdk._base_client:818 - DEBUG] HTTP Request: POST http://127.0.0.1:4010/foo/bar "200 OK"
    logging.basicConfig(
        format="[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_logging() -> None:
    env = os.environ.get("DEDALUS_LOG")
    if env == "debug":
        _basic_config()
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
    elif env == "info":
        _basic_config()
        logger.setLevel(logging.INFO)
        httpx_logger.setLevel(logging.INFO)
