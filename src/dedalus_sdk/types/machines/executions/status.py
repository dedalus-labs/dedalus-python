# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Status", "Capture"]


class Capture(BaseModel):
    code: Optional[str] = None

    lost_bytes: Optional[str] = None

    state: Optional[Literal["pending", "incomplete", "unavailable"]] = None

    unconfirmed_bytes: Optional[str] = None


class Status(BaseModel):
    capture: Capture

    execution_id: str

    stream_id: Optional[str] = None
