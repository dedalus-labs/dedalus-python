# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UsageMachineStorageParams"]


class UsageMachineStorageParams(TypedDict, total=False):
    machine_id: str
    """Optional machine ID filter."""

    period_end: str
    """Last UTC usage date to include (YYYY-MM-DD). Defaults to current time."""

    period_start: str
    """Usage period start (YYYY-MM-DD). Defaults to first of current month."""
