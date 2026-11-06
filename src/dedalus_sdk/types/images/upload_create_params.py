# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UploadCreateParams"]


class UploadCreateParams(TypedDict, total=False):
    platform: Required[str]

    sha256: Required[str]

    size_bytes: Required[int]
