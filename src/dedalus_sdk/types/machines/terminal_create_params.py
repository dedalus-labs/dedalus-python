# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TerminalCreateParams"]


class TerminalCreateParams(TypedDict, total=False):
    machine_id: Required[str]

    cwd: str

    env: Dict[str, str]

    height: Required[int]

    shell: str

    width: Required[int]

    x_dedalus_org_id: Annotated[str, PropertyInfo(alias="X-Dedalus-Org-Id")]
