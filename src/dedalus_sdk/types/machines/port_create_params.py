# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Literal, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PortCreateParams"]


class PortCreateParams(TypedDict, total=False):
    machine_id: Required[str]

    port: Required[int]

    protocol: Literal["http", "https"]

    x_dedalus_org_id: Annotated[str, PropertyInfo(alias="X-Dedalus-Org-Id")]
