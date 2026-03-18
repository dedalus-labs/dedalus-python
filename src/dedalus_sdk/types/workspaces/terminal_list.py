# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .terminal import Terminal
from ..._models import BaseModel

__all__ = ["TerminalList"]


class TerminalList(BaseModel):
    items: Optional[List[Terminal]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    next_cursor: Optional[str] = None
