# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .preview import Preview
from ..._models import BaseModel

__all__ = ["PreviewList"]


class PreviewList(BaseModel):
    items: Optional[List[Preview]] = None

    next_cursor: Optional[str] = None
