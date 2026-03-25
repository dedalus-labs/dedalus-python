# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .lifecycle_status import LifecycleStatus

__all__ = ["Workspace"]


class Workspace(BaseModel):
    desired_state: Literal["running", "sleeping", "destroyed"]

    memory_mib: int
    """Memory in MiB."""

    status: LifecycleStatus

    storage_gib: int

    vcpu: float
    """CPU in vCPUs."""

    workspace_id: str
