# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExecutionEventsParams"]


class ExecutionEventsParams(TypedDict, total=False):
    machine_id: Required[str]

    execution_id: Required[str]

    cursor: str

    limit: int
