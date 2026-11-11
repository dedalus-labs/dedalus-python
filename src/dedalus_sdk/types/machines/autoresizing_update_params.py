# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..autoresizing_switch import AutoresizingSwitch

__all__ = ["AutoresizingUpdateParams"]


class AutoresizingUpdateParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    cpu: AutoresizingSwitch

    cpu_max_vcpu: Optional[float]

    memory: AutoresizingSwitch

    memory_max_mib: Optional[int]
