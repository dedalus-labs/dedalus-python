# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ImageUpdateParams"]


class ImageUpdateParams(TypedDict, total=False):
    image_id: Required[str]

    name: Required[Optional[str]]
    """The new label, or null to clear it. No other field can change."""
