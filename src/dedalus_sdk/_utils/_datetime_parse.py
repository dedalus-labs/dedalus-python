"""
Parsing for the `date` and `date-time` values a response carries.

Models built without validation (`construct_type`) turn these values into `date` and `datetime`
objects here. A string is read as a date or date-time in the RFC 3339 / ISO 8601 shape, with the
departures `_DATE` and `_DATE_TIME` list; a number, or a string or bytes holding one, is read as a
Unix timestamp.

`datetime.fromisoformat` is not used: before Python 3.11 it rejects a `Z` offset and fractions that
are not exactly three or six digits, and the supported floor is lower than that.
"""

from __future__ import annotations

import re
from typing import Union, Optional
from datetime import date, datetime, timezone, timedelta

from .._types import StrBytesIntFloat

# RFC 3339 `full-date`, loosened to accept a one-digit month or day.
_DATE = re.compile(r"(\d{4})-(\d\d?)-(\d\d?)$")

# RFC 3339 `date-time`, loosened the same way: a space may stand in for `T`, the seconds may be left
# out, and the offset may be `Z`, `+HH`, `+HHMM` or `+HH:MM`, or missing for a local time. It is also
# stricter in two places: `T` and `Z` must be uppercase, and a leap second (`:60`) is rejected,
# because `datetime` cannot hold one.
_DATE_TIME = re.compile(
    r"""
    (\d{4}) - (\d\d?) - (\d\d?)
    [T ]
    (\d\d?) : (\d\d?)
    (?: : (\d\d?) (?: \. (\d{1,12}) )? )?
    (Z | [+-] \d\d (?: :? \d\d )? )?
    $
    """,
    re.VERBOSE,
)

_UNIX_EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
# A timestamp whose magnitude is above this is taken to be in milliseconds (or a finer unit): as
# seconds it would land after the year 2603.
_SECONDS_LIMIT = 2e10
# Past this magnitude no unit brings the value inside the range `datetime` can represent.
_CLAMP_LIMIT = 3e20


def _number_or_text(value: object, kind: str) -> Union[int, float, str]:
    """Sorts an input into a timestamp (returned as a number) or text to parse as a `kind`.

    Text that reads as a number, such as `"1700000000"` or even `"2024"`, is a timestamp. Any other
    type `float()` accepts, such as `Decimal` or a NumPy scalar, is a timestamp too; everything else
    raises `TypeError`.
    """
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, bytes):
        value = value.decode()
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return value
    try:
        return float(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        raise TypeError(f"cannot parse a {type(value).__name__} as a {kind}") from None


def _from_timestamp(number: Union[int, float]) -> datetime:
    """Converts a Unix timestamp to an aware UTC `datetime`.

    The unit is inferred from the size: a value too large to be seconds is read as milliseconds,
    one too large for that as microseconds, and so on. A value too large for any unit is clamped to
    the naive `datetime.max` or `datetime.min`.
    """
    magnitude = abs(number)
    if magnitude > _CLAMP_LIMIT:
        return datetime.max if number > 0 else datetime.min
    divisor = 1
    while magnitude > _SECONDS_LIMIT * divisor:
        divisor *= 1000
    return _UNIX_EPOCH + timedelta(seconds=number / divisor)


def _zone(offset: Optional[str]) -> Optional[timezone]:
    """Returns the fixed-offset zone a `Z` or `±HH[[:]MM]` suffix names, or `None` for no suffix."""
    if offset is None:
        return None
    if offset == "Z":
        return timezone.utc
    digits = offset[1:].replace(":", "")
    delta = timedelta(hours=int(digits[:2]), minutes=int(digits[2:] or 0))
    # `timezone` itself rejects an offset of a day or more with a `ValueError`.
    return timezone(-delta if offset.startswith("-") else delta)


def parse_datetime(value: Union[datetime, StrBytesIntFloat]) -> datetime:
    """
    Parses a date-time string, or a Unix timestamp in seconds or milliseconds, into a `datetime`.

    A string with an offset gives an aware `datetime` with that fixed offset, and one without gives
    a naive one. A timestamp gives an aware UTC `datetime`, except that one beyond the representable
    range is clamped to the naive `datetime.max` or `datetime.min`. A `datetime` is returned unchanged.

    Raises `ValueError` for a malformed string or out-of-range fields, and `TypeError` for any other
    input type.
    """
    if isinstance(value, datetime):
        return value

    parsed = _number_or_text(value, "datetime")
    if not isinstance(parsed, str):
        return _from_timestamp(parsed)

    match = _DATE_TIME.match(parsed)
    if match is None:
        raise ValueError("invalid date-time format")
    year, month, day, hour, minute, second, fraction, offset = match.groups()
    # Pad the fraction out to microseconds, or cut it down to them.
    microsecond = int(f"{fraction or ''}000000"[:6])
    return datetime(
        int(year),
        int(month),
        int(day),
        int(hour),
        int(minute),
        int(second or 0),
        microsecond,
        tzinfo=_zone(offset),
    )


def parse_date(value: Union[date, StrBytesIntFloat]) -> date:
    """
    Parses a date string, or a Unix timestamp in seconds or milliseconds, into a `date`.

    A `datetime` gives its date part, and a `date` is returned unchanged.

    Raises `ValueError` for a malformed string or an impossible date, and `TypeError` for any other
    input type.
    """
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value

    parsed = _number_or_text(value, "date")
    if not isinstance(parsed, str):
        return _from_timestamp(parsed).date()

    match = _DATE.match(parsed)
    if match is None:
        raise ValueError("invalid date format")
    year, month, day = (int(part) for part in match.groups())
    return date(year, month, day)
