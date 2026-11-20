# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

from .image import Image

__all__ = ["ImageList"]


class ImageList(BaseModel):
    items: Optional[List[Image]] = None

    next_cursor: Optional[str] = None
