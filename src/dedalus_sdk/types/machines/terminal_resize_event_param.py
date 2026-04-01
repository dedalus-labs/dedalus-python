# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TerminalResizeEventParam"]


class TerminalResizeEventParam(TypedDict, total=False):
    height: Required[int]

    type: Required[Literal["resize"]]

    width: Required[int]
