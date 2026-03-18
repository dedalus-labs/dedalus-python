# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .ssh_session import SSHSession

__all__ = ["SSHSessionList"]


class SSHSessionList(BaseModel):
    items: Optional[List[SSHSession]] = None

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""

    next_cursor: Optional[str] = None
