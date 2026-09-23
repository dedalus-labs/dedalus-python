# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TerminalOutputEvent"]


class TerminalOutputEvent(BaseModel):
    data: str
    """Base64-encoded terminal output."""

    type: Literal["output"]
