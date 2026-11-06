# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

from ..source import Source

__all__ = ["Reservation", "Upload"]


class Upload(BaseModel):
    expires_at: datetime

    headers: Dict[str, Optional[List[str]]]

    method: str

    url: str


class Reservation(BaseModel):
    source: Source

    upload: Upload
