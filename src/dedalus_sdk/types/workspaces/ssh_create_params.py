# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHCreateParams"]


class SSHCreateParams(TypedDict, total=False):
    public_key: Required[str]
