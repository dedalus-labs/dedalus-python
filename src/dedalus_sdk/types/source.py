# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Source"]


class Source(BaseModel):
    kind: str

    reference: Optional[str] = None

    sha256: Optional[str] = None

    upload_id: Optional[str] = None
