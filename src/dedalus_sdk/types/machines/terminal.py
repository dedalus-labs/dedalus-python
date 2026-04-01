# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Terminal"]


class Terminal(BaseModel):
    created_at: datetime

    height: int

    machine_id: str

    status: Literal["wake_in_progress", "ready", "closed", "expired", "failed"]

    terminal_id: str

    width: int

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    expires_at: Optional[datetime] = None

    protocol: Optional[Literal["websocket"]] = None

    ready_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None

    stream_url: Optional[str] = None
