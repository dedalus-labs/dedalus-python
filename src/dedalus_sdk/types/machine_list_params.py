# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MachineListParams"]


class MachineListParams(TypedDict, total=False):
    limit: int

    cursor: str
