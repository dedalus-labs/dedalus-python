# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel

from .error import Error
from .source import Source

__all__ = ["Image", "Context", "ContextProgress"]


class ContextProgress(BaseModel):
    completed: int

    step: str

    total: int


class Context(BaseModel):
    percent: int

    progress: Optional[ContextProgress] = None

    stage: str


class Image(BaseModel):
    context: Optional[Context] = None

    created_at: datetime

    error: Optional[Error] = None

    image_id: str

    name: Optional[str] = None

    platform: str

    reason: Optional[str] = None

    source: Source

    state: str
