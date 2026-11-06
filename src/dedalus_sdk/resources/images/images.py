# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

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
from ..._base_client import make_request_options
from .uploads import (
    UploadsResource,
    AsyncUploadsResource,
    UploadsResourceWithRawResponse,
    AsyncUploadsResourceWithRawResponse,
    UploadsResourceWithStreamingResponse,
    AsyncUploadsResourceWithStreamingResponse,
)
from ...types.image_list import ImageList
from ...types import image_list_params, image_create_params, image_update_params
from ...types.image import Image
from ...types.source_param import SourceParam

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def uploads(self) -> UploadsResource:
        return UploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageList:
        """
        Pages through the organization's images in ID order. A deleted image is left out; it still reads by ID.

        Args:
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageList: OK

        Example:
            ```python
            image = client.images.list(
                limit=100,
            )
            ```
        """
        return self._get(
            "/v1/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, image_list_params.ImageListParams),
            ),
            cast_to=ImageList,
        )

    def create(
        self,
        *,
        credential_ref: str | Omit = omit,
        name: str | Omit = omit,
        platform: Literal["linux/amd64", "linux/arm64"],
        source: SourceParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Image:
        """
        Requires an entitled organization and linux/amd64 on the current fleet. Acceptance queues preparation; only a ready image can launch a machine. Private registry credentials are not yet supported.

        Args:
            credential_ref: Body parameter.
            name: A label people use to tell images apart. Programs use the image ID.
            platform: Body parameter.
            source: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Image: Accepted

        Example:
            ```python
            image = client.images.create(
                platform="linux/amd64",
                source={"kind": ""},
                idempotency_key="",
            )
            ```
        """
        return self._post(
            "/v1/images",
            body=maybe_transform(
                {
                    "credential_ref": credential_ref,
                    "name": name,
                    "platform": platform,
                    "source": source,
                },
                image_create_params.ImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Image,
        )

    def retrieve(
        self,
        *,
        image_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Image:
        """
        A preparing image reports its stage, the worker's last step and an estimated percent of the whole preparation. A failed image names the cause: IMAGE_OS_UNSUPPORTED, IMAGE_SOURCE_INVALID, IMAGE_SOURCE_NOT_FOUND and IMAGE_SOURCE_UNAUTHORIZED describe the image or its reference and are final; IMAGE_SOURCE_UNAVAILABLE, IMAGE_REGISTRY_UNREACHABLE, IMAGE_REGISTRY_RATE_LIMITED, IMAGE_ARCHIVE_UNAVAILABLE and IMAGE_EXECUTION_FAILED describe this attempt and are retryable with a new idempotency key.

        Args:
            image_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Image: OK

        Example:
            ```python
            image = client.images.retrieve(
                image_id="imageID",
            )
            ```
        """
        if image_id is None or (isinstance(image_id, str) and not image_id):
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._get(
            path_template("/v1/images/{image_id}", **{"image_id": image_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Image,
        )

    def update(
        self,
        *,
        image_id: str,
        name: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Image:
        """
        Changes only the name. The image's source, platform and state are immutable.

        Args:
            image_id: Path parameter.
            name: The new label, or null to clear it. No other field can change.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Image: OK

        Example:
            ```python
            image = client.images.update(
                image_id="imageID",
                name="",
                idempotency_key="",
            )
            ```
        """
        if image_id is None or (isinstance(image_id, str) and not image_id):
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._patch(
            path_template("/v1/images/{image_id}", **{"image_id": image_id}),
            body=maybe_transform(
                {"name": name},
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Image,
        )

    def delete(
        self,
        *,
        image_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Image:
        """
        The image can create no new Machine and no longer counts against the organization's image limit. Machines already running from it keep working. The image stays readable, and deleting it again returns the same image.

        Args:
            image_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Image: OK

        Example:
            ```python
            image = client.images.delete(
                image_id="imageID",
                idempotency_key="",
            )
            ```
        """
        if image_id is None or (isinstance(image_id, str) and not image_id):
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return self._delete(
            path_template("/v1/images/{image_id}", **{"image_id": image_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Image,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def uploads(self) -> AsyncUploadsResource:
        return AsyncUploadsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ImageList:
        """
        Pages through the organization's images in ID order. A deleted image is left out; it still reads by ID.

        Args:
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ImageList: OK

        Example:
            ```python
            image = await client.images.list(
                limit=100,
            )
            ```
        """
        return await self._get(
            "/v1/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"limit": limit, "cursor": cursor}, image_list_params.ImageListParams
                ),
            ),
            cast_to=ImageList,
        )

    async def create(
        self,
        *,
        credential_ref: str | Omit = omit,
        name: str | Omit = omit,
        platform: Literal["linux/amd64", "linux/arm64"],
        source: SourceParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Image:
        """
        Requires an entitled organization and linux/amd64 on the current fleet. Acceptance queues preparation; only a ready image can launch a machine. Private registry credentials are not yet supported.

        Args:
            credential_ref: Body parameter.
            name: A label people use to tell images apart. Programs use the image ID.
            platform: Body parameter.
            source: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Image: Accepted

        Example:
            ```python
            image = await client.images.create(
                platform="linux/amd64",
                source={"kind": ""},
                idempotency_key="",
            )
            ```
        """
        return await self._post(
            "/v1/images",
            body=await async_maybe_transform(
                {
                    "credential_ref": credential_ref,
                    "name": name,
                    "platform": platform,
                    "source": source,
                },
                image_create_params.ImageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Image,
        )

    async def retrieve(
        self,
        *,
        image_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Image:
        """
        A preparing image reports its stage, the worker's last step and an estimated percent of the whole preparation. A failed image names the cause: IMAGE_OS_UNSUPPORTED, IMAGE_SOURCE_INVALID, IMAGE_SOURCE_NOT_FOUND and IMAGE_SOURCE_UNAUTHORIZED describe the image or its reference and are final; IMAGE_SOURCE_UNAVAILABLE, IMAGE_REGISTRY_UNREACHABLE, IMAGE_REGISTRY_RATE_LIMITED, IMAGE_ARCHIVE_UNAVAILABLE and IMAGE_EXECUTION_FAILED describe this attempt and are retryable with a new idempotency key.

        Args:
            image_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Image: OK

        Example:
            ```python
            image = await client.images.retrieve(
                image_id="imageID",
            )
            ```
        """
        if image_id is None or (isinstance(image_id, str) and not image_id):
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._get(
            path_template("/v1/images/{image_id}", **{"image_id": image_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Image,
        )

    async def update(
        self,
        *,
        image_id: str,
        name: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Image:
        """
        Changes only the name. The image's source, platform and state are immutable.

        Args:
            image_id: Path parameter.
            name: The new label, or null to clear it. No other field can change.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Image: OK

        Example:
            ```python
            image = await client.images.update(
                image_id="imageID",
                name="",
                idempotency_key="",
            )
            ```
        """
        if image_id is None or (isinstance(image_id, str) and not image_id):
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._patch(
            path_template("/v1/images/{image_id}", **{"image_id": image_id}),
            body=await async_maybe_transform(
                {"name": name},
                image_update_params.ImageUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Image,
        )

    async def delete(
        self,
        *,
        image_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Image:
        """
        The image can create no new Machine and no longer counts against the organization's image limit. Machines already running from it keep working. The image stays readable, and deleting it again returns the same image.

        Args:
            image_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Image: OK

        Example:
            ```python
            image = await client.images.delete(
                image_id="imageID",
                idempotency_key="",
            )
            ```
        """
        if image_id is None or (isinstance(image_id, str) and not image_id):
            raise ValueError(f"Expected a non-empty value for `image_id` but received {image_id!r}")
        return await self._delete(
            path_template("/v1/images/{image_id}", **{"image_id": image_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Image,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_raw_response_wrapper(
            images.list,
        )
        self.create = to_raw_response_wrapper(
            images.create,
        )
        self.retrieve = to_raw_response_wrapper(
            images.retrieve,
        )
        self.update = to_raw_response_wrapper(
            images.update,
        )
        self.delete = to_raw_response_wrapper(
            images.delete,
        )

    @cached_property
    def uploads(self) -> UploadsResourceWithRawResponse:
        return UploadsResourceWithRawResponse(self._images.uploads)


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.list = async_to_raw_response_wrapper(
            images.list,
        )
        self.create = async_to_raw_response_wrapper(
            images.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            images.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            images.update,
        )
        self.delete = async_to_raw_response_wrapper(
            images.delete,
        )

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithRawResponse:
        return AsyncUploadsResourceWithRawResponse(self._images.uploads)


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_streamed_response_wrapper(
            images.list,
        )
        self.create = to_streamed_response_wrapper(
            images.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            images.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            images.update,
        )
        self.delete = to_streamed_response_wrapper(
            images.delete,
        )

    @cached_property
    def uploads(self) -> UploadsResourceWithStreamingResponse:
        return UploadsResourceWithStreamingResponse(self._images.uploads)


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
        self.create = async_to_streamed_response_wrapper(
            images.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            images.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            images.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            images.delete,
        )

    @cached_property
    def uploads(self) -> AsyncUploadsResourceWithStreamingResponse:
        return AsyncUploadsResourceWithStreamingResponse(self._images.uploads)
