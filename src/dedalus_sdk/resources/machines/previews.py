# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.machines import preview_list_params, preview_create_params
from ...types.machines.preview import Preview

__all__ = ["PreviewsResource", "AsyncPreviewsResource"]


class PreviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return PreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return PreviewsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        machine_id: str,
        port: int,
        protocol: Literal["http", "https"] | Omit = omit,
        visibility: Literal["public", "private", "org"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Preview:
        """
        Create preview

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._post(
            path_template("/v1/machines/{machine_id}/previews", machine_id=machine_id),
            body=maybe_transform(
                {
                    "port": port,
                    "protocol": protocol,
                    "visibility": visibility,
                },
                preview_create_params.PreviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Preview,
        )

    def retrieve(
        self,
        *,
        machine_id: str,
        preview_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Preview:
        """
        Get preview

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/previews/{preview_id}", machine_id=machine_id, preview_id=preview_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Preview,
        )

    def list(
        self,
        *,
        machine_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Preview]:
        """
        List previews

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/previews", machine_id=machine_id),
            page=SyncCursorPage[Preview],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    preview_list_params.PreviewListParams,
                ),
            ),
            model=Preview,
        )

    def delete(
        self,
        *,
        machine_id: str,
        preview_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Preview:
        """
        Delete preview

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/previews/{preview_id}", machine_id=machine_id, preview_id=preview_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Preview,
        )


class AsyncPreviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return AsyncPreviewsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        machine_id: str,
        port: int,
        protocol: Literal["http", "https"] | Omit = omit,
        visibility: Literal["public", "private", "org"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Preview:
        """
        Create preview

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._post(
            path_template("/v1/machines/{machine_id}/previews", machine_id=machine_id),
            body=await async_maybe_transform(
                {
                    "port": port,
                    "protocol": protocol,
                    "visibility": visibility,
                },
                preview_create_params.PreviewCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Preview,
        )

    async def retrieve(
        self,
        *,
        machine_id: str,
        preview_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Preview:
        """
        Get preview

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/previews/{preview_id}", machine_id=machine_id, preview_id=preview_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Preview,
        )

    def list(
        self,
        *,
        machine_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Preview, AsyncCursorPage[Preview]]:
        """
        List previews

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/previews", machine_id=machine_id),
            page=AsyncCursorPage[Preview],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    preview_list_params.PreviewListParams,
                ),
            ),
            model=Preview,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        preview_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Preview:
        """
        Delete preview

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not preview_id:
            raise ValueError(f"Expected a non-empty value for `preview_id` but received {preview_id!r}")
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/previews/{preview_id}", machine_id=machine_id, preview_id=preview_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Preview,
        )


class PreviewsResourceWithRawResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.create = to_raw_response_wrapper(
            previews.create,
        )
        self.retrieve = to_raw_response_wrapper(
            previews.retrieve,
        )
        self.list = to_raw_response_wrapper(
            previews.list,
        )
        self.delete = to_raw_response_wrapper(
            previews.delete,
        )


class AsyncPreviewsResourceWithRawResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.create = async_to_raw_response_wrapper(
            previews.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            previews.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            previews.list,
        )
        self.delete = async_to_raw_response_wrapper(
            previews.delete,
        )


class PreviewsResourceWithStreamingResponse:
    def __init__(self, previews: PreviewsResource) -> None:
        self._previews = previews

        self.create = to_streamed_response_wrapper(
            previews.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            previews.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            previews.list,
        )
        self.delete = to_streamed_response_wrapper(
            previews.delete,
        )


class AsyncPreviewsResourceWithStreamingResponse:
    def __init__(self, previews: AsyncPreviewsResource) -> None:
        self._previews = previews

        self.create = async_to_streamed_response_wrapper(
            previews.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            previews.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            previews.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            previews.delete,
        )
