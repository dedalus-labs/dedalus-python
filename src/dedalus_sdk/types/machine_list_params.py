# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MachineListParams"]


class MachineListParams(TypedDict, total=False):
    limit: int

    cursor: str

    x_dedalus_org_id: Annotated[str, PropertyInfo(alias="X-Dedalus-Org-Id")]
