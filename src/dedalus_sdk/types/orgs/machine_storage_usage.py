# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .machine_storage_usage_evidence import MachineStorageUsageEvidence

__all__ = ["MachineStorageUsage"]


class MachineStorageUsage(BaseModel):
    period_end: datetime
    """Exclusive evidence period end."""

    period_start: datetime
    """Inclusive evidence period start."""

    rows: Optional[List[MachineStorageUsageEvidence]] = None
    """Machine-level storage usage evidence rows."""
