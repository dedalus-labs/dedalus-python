# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["MachineStorageUsageEvidence"]


class MachineStorageUsageEvidence(BaseModel):
    bucket_end: datetime
    """Exclusive evidence bucket end."""

    bucket_start: datetime
    """Inclusive evidence bucket start."""

    logical_storage_bytes: int
    """Machine logical bytes observed for storage allocation."""

    machine_id: str
    """Machine identifier."""

    org_metering_bucket_id: str
    """Org storage bucket ID this evidence row contributes to."""

    storage_mib_seconds: int
    """Allocated logical MiB-seconds for this machine."""

    stripe_storage_identifier: str
    """Stripe storage meter event identifier linked to that org bucket."""

    latest_stripe_emitted_at: Optional[datetime] = None
    """Latest Stripe emission timestamp for the linked org bucket, when emitted."""
