# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MachineCreateParams"]


class MachineCreateParams(TypedDict, total=False):
    autosleep: str
    """Idle window before autosleep.

    Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds
    ("1800"), or never to disable.
    """

    memory_mib: int
    """Memory in MiB."""

    storage_gib: int
    """Storage in GiB."""

    vcpu: float
    """CPU in vCPUs."""
