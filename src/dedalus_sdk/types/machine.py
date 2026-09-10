# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Machine"]


class Machine(BaseModel):
    autosleep_seconds: int
    """Seconds of inactivity before autosleep. 0 disables autosleep."""

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
