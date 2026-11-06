# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .source_param import SourceParam

__all__ = ["ImageCreateParams"]


class ImageCreateParams(TypedDict, total=False):
    credential_ref: str

    name: str
    """A label people use to tell images apart. Programs use the image ID."""

    platform: Required[Literal["linux/amd64", "linux/arm64"]]

    source: Required[SourceParam]
