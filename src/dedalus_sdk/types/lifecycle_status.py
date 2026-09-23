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
