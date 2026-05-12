# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UsageGetMachineUsageParams"]


class UsageGetMachineUsageParams(TypedDict, total=False):
    org_id: Required[str]

    granularity: str
    """Evidence granularity: hour or day. Defaults to hour."""

    machine_id: str
    """Optional machine ID filter."""

    period_end: str
    """Last UTC evidence date to include (YYYY-MM-DD). Defaults to current time."""

    period_start: str
    """Evidence period start (YYYY-MM-DD). Defaults to first of current month."""
