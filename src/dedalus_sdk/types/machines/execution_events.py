# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .execution_event import ExecutionEvent

__all__ = ["ExecutionEvents"]


class ExecutionEvents(BaseModel):
    items: Optional[List[ExecutionEvent]] = None

    next_cursor: Optional[str] = None
