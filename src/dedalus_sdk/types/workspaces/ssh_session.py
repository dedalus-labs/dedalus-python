# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .ssh_connection import SSHConnection

__all__ = ["SSHSession"]


class SSHSession(BaseModel):
    created_at: datetime

    session_id: str

    status: Literal["wake_in_progress", "ready", "closed", "expired", "failed"]

    workspace_id: str

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    connection: Optional[SSHConnection] = None

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    expires_at: Optional[datetime] = None

    ready_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None
