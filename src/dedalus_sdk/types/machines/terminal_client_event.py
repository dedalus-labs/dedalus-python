# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .terminal_input_event import TerminalInputEvent
from .terminal_resize_event import TerminalResizeEvent

__all__ = ["TerminalClientEvent"]

TerminalClientEvent: TypeAlias = Annotated[
    Union[TerminalInputEvent, TerminalResizeEvent], PropertyInfo(discriminator="type")
]
