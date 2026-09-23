# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MachineUpdateParams"]


class MachineUpdateParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    autosleep: str
    """Idle window before autosleep. Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds ("1800"), or never to disable."""

    memory_mib: int
    """Memory in MiB."""

    storage_gib: int
    """Storage in GiB."""

    vcpu: float
    """CPU in vCPUs."""
