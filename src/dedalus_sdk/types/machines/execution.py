# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

from .artifact_ref import ArtifactRef

__all__ = ["Execution", "LogCapture"]


class LogCapture(BaseModel):
    code: Optional[str] = None

    lost_bytes: Optional[str] = None

    state: Optional[Literal["pending", "incomplete", "unavailable"]] = None

    unconfirmed_bytes: Optional[str] = None


class Execution(BaseModel):
    artifacts: Optional[List[ArtifactRef]] = None

    command: Optional[List[str]] = None

    completed_at: Optional[datetime] = None

    created_at: datetime

    creation_request_id: Optional[str] = None

    creation_trace_id: Optional[str] = None

    cwd: Optional[str] = None

    env_keys: Optional[List[str]] = None

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    execution_id: str

    exit_code: Optional[int] = None

    expires_at: Optional[datetime] = None

    log_capture: LogCapture

    machine_id: str

    retry_after_ms: Optional[int] = None

    signal: Optional[int] = None

    started_at: Optional[datetime] = None

    status: Literal["wake_in_progress", "queued", "running", "succeeded", "failed", "cancelled", "expired"]

    stderr_bytes: Optional[int] = None

    stderr_truncated: Optional[bool] = None

    stdout_bytes: Optional[int] = None

    stdout_truncated: Optional[bool] = None
