# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SourceParam"]


class SourceParam(TypedDict, total=False):
    kind: Required[str]

    reference: str

    sha256: str

    upload_id: str
