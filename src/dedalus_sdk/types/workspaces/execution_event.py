# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ExecutionEvent"]


class ExecutionEvent(BaseModel):
    at: datetime

    sequence: int

    type: Literal["lifecycle", "stdout", "stderr"]

    chunk: Optional[str] = None

    error_code: Optional[str] = None

    error_message: Optional[str] = None

    exit_code: Optional[int] = None

    signal: Optional[int] = None

    status: Optional[
        Literal["wake_in_progress", "queued", "running", "succeeded", "failed", "cancelled", "expired"]
    ] = None
