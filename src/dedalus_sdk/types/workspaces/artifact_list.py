# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .artifact import Artifact
from ..._models import BaseModel

__all__ = ["ArtifactList"]


class ArtifactList(BaseModel):
    items: Optional[List[Artifact]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    next_cursor: Optional[str] = None
