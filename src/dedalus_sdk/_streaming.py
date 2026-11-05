from __future__ import annotations

import re
import sys
import json
import inspect
from types import TracebackType
from typing import TYPE_CHECKING, Any, Generic, TypeVar, Iterator, Optional, AsyncIterator, cast
from typing_extensions import Self, Protocol, TypeGuard, override, get_origin, runtime_checkable

import httpx

from ._utils import extract_type_var_from_base
from ._decoding import iter_decoded, aiter_decoded
from ._exceptions import DedalusError

if TYPE_CHECKING:
    from ._client import Dedalus, AsyncDedalus
    from ._models import FinalRequestOptions


_T = TypeVar("_T")


class Stream(Generic[_T]):
    """Provides the core interface to iterate over a synchronous stream response."""

    response: httpx.Response
    _options: Optional[FinalRequestOptions] = None
    _decoder: SSEBytesDecoder

    def __init__(
        self,
        *,
        cast_to: type[_T],
        response: httpx.Response,
        client: Dedalus,
        options: Optional[FinalRequestOptions] = None,
    ) -> None:
        self.response = response
        self._cast_to = cast_to
        self._client = client
        self._options = options
        self._decoder = client._make_sse_decoder()
        self._iterator = self.__stream__()

    def __next__(self) -> _T:
        return self._iterator.__next__()

    def __iter__(self) -> Iterator[_T]:
        for item in self._iterator:
            yield item

    def _iter_events(self) -> Iterator[ServerSentEvent]:
        yield from self._decoder.iter_bytes(iter_decoded(self.response))

    def __stream__(self) -> Iterator[_T]:
        cast_to = cast(Any, self._cast_to)
        response = self.response
        process_data = self._client._process_response_data
        iterator = self._iter_events()

        try:
            for sse in iterator:
                if not sse.data:
                    continue
                try:
                    payload = sse.json()
                except Exception:
                    payload = sse.data
                yield process_data(data=payload, cast_to=cast_to, response=response)
        finally:
            # Ensure the response is closed even if the consumer doesn't read all data
            response.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def close(self) -> None:
        """
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        """
        self.response.close()


class AsyncStream(Generic[_T]):
    """Provides the core interface to iterate over an asynchronous stream response."""

    response: httpx.Response
    _options: Optional[FinalRequestOptions] = None
    _decoder: SSEDecoder | SSEBytesDecoder

    def __init__(
        self,
        *,
        cast_to: type[_T],
        response: httpx.Response,
        client: AsyncDedalus,
        options: Optional[FinalRequestOptions] = None,
    ) -> None:
        self.response = response
        self._cast_to = cast_to
        self._client = client
        self._options = options
        self._decoder = client._make_sse_decoder()
        self._iterator = self.__stream__()

    async def __anext__(self) -> _T:
        return await self._iterator.__anext__()

    async def __aiter__(self) -> AsyncIterator[_T]:
        async for item in self._iterator:
            yield item

    async def _iter_events(self) -> AsyncIterator[ServerSentEvent]:
        async for sse in self._decoder.aiter_bytes(aiter_decoded(self.response)):
            yield sse

    async def __stream__(self) -> AsyncIterator[_T]:
        cast_to = cast(Any, self._cast_to)
        response = self.response
        process_data = self._client._process_response_data
        iterator = self._iter_events()

        try:
            async for sse in iterator:
                if not sse.data:
                    continue
                try:
                    payload = sse.json()
                except Exception:
                    payload = sse.data
                yield process_data(data=payload, cast_to=cast_to, response=response)
        finally:
            # Ensure the response is closed even if the consumer doesn't read all data
            await response.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        """
        Close the response and release the connection.

        Automatically called if the response body is read to completion.
        """
        await self.response.aclose()


class ServerSentEvent:
    def __init__(
        self,
        *,
        event: str | None = None,
        data: str | None = None,
        id: str | None = None,
        retry: int | None = None,
    ) -> None:
        if data is None:
            data = ""

        self._id = id
        self._data = data
        self._event = event or None
        self._retry = retry

    @property
    def event(self) -> str | None:
        return self._event

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def retry(self) -> int | None:
        return self._retry

    @property
    def data(self) -> str:
        return self._data

    def json(self) -> Any:
        return json.loads(self.data)

    @override
    def __repr__(self) -> str:
        return f"ServerSentEvent(event={self.event}, data={self.data}, id={self.id}, retry={self.retry})"


_LINE_TERMINATOR = re.compile(rb"\r\n|\r|\n")
_UTF8_BOM = b"\xef\xbb\xbf"

# The most bytes one line still waiting for its terminator, or one event still waiting for the blank
# line that dispatches it, may hold. A server that never ends a line or an event would otherwise
# make the decoder buffer without bound.
MAX_PENDING_BYTES = 64 * 1024 * 1024

# What one pending `data` line costs besides the string itself: its slot in the list of lines.
_LIST_SLOT_BYTES = 8


def _pending_too_large(what: str) -> DedalusError:
    """The error for a stream whose pending `what` grew past `MAX_PENDING_BYTES`."""
    return DedalusError(
        f"Server-sent event stream {what} exceeds the {MAX_PENDING_BYTES} byte limit "
        f"({MAX_PENDING_BYTES // (1024 * 1024)} MiB)"
    )


class SSEDecoder:
    """Incremental decoder for a `text/event-stream` body.

    Follows "Interpreting an event stream" in the WHATWG HTML standard:
    https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation

    Bytes arrive in arbitrary network chunks, so an unfinished line is buffered until its line
    terminator arrives. As the standard requires, a byte order mark opening the stream is skipped,
    bytes that are not valid UTF-8 decode to U+FFFD, and an event still pending when the stream ends
    (it never saw the blank line that dispatches it) is dropped.
    """

    def __init__(self) -> None:
        self._event: str | None = None
        self._data: list[str] = []
        # Characters held in `_data`, kept beside it so the event cap costs nothing per line.
        self._data_size = 0
        self._last_event_id: str | None = None
        self._retry: int | None = None
        # The pieces of a line whose terminator has not arrived yet, joined once it does so a long
        # line arriving in many chunks is copied once rather than once per chunk.
        self._pending: list[bytes] = []
        # Bytes held in `_pending`, kept beside it so the line cap costs nothing per chunk.
        self._pending_size = 0
        # Set when a chunk ended on `\r`: a `\n` opening the next chunk completes that `\r\n`, so it
        # must not be read as a second, empty line (which would dispatch an event).
        self._skip_leading_lf = False
        # The opening bytes of the stream, held until there are enough to tell whether they are a
        # byte order mark (which can itself arrive split across chunks); `None` once that is settled.
        self._head: bytes | None = b""

    def iter_bytes(self, iterator: Iterator[bytes]) -> Iterator[ServerSentEvent]:
        """Decodes raw body chunks and yields each event as soon as its blank line arrives."""
        for chunk in iterator:
            yield from self._feed(chunk)

    async def aiter_bytes(self, iterator: AsyncIterator[bytes]) -> AsyncIterator[ServerSentEvent]:
        """Decodes raw async body chunks and yields each event as soon as its blank line arrives."""
        async for chunk in iterator:
            for sse in self._feed(chunk):
                yield sse

    def _feed(self, chunk: bytes) -> Iterator[ServerSentEvent]:
        """Consumes one chunk and yields the events completed by the lines it finishes."""
        if not chunk:
            return
        if self._head is not None:
            chunk = self._head + chunk
            if len(chunk) < len(_UTF8_BOM) and _UTF8_BOM.startswith(chunk):
                self._head = chunk
                return
            self._head = None
            if chunk.startswith(_UTF8_BOM):
                chunk = chunk[len(_UTF8_BOM) :]
                if not chunk:
                    return
        if self._skip_leading_lf and chunk.startswith(b"\n"):
            chunk = chunk[1:]
        self._skip_leading_lf = chunk.endswith(b"\r")

        # Lines are split on the raw bytes, which no UTF-8 continuation byte can be mistaken for,
        # and each complete line is decoded on its own so a character split across chunks waits
        # in `_pending` with the rest of its line. Only the new chunk is scanned: `_pending` holds
        # no terminator, and a `\r\n` split across chunks was handled above.
        *finished, unfinished = _LINE_TERMINATOR.split(chunk)
        if not finished:
            self._hold(unfinished)
            return
        if self._pending_size + len(finished[0]) > MAX_PENDING_BYTES:
            raise _pending_too_large("line")
        lines = [b"".join([*self._pending, finished[0]]), *finished[1:]]
        self._pending = []
        self._pending_size = 0
        self._hold(unfinished)
        for line in lines:
            sse = self.decode(line.decode("utf-8", errors="replace"))
            if sse is not None:
                yield sse

    def _hold(self, piece: bytes) -> None:
        """Keeps `piece`, the start of a line whose terminator has not arrived, within the line cap."""
        if not piece:
            return
        self._pending_size += len(piece)
        if self._pending_size > MAX_PENDING_BYTES:
            raise _pending_too_large("line")
        self._pending.append(piece)

    def decode(self, line: str) -> ServerSentEvent | None:
        """Processes one line, without its terminator, and returns the event a blank line dispatches."""
        if not line:
            return self._dispatch()

        if line.startswith(":"):
            # A comment, such as a keep-alive.
            return None

        # A line with no colon names a field whose value is empty.
        name, _, value = line.partition(":")
        if value.startswith(" "):
            value = value[1:]

        if name == "data":
            # Each `data` line is held as its own string in a list until the event ends, so it is
            # charged what that costs in memory: the string's own size (up to 4 bytes a character
            # for astral text, plus its header) and its list slot. An empty line is not free.
            self._data_size += sys.getsizeof(value) + _LIST_SLOT_BYTES
            if self._data_size > MAX_PENDING_BYTES:
                raise _pending_too_large("event")
            self._data.append(value)
        elif name == "event":
            self._event = value
        elif name == "id":
            # The standard ignores an id containing NUL rather than truncating it.
            if "\0" not in value:
                self._last_event_id = value
        elif name == "retry":
            # Only ASCII digits count; `int()` alone would also take a sign, spaces or other scripts' digits.
            if value.isascii() and value.isdigit():
                self._retry = int(value)
        # Any other field name is ignored.
        return None

    def _dispatch(self) -> ServerSentEvent | None:
        """Builds the event a blank line completes, and resets the per-event fields."""
        # An event with no data still dispatches when it set a name, an id or a retry, so a consumer
        # sees named events that carry no payload. The last event id persists across events, so
        # once one is set every blank line dispatches.
        if not (self._data or self._event or self._last_event_id or self._retry is not None):
            return None

        sse = ServerSentEvent(
            event=self._event,
            data="\n".join(self._data),
            id=self._last_event_id,
            retry=self._retry,
        )
        self._event = None
        self._data = []
        self._data_size = 0
        self._retry = None
        return sse


@runtime_checkable
class SSEBytesDecoder(Protocol):
    def iter_bytes(self, iterator: Iterator[bytes]) -> Iterator[ServerSentEvent]:
        """Given an iterator that yields raw binary data, iterate over it & yield every event encountered"""
        ...

    def aiter_bytes(self, iterator: AsyncIterator[bytes]) -> AsyncIterator[ServerSentEvent]:
        """Given an async iterator that yields raw binary data, iterate over it & yield every event encountered"""
        ...


def is_stream_class_type(typ: type) -> TypeGuard[type[Stream[object]] | type[AsyncStream[object]]]:
    """TypeGuard for determining whether or not the given type is a subclass of `Stream` / `AsyncStream`"""
    origin = get_origin(typ) or typ
    return inspect.isclass(origin) and issubclass(origin, (Stream, AsyncStream))


def extract_stream_chunk_type(
    stream_cls: type,
    *,
    failure_message: str | None = None,
) -> type:
    """Given a type like `Stream[T]`, returns the generic type variable `T`.

    This also handles the case where a concrete subclass is given, e.g.
    ```py
    class MyStream(Stream[bytes]):
        ...

    extract_stream_chunk_type(MyStream) -> bytes
    ```
    """
    from ._base_client import Stream, AsyncStream

    return extract_type_var_from_base(
        stream_cls,
        index=0,
        generic_bases=cast("tuple[type, ...]", (Stream, AsyncStream)),
        failure_message=failure_message,
    )
