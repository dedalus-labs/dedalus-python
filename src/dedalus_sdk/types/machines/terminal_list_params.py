# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TerminalListParams"]


class TerminalListParams(TypedDict, total=False):
    machine_id: Required[str]

    limit: int

    cursor: str

    x_dedalus_org_id: Annotated[str, PropertyInfo(alias="X-Dedalus-Org-Id")]
