# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutoresizingUpdateParams"]


class AutoresizingUpdateParams(TypedDict, total=False):
    enabled: Required[bool]
    """Allow automatic RAM increases for all organization machines. Disabling preserves applied RAM and already admitted resizes."""
