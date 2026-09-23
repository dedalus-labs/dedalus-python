# File generated from our OpenAPI spec by Scalar. See README.md for details.

from ..._models import BaseModel

__all__ = ["Policy"]


class Policy(BaseModel):
    enabled: bool
    """Allow automatic RAM increases for all organization machines. Disabling preserves applied RAM and already admitted resizes."""
