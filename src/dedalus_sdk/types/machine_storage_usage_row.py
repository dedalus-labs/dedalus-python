# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MachineStorageUsageRow"]


class MachineStorageUsageRow(BaseModel):
    bucket_end: datetime
    """Exclusive usage bucket end."""

    bucket_start: datetime
    """Inclusive usage bucket start."""

    latest_meter_emitted_at: Optional[datetime] = None
    """Latest meter emission timestamp for the linked org bucket, when emitted."""

    logical_storage_bytes: int
    """Machine logical bytes observed for storage allocation."""

    machine_id: str
    """Machine identifier."""

    org_metering_bucket_id: str
    """Org storage bucket ID this row contributes to."""

    storage_mib_seconds: int
    """Allocated logical MiB-seconds for this machine."""
