# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AccessKeyMintResponse"]


class AccessKeyMintResponse(BaseModel):
    access_key: str

    access_key_id: str

    created_at: datetime

    expires_at: datetime

    last_used_at: Optional[datetime] = None
    """Most recent durably recorded use, coalesced to five-minute resolution."""

    port_id: str

    revoked_at: Optional[datetime] = None
