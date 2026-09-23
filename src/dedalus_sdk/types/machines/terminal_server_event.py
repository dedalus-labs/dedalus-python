# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo

from .terminal_output_event import TerminalOutputEvent
from .terminal_error_event import TerminalErrorEvent
from .terminal_closed_event import TerminalClosedEvent

__all__ = ["TerminalServerEvent"]

TerminalServerEvent: TypeAlias = Annotated[
    Union[TerminalOutputEvent, TerminalErrorEvent, TerminalClosedEvent], PropertyInfo(discriminator="type")
]
