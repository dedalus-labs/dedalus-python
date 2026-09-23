# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MachineListItem"]


class MachineListItem(BaseModel):
    autosleep_seconds: int
    """Seconds of inactivity before autosleep. 0 disables autosleep."""

    created_at: datetime

    desired_state: Literal["running", "sleeping", "destroyed"]

    machine_id: str

    memory_mib: int
    """Memory in MiB."""

    phase: Literal[
        "accepted",
        "placement_pending",
        "starting",
        "running",
        "stopping",
        "sleeping",
        "destroying",
        "destroyed",
        "failed",
    ]

    storage_gib: int

    vcpu: float
    """CPU in vCPUs."""
