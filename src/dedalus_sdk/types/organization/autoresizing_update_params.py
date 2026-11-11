# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..autoresizing_switch import AutoresizingSwitch

__all__ = ["AutoresizingUpdateParams"]


class AutoresizingUpdateParams(TypedDict, total=False):
    cpu: AutoresizingSwitch

    cpu_max_vcpu: Optional[float]

    memory: AutoresizingSwitch

    memory_max_mib: Optional[int]
