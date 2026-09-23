# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Annotated, Required, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SSHCreateParams"]


class SSHCreateParams(TypedDict, total=False):
    machine_id: Required[str]

    public_key: Required[str]

    x_dedalus_org_id: Annotated[str, PropertyInfo(alias="X-Dedalus-Org-Id")]
