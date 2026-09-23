# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .port import Port

__all__ = ["PortList"]


class PortList(BaseModel):
    items: Optional[List[Port]] = None

    next_cursor: Optional[str] = None
