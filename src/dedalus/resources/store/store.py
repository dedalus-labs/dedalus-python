# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.store_list_inventory_response import StoreListInventoryResponse

__all__ = ["StoreResource", "AsyncStoreResource"]


class StoreResource(SyncAPIResource):
    """Access to Petstore orders"""

    @cached_property
    def orders(self) -> OrdersResource:
        """Access to Petstore orders"""
        return OrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> StoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return StoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#with_streaming_response
        """
        return StoreResourceWithStreamingResponse(self)

    def list_inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreListInventoryResponse:
        """Returns a map of status codes to quantities"""
        return self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreListInventoryResponse,
        )


class AsyncStoreResource(AsyncAPIResource):
    """Access to Petstore orders"""

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        """Access to Petstore orders"""
        return AsyncOrdersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#with_streaming_response
        """
        return AsyncStoreResourceWithStreamingResponse(self)

    async def list_inventory(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StoreListInventoryResponse:
        """Returns a map of status codes to quantities"""
        return await self._get(
            "/store/inventory",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StoreListInventoryResponse,
        )


class StoreResourceWithRawResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

        self.list_inventory = to_raw_response_wrapper(
            store.list_inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        """Access to Petstore orders"""
        return OrdersResourceWithRawResponse(self._store.orders)


class AsyncStoreResourceWithRawResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

        self.list_inventory = async_to_raw_response_wrapper(
            store.list_inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        """Access to Petstore orders"""
        return AsyncOrdersResourceWithRawResponse(self._store.orders)


class StoreResourceWithStreamingResponse:
    def __init__(self, store: StoreResource) -> None:
        self._store = store

        self.list_inventory = to_streamed_response_wrapper(
            store.list_inventory,
        )

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        """Access to Petstore orders"""
        return OrdersResourceWithStreamingResponse(self._store.orders)


class AsyncStoreResourceWithStreamingResponse:
    def __init__(self, store: AsyncStoreResource) -> None:
        self._store = store

        self.list_inventory = async_to_streamed_response_wrapper(
            store.list_inventory,
        )

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        """Access to Petstore orders"""
        return AsyncOrdersResourceWithStreamingResponse(self._store.orders)
