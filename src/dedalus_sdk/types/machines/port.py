# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Port"]


class Port(BaseModel):
    created_at: datetime

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    expires_at: Optional[datetime] = None

    machine_id: str

    port: int

    port_id: str

    protocol: Optional[Literal["http", "https"]] = None

    ready_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None

    status: Literal["wake_in_progress", "ready", "closed", "expired", "failed"]

    url: Optional[str] = None
