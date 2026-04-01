# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExecutionOutput"]


class ExecutionOutput(BaseModel):
    execution_id: str

    stderr: Optional[str] = None

    stderr_bytes: Optional[int] = None

    stderr_truncated: Optional[bool] = None

    stdout: Optional[str] = None

    stdout_bytes: Optional[int] = None

    stdout_truncated: Optional[bool] = None
