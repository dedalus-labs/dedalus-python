# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

__all__ = ["ConnectClientEventParam", "WebSocketEvent"]


class WebSocketEvent(TypedDict, total=False):
    pass


ConnectClientEventParam: TypeAlias = Union[WebSocketEvent]
