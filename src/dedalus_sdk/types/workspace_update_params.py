# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkspaceUpdateParams"]


class WorkspaceUpdateParams(TypedDict, total=False):
    if_match: Required[Annotated[str, PropertyInfo(alias="If-Match")]]

    memory_mib: int
    """Memory in MiB."""

    storage_gib: int

    vcpu: float
    """CPU in vCPUs."""
