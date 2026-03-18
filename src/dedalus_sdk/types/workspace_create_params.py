# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkspaceCreateParams"]


class WorkspaceCreateParams(TypedDict, total=False):
    image_version: Required[str]

    memory_mib: Required[int]
    """Memory in MiB."""

    storage_gib: Required[int]

    vcpu: Required[float]
    """CPU in vCPUs."""
