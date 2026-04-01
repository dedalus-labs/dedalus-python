# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MachineUpdateParams"]


class MachineUpdateParams(TypedDict, total=False):
    machine_id: Required[str]

    if_match: Required[Annotated[str, PropertyInfo(alias="If-Match")]]

    memory_mib: int
    """Memory in MiB."""

    storage_gib: int
    """Storage in GiB."""

    vcpu: float
    """CPU in vCPUs."""
