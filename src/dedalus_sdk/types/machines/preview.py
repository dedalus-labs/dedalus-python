# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Preview"]


class Preview(BaseModel):
    created_at: datetime

    machine_id: str

    port: int

    preview_id: str

    status: Literal["wake_in_progress", "ready", "closed", "expired", "failed"]

    visibility: Literal["public", "private", "org"]

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    expires_at: Optional[datetime] = None

    protocol: Optional[Literal["http", "https"]] = None

    ready_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None

    url: Optional[str] = None
