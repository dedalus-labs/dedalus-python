# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UsageRetrieveParams"]


class UsageRetrieveParams(TypedDict, total=False):
    period_start: str
    """Billing period start (YYYY-MM-DD). Defaults to first of current month."""
