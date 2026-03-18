# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .execution import Execution

__all__ = ["ExecutionList"]


class ExecutionList(BaseModel):
    items: Optional[List[Execution]] = None

    next_cursor: Optional[str] = None
