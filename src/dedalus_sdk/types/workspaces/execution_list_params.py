# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ExecutionListParams"]


class ExecutionListParams(TypedDict, total=False):
    cursor: str

    limit: int
