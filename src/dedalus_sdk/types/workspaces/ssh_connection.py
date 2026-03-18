# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .ssh_host_trust import SSHHostTrust

__all__ = ["SSHConnection"]


class SSHConnection(BaseModel):
    endpoint: str

    port: int

    ssh_username: str

    host_trust: Optional[SSHHostTrust] = None

    user_certificate: Optional[str] = None
