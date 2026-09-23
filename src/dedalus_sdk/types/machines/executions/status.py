# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Status", "Capture", "Publication"]


class Publication(BaseModel):
    code: Optional[str] = None

    complete: bool

    queued_messages: int

    state: Literal["active", "finishing", "failed", "closed"]


class Capture(BaseModel):
    code: Optional[str] = None

    lost_bytes: Optional[str] = None

    state: Optional[Literal["pending", "incomplete", "unavailable"]] = None

    unconfirmed_bytes: Optional[str] = None


class Status(BaseModel):
    capture: Capture

    code: Optional[str] = None

    execution_id: str

    publication: Optional[Publication] = None

    stream_id: Optional[str] = None
