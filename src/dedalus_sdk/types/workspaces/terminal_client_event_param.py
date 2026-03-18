# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .terminal_input_event_param import TerminalInputEventParam
from .terminal_resize_event_param import TerminalResizeEventParam

__all__ = ["TerminalClientEventParam"]

TerminalClientEventParam: TypeAlias = Union[TerminalInputEventParam, TerminalResizeEventParam]
