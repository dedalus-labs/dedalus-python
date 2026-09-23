# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from ..._models import BaseModel

from .artifact import Artifact

__all__ = ["ArtifactList"]


class ArtifactList(BaseModel):
    items: Optional[List[Artifact]] = None

    next_cursor: Optional[str] = None
