# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .machine_storage_usage_row import MachineStorageUsageRow

__all__ = ["MachineStorageUsage"]


class MachineStorageUsage(BaseModel):
    period_end: datetime
    """Exclusive usage period end."""

    period_start: datetime
    """Inclusive usage period start."""

    rows: Optional[List[MachineStorageUsageRow]] = None
    """Machine-level storage usage breakdown rows."""
