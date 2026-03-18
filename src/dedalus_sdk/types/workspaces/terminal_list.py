# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .terminal import Terminal
from ..._models import BaseModel

__all__ = ["TerminalList"]


class TerminalList(BaseModel):
    items: Optional[List[Terminal]] = None

    next_cursor: Optional[str] = None
