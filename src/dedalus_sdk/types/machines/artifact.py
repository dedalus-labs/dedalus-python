# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Artifact"]


class Artifact(BaseModel):
    artifact_id: str

    created_at: datetime

    machine_id: str

    name: str

    size_bytes: int

    download_url: Optional[str] = None

    execution_id: Optional[str] = None

    expires_at: Optional[datetime] = None

    mime_type: Optional[str] = None

    sha256: Optional[str] = None
