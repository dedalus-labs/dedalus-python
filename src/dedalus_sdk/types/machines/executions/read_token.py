# File generated from our OpenAPI spec by Scalar. See README.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ReadToken"]


class ReadToken(BaseModel):
    access_token: str

    base_url: str

    execution_id: str

    expires_at: datetime

    stream_id: str

    token_type: str
