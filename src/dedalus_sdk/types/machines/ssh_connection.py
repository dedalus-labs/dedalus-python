# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional

from ..._models import BaseModel

from .ssh_host_trust import SSHHostTrust

__all__ = ["SSHConnection"]


class SSHConnection(BaseModel):
    endpoint: str

    host_trust: Optional[SSHHostTrust] = None

    port: int

    ssh_username: str

    user_certificate: Optional[str] = None
