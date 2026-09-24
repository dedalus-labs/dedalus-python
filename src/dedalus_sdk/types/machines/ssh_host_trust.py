# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSHHostTrust"]


class SSHHostTrust(BaseModel):
    host_pattern: str

    kind: Literal["cert_authority"]

    public_key: str
