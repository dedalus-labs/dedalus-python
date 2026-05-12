# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["OrgUsage"]


class OrgUsage(BaseModel):
    billed_awake_seconds: int
    """Closed awake seconds in billed org buckets for the period."""

    billed_cpu_millicore_seconds: int
    """
    Closed requested vCPU millicores multiplied by active CPU seconds for the
    period.
    """

    billed_logical_storage_mib_seconds: int
    """
    Closed billable logical MiB-seconds for the period, matching the Stripe storage
    meter.
    """

    billed_memory_mib_seconds: int
    """Closed requested memory MiB multiplied by awake seconds for the period."""

    included_storage_gib: int
    """Plan-included storage in GiB, used as a local guardrail only."""

    plan_slug: str
    """Billing plan in effect for the organization."""

    provisioned_storage_gib: int
    """Current provisioned storage summed across machines in GiB."""
