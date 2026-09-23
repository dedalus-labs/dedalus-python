# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UsageMachineComputeParams"]


class UsageMachineComputeParams(TypedDict, total=False):
    period_start: str
    """Usage period start (YYYY-MM-DD). Defaults to first of current month."""

    period_end: str
    """Last UTC usage date to include (YYYY-MM-DD). Defaults to current time."""

    machine_id: str
    """Optional machine ID filter."""

    granularity: str
    """Usage breakdown granularity: hour or day. Defaults to hour."""
