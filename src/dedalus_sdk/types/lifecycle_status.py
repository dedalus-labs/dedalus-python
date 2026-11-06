# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LifecycleStatus", "Autoresize", "AutoresizeCPU", "AutoresizeMemory"]


class AutoresizeMemory(BaseModel):
    blocked_at: Optional[datetime] = None
    """Time the current refusal was first recorded."""

    blocked_reason: Optional[
        Literal[
            "MACHINE_GROWTH_LIMIT_REACHED",
            "MACHINE_TIER_SHAPE_EXCEEDED",
            "MACHINE_QUOTA_EXCEEDED",
            "MACHINE_MEMORY_ABOVE_LIMIT",
            "ASSIGNED_HOST_CAPACITY_CONFLICT",
            "MACHINE_PLACEMENT_EXHAUSTED",
            "MACHINE_RESIZE_UNAVAILABLE",
            "MACHINE_SHAPE_UNSUPPORTED",
        ]
    ] = None
    """Why the latest automatic increase could not proceed, as the error code an explicit resize would return. Absent once an automatic increase is accepted."""


class AutoresizeCPU(BaseModel):
    blocked_at: Optional[datetime] = None
    """Time the current refusal was first recorded."""

    blocked_reason: Optional[
        Literal[
            "MACHINE_GROWTH_LIMIT_REACHED",
            "MACHINE_TIER_SHAPE_EXCEEDED",
            "MACHINE_QUOTA_EXCEEDED",
            "MACHINE_MEMORY_ABOVE_LIMIT",
            "ASSIGNED_HOST_CAPACITY_CONFLICT",
            "MACHINE_PLACEMENT_EXHAUSTED",
            "MACHINE_RESIZE_UNAVAILABLE",
            "MACHINE_SHAPE_UNSUPPORTED",
        ]
    ] = None
    """Why the latest automatic increase could not proceed, as the error code an explicit resize would return. Absent once an automatic increase is accepted."""


class Autoresize(BaseModel):
    cpu: Optional[AutoresizeCPU] = None

    memory: Optional[AutoresizeMemory] = None


class LifecycleStatus(BaseModel):
    autoresize: Autoresize

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
