# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    stripe_cpu_identifiers: Optional[List[str]] = None
    """Stripe CPU meter event identifiers linked to those org buckets."""

    stripe_memory_identifiers: Optional[List[str]] = None
    """Stripe memory meter event identifiers linked to those org buckets."""

    window_count: int
    """Raw usage windows compacted into this row."""

    latest_stripe_emitted_at: Optional[datetime] = None
    """Latest Stripe emission timestamp for linked org buckets, when emitted."""
