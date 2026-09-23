# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .terminal import Terminal

__all__ = ["TerminalList"]


class TerminalList(BaseModel):
    items: Optional[List[Terminal]] = None

    next_cursor: Optional[str] = None
