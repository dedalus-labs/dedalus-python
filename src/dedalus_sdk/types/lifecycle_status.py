# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LifecycleStatus"]


class LifecycleStatus(BaseModel):
    last_error: Optional[str] = None

    last_progress_at: datetime

    last_transition_at: datetime

    memory_assigned_mib: Optional[int] = None
    """Last confirmed RAM allocation for the current running generation. Absent when the allocation is unknown or no longer current."""

    memory_configured_mib: int
    """Accepted RAM maximum, including completed automatic increases."""

    memory_last_autoresized_at: Optional[datetime] = None
    """Time of the latest confirmed automatic RAM increase. Does not include explicit resizing or a complete change history."""

    memory_resize_state: Optional[Literal["stable", "error", "pending_capacity"]] = None
    """Resize progress reported by the current runtime. A pending automatic target may not yet be applied by that runtime."""

    memory_target_mib: Optional[int] = None
    """Pending automatic RAM target, or the current runtime target when no automatic target is pending."""

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

    reason: str

    retryable: bool

    revision: str
