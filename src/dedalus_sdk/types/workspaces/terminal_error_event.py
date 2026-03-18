# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TerminalErrorEvent"]


class TerminalErrorEvent(BaseModel):
    type: Literal["error"]

    error_code: Optional[str] = None

    error_message: Optional[str] = None
