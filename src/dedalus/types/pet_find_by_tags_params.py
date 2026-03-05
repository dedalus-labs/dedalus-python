# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PetFindByTagsParams"]


class PetFindByTagsParams(TypedDict, total=False):
    tags: SequenceNotStr[str]
    """Tags to filter by"""
