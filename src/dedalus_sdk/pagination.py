# File generated from our OpenAPI spec by Scalar. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override


from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage
from ._models import construct_type

__all__ = ["SyncCursorPage", "AsyncCursorPage"]

_T = TypeVar("_T")


def _has_next_cursor(cursor: object) -> bool:
    """Return True for non-empty string cursors and finite numeric cursor IDs like 0."""
    import math

    if isinstance(cursor, bool):
        return False
    if isinstance(cursor, str):
        return cursor != ""
    if isinstance(cursor, (int, float)):
        return math.isfinite(cursor)
    return False


class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        # The item model is attached by the response post-parser after the page is parsed.
        return [cast(_T, construct_type(value=item, type_=self._model)) for item in items]

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.next_cursor
        if not _has_next_cursor(cursor):
            return None

        return PageInfo(params={"cursor": cursor})


class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_cursor: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        # The item model is attached by the response post-parser after the page is parsed.
        return [cast(_T, construct_type(value=item, type_=self._model)) for item in items]

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        cursor = self.next_cursor
        if not _has_next_cursor(cursor):
            return None

        return PageInfo(params={"cursor": cursor})
