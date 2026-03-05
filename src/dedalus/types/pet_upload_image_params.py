# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PetUploadImageParams"]


class PetUploadImageParams(TypedDict, total=False):
    additional_metadata: Annotated[str, PropertyInfo(alias="additionalMetadata")]
    """Additional Metadata"""
