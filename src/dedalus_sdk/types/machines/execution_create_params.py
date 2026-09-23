# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, Required, TypedDict
from ..._types import SequenceNotStr

from ..._utils import PropertyInfo

__all__ = ["ExecutionCreateParams"]


class ExecutionCreateParams(TypedDict, total=False):
    machine_id: Required[str]

    command: Required[Optional[SequenceNotStr[str]]]

    cwd: str

    env: Dict[str, str]

    stdin: str

    timeout_ms: int

    x_dedalus_org_id: Annotated[str, PropertyInfo(alias="X-Dedalus-Org-Id")]
