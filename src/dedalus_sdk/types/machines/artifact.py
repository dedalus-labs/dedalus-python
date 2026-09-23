# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Artifact"]


class Artifact(BaseModel):
    artifact_id: str

    created_at: datetime

    download_url: Optional[str] = None

    execution_id: Optional[str] = None

    expires_at: Optional[datetime] = None

    machine_id: str

    mime_type: Optional[str] = None

    name: str

    sha256: Optional[str] = None

    size_bytes: int
