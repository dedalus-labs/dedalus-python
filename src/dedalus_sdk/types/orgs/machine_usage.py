# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .machine_usage_evidence import MachineUsageEvidence

__all__ = ["MachineUsage"]


class MachineUsage(BaseModel):
    granularity: str
    """Evidence granularity used for rows: hour or day."""

    period_end: datetime
    """Exclusive evidence period end."""

    period_start: datetime
    """Inclusive evidence period start."""

    rows: Optional[List[MachineUsageEvidence]] = None
    """Machine-level usage evidence rows."""
