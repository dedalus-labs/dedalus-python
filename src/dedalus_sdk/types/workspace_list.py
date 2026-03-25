# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .lifecycle_status import LifecycleStatus

__all__ = ["WorkspaceList", "Item"]


class Item(BaseModel):
    created_at: datetime

    desired_state: Literal["running", "sleeping", "destroyed"]

    memory_mib: int
    """Memory in MiB."""

    status: LifecycleStatus

    storage_gib: int

    vcpu: float
    """CPU in vCPUs."""

    workspace_id: str


class WorkspaceList(BaseModel):
    items: Optional[List[Item]] = None

    next_cursor: Optional[str] = None
