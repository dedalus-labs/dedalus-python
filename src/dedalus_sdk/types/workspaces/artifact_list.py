# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .artifact import Artifact
from ..._models import BaseModel

__all__ = ["ArtifactList"]


class ArtifactList(BaseModel):
    items: Optional[List[Artifact]] = None

    next_cursor: Optional[str] = None
