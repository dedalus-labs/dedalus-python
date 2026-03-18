# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Artifact"]


class Artifact(BaseModel):
    artifact_id: str

    created_at: datetime

    name: str

    size_bytes: int

    workspace_id: str

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    download_url: Optional[str] = None

    execution_id: Optional[str] = None

    expires_at: Optional[datetime] = None

    mime_type: Optional[str] = None

    sha256: Optional[str] = None
