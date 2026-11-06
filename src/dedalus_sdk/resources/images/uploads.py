# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.images.reservation import Reservation
from ...types.images import upload_create_params

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        return UploadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        platform: str,
        sha256: str,
        size_bytes: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Reservation:
        """
        Reserve an immutable Docker image archive upload

        Args:
            platform: Body parameter.
            sha256: Body parameter.
            size_bytes: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Reservation: OK

        Example:
            ```python
            upload = client.images.uploads.create(
                platform="",
                sha256="",
                size_bytes=0,
                idempotency_key="",
            )
            ```
        """
        return self._post(
            "/v1/images/uploads",
            body=maybe_transform(
                {
                    "platform": platform,
                    "sha256": sha256,
                    "size_bytes": size_bytes,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Reservation,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        platform: str,
        sha256: str,
        size_bytes: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Reservation:
        """
        Reserve an immutable Docker image archive upload

        Args:
            platform: Body parameter.
            sha256: Body parameter.
            size_bytes: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Reservation: OK

        Example:
            ```python
            upload = await client.images.uploads.create(
                platform="",
                sha256="",
                size_bytes=0,
                idempotency_key="",
            )
            ```
        """
        return await self._post(
            "/v1/images/uploads",
            body=await async_maybe_transform(
                {
                    "platform": platform,
                    "sha256": sha256,
                    "size_bytes": size_bytes,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Reservation,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_raw_response_wrapper(
            uploads.create,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
