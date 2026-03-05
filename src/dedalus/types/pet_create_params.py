# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .category_param import CategoryParam

__all__ = ["PetCreateParams", "Tag"]


class PetCreateParams(TypedDict, total=False):
    name: Required[str]

    photo_urls: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="photoUrls")]]

    id: int

    category: CategoryParam

    status: Literal["available", "pending", "sold"]
    """pet status in the store"""

    tags: Iterable[Tag]


class Tag(TypedDict, total=False):
    id: int

    name: str
