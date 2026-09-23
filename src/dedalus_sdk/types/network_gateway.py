# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NetworkGateway"]


class NetworkGateway(BaseModel):
    hostname: str

    kind: Literal["ssh", "port"]

    port: Optional[int] = None

    protocol: Literal["ssh", "https"]
