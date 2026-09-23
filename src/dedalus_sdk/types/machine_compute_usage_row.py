# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MachineComputeUsageRow"]


class MachineComputeUsageRow(BaseModel):
    awake_seconds: int
    """Machine-awake seconds in this bucket."""

    bucket_end: datetime
    """Exclusive usage bucket end."""

    bucket_start: datetime
    """Inclusive usage bucket start."""

    cpu_millicore_seconds: int
    """Requested vCPU millicores multiplied by guest-owned active CPU seconds."""

    last_window_end: datetime
    """Latest raw window_end represented by this row."""

    latest_meter_emitted_at: Optional[datetime] = None
    """Latest meter emission timestamp for linked org buckets, when emitted."""

    machine_id: str
    """Machine identifier."""

    memory_mib_seconds: int
    """Requested memory MiB multiplied by running allocation seconds."""

    org_metering_bucket_ids: Optional[List[str]] = None
    """Org compute bucket IDs this row contributes to."""

    requested_memory_mib: int
    """Requested memory for this shape, in MiB."""

    requested_storage_gib: int
    """Requested storage for this shape, in GiB."""

    requested_vcpu: float
    """Requested vCPU for this shape."""

    spec_fingerprint: str
    """Stable fingerprint for the requested machine shape."""

    window_count: int
    """Raw metering events compacted into this row."""
