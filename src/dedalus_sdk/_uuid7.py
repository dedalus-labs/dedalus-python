"""Time-ordered (version 7) UUIDs for idempotency keys.

The standard library gains `uuid.uuid7` only in Python 3.14, and the SDK supports older versions
without a third-party dependency, so this module builds one by hand per RFC 9562.
"""

from __future__ import annotations

import os
import time
import uuid


def uuid7() -> uuid.UUID:
    """A version 7 UUID: a 48-bit Unix millisecond timestamp, then version and variant bits, the rest random."""
    value = bytearray(os.urandom(16))
    # Clamped, because `to_bytes` rejects a negative int: a clock set before 1970 writes a zero timestamp.
    value[0:6] = max(0, time.time_ns() // 1_000_000).to_bytes(6, "big")
    value[6] = (value[6] & 0x0F) | 0x70
    value[8] = (value[8] & 0x3F) | 0x80
    return uuid.UUID(bytes=bytes(value))
