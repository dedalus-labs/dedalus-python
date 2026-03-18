# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExecutionOutput"]


class ExecutionOutput(BaseModel):
    execution_id: str

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    stderr: Optional[str] = None

    stderr_bytes: Optional[int] = None

    stderr_truncated: Optional[bool] = None

    stdout: Optional[str] = None

    stdout_bytes: Optional[int] = None

    stdout_truncated: Optional[bool] = None
