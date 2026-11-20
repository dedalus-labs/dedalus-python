# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["AccessKeyListResponse", "Item"]


class Item(BaseModel):
    access_key_id: str

    created_at: datetime

    expires_at: datetime

    last_used_at: Optional[datetime] = None
    """Most recent durably recorded use, coalesced to five-minute resolution."""

    port_id: str

    revoked_at: Optional[datetime] = None


class AccessKeyListResponse(BaseModel):
    items: Optional[List[Item]] = None

    next_cursor: Optional[str] = None
