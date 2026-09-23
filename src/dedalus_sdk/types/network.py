# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import List, Optional

from .._models import BaseModel

from .network_gateway import NetworkGateway

__all__ = ["Network"]


class Network(BaseModel):
    gateways: Optional[List[NetworkGateway]] = None

    name: str

    network_id: str
