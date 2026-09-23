# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["MachineNetwork"]


class MachineNetwork(BaseModel):
    hostname: str

    machine_id: str

    network_id: str

    network_name: str

    private_ipv4: str

    private_ipv6: str
