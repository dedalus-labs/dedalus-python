# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Port", "InitialAccessKey"]


class InitialAccessKey(BaseModel):
    access_key: str

    access_key_id: str

    created_at: datetime

    expires_at: datetime

    last_used_at: Optional[datetime] = None
    """Most recent durably recorded use, coalesced to five-minute resolution."""

    port_id: str

    revoked_at: Optional[datetime] = None


class Port(BaseModel):
    application_url: str
    """Isolated guest application origin. Direct clients preserve their HTTP method and body and send any required Dedalus credential in headers."""

    created_at: datetime

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    expires_at: Optional[datetime] = None

    initial_access_key: Optional[InitialAccessKey] = None
    """Initial key for a newly created key_required port. Plaintext is returned once and omitted on replay."""

    machine_id: str

    port: int

    port_id: str

    protocol: Optional[Literal["http"]] = None

    ready_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None

    status: Literal["wake_in_progress", "ready", "unavailable", "closed", "expired", "failed"]
    """Unavailable is a recoverable failure reaching the guest service. See error_code and error_message for the diagnosis."""

    url: Optional[str] = None
    """Stable browser share URL. Browser navigation only; use application_url for APIs, webhooks, and WebSockets."""

    visibility: Literal["public", "key_required", "private"]
