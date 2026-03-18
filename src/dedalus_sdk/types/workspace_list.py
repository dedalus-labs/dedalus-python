# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .lifecycle_status import LifecycleStatus

__all__ = ["WorkspaceList", "Item"]


class Item(BaseModel):
    created_at: datetime

    desired_state: Literal["active", "inactive", "destroyed"]

    memory_mib: int
    """Memory in MiB."""

    status: LifecycleStatus

    storage_gib: int

    vcpu: float
    """CPU in vCPUs."""

    workspace_id: str

    image_version: Optional[str] = None


class WorkspaceList(BaseModel):
    items: Optional[List[Item]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    next_cursor: Optional[str] = None
