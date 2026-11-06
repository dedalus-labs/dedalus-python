# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AutoresizingUpdateParams"]


class AutoresizingUpdateParams(TypedDict, total=False):
    cpu: Literal["on", "off"]

    cpu_max_vcpu: Optional[float]

    memory: Literal["on", "off"]

    memory_max_mib: Optional[int]
