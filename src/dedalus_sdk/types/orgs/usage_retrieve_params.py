# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UsageRetrieveParams"]


class UsageRetrieveParams(TypedDict, total=False):
    org_id: Required[str]

    period_start: str
    """Billing period start (YYYY-MM-DD). Defaults to first of current month."""
