# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .artifact_ref import ArtifactRef

__all__ = ["Execution"]


class Execution(BaseModel):
    command: Optional[List[str]] = None

    created_at: datetime

    execution_id: str

    status: Literal["wake_in_progress", "queued", "running", "succeeded", "failed", "cancelled", "expired"]

    workspace_id: str

    artifacts: Optional[List[ArtifactRef]] = None

    completed_at: Optional[datetime] = None

    cwd: Optional[str] = None

    env_keys: Optional[List[str]] = None

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    exit_code: Optional[int] = None

    expires_at: Optional[datetime] = None

    retry_after_ms: Optional[int] = None

    signal: Optional[int] = None

    started_at: Optional[datetime] = None

    stderr_bytes: Optional[int] = None

    stderr_truncated: Optional[bool] = None

    stdout_bytes: Optional[int] = None

    stdout_truncated: Optional[bool] = None
