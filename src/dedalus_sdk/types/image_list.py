# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ImageList"]


class ImageList(BaseModel):
    image_ids: Optional[List[str]] = None

    next_cursor: Optional[str] = None
