# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .machine_compute_usage_row import MachineComputeUsageRow

__all__ = ["MachineComputeUsage"]


class MachineComputeUsage(BaseModel):
    granularity: str
    """Usage breakdown granularity used for rows: hour or day."""

    period_end: datetime
    """Exclusive usage period end."""

    period_start: datetime
    """Inclusive usage period start."""

    rows: Optional[List[MachineComputeUsageRow]] = None
    """Machine-level compute usage breakdown rows."""
