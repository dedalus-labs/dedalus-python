# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TerminalInputEvent"]


class TerminalInputEvent(BaseModel):
    data: str
    """Base64-encoded terminal input."""

    type: Literal["input"]
