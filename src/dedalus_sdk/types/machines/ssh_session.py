# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

from .ssh_connection import SSHConnection

__all__ = ["SSHSession"]


class SSHSession(BaseModel):
    connection: Optional[SSHConnection] = None

    created_at: datetime

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    expires_at: Optional[datetime] = None

    machine_id: str

    ready_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None

    session_id: str

    status: Literal["wake_in_progress", "ready", "closed", "expired", "failed"]
