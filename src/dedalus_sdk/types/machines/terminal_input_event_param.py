# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, Literal, Required, TypedDict
from ..._types import Base64FileInput

from ..._utils import PropertyInfo

__all__ = ["TerminalInputEventParam"]


class TerminalInputEventParam(TypedDict, total=False):
    data: Required[Annotated[Union[str, Base64FileInput], PropertyInfo(format="base64")]]
    """Base64-encoded terminal input."""

    type: Required[Literal["input"]]
