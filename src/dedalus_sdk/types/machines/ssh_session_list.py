# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .ssh_session import SSHSession

__all__ = ["SSHSessionList"]


class SSHSessionList(BaseModel):
    items: Optional[List[SSHSession]] = None

    next_cursor: Optional[str] = None
