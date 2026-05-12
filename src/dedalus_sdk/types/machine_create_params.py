# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MachineCreateParams"]


class MachineCreateParams(TypedDict, total=False):
    memory_mib: Required[int]
    """Memory in MiB."""

    storage_gib: Required[int]
    """Storage in GiB."""

    vcpu: Required[float]
    """CPU in vCPUs."""

    autosleep: str
    """Idle window before autosleep.

    Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds
    ("1800"), or never to disable.
    """
