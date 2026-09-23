# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TerminalErrorEvent"]


class TerminalErrorEvent(BaseModel):
    error_code: Optional[str] = None

    error_message: Optional[str] = None

    type: Literal["error"]
