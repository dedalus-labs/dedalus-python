# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PreviewCreateParams"]


class PreviewCreateParams(TypedDict, total=False):
    port: Required[int]

    protocol: Literal["http", "https"]

    wake_if_needed: bool
