# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

from ..autoresizing_switch import AutoresizingSwitch

__all__ = ["Policy"]


class Policy(BaseModel):
    cpu: AutoresizingSwitch
    """Permit automatic CPU growth independently of RAM."""

    cpu_limit_source: Literal["plan", "configured", "platform"]

    cpu_max_vcpu: Optional[float] = None
    """Configured CPU growth limit in 0.25-vCPU steps. Null uses the plan limit."""

    effective_cpu_max_vcpu: float
    """Largest automatic CPU size allowed by this policy, plan and platform."""

    effective_memory_max_mib: int
    """Largest automatic RAM size allowed by this policy and plan, in MiB."""

    enabled: bool
    """Deprecated RAM permission alias. Use memory."""

    memory: AutoresizingSwitch
    """Permit automatic RAM growth. Automatic shrink remains internal."""

    memory_limit_source: Literal["plan", "configured", "platform"]

    memory_max_mib: Optional[int] = None
    """Configured RAM growth limit in MiB. Null uses the plan limit."""
