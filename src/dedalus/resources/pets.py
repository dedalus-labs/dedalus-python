# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    pet_create_params,
    pet_update_params,
    pet_find_by_tags_params,
    pet_update_by_id_params,
    pet_upload_image_params,
    pet_find_by_status_params,
)
from .._files import read_file_content, async_read_file_content
from .._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    BinaryTypes,
    FileContent,
    SequenceNotStr,
    AsyncBinaryTypes,
    omit,
    not_given,
)
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.pet import Pet
from .._base_client import make_request_options
from ..types.category_param import CategoryParam
from ..types.pet_find_by_tags_response import PetFindByTagsResponse
from ..types.pet_upload_image_response import PetUploadImageResponse
from ..types.pet_find_by_status_response import PetFindByStatusResponse

__all__ = ["PetsResource", "AsyncPetsResource"]


class PetsResource(SyncAPIResource):
    """Everything about your Pets"""

    @cached_property
    def with_raw_response(self) -> PetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return PetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#with_streaming_response
        """
        return PetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        photo_urls: SequenceNotStr[str],
        id: int | Omit = omit,
        category: CategoryParam | Omit = omit,
        status: Literal["available", "pending", "sold"] | Omit = omit,
        tags: Iterable[pet_create_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pet:
        """
        Add a new pet to the store

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pet",
            body=maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_create_params.PetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def retrieve(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pet:
        """
        Returns a single pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def update(
        self,
        *,
        name: str,
        photo_urls: SequenceNotStr[str],
        id: int | Omit = omit,
        category: CategoryParam | Omit = omit,
        status: Literal["available", "pending", "sold"] | Omit = omit,
        tags: Iterable[pet_update_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pet:
        """
        Update an existing pet by Id

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/pet",
            body=maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_update_params.PetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    def delete(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        delete a pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def find_by_status(
        self,
        *,
        status: Literal["available", "pending", "sold"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PetFindByStatusResponse:
        """
        Multiple status values can be provided with comma separated strings

        Args:
          status: Status values that need to be considered for filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pet/findByStatus",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, pet_find_by_status_params.PetFindByStatusParams),
            ),
            cast_to=PetFindByStatusResponse,
        )

    def find_by_tags(
        self,
        *,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PetFindByTagsResponse:
        """Multiple tags can be provided with comma separated strings.

        Use tag1, tag2, tag3
        for testing.

        Args:
          tags: Tags to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pet/findByTags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tags": tags}, pet_find_by_tags_params.PetFindByTagsParams),
            ),
            cast_to=PetFindByTagsResponse,
        )

    def update_by_id(
        self,
        pet_id: int,
        *,
        name: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates a pet in the store with form data

        Args:
          name: Name of pet that needs to be updated

          status: Status of pet that needs to be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "status": status,
                    },
                    pet_update_by_id_params.PetUpdateByIDParams,
                ),
            ),
            cast_to=NoneType,
        )

    def upload_image(
        self,
        pet_id: int,
        image: FileContent | BinaryTypes,
        *,
        additional_metadata: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PetUploadImageResponse:
        """
        uploads an image

        Args:
          additional_metadata: Additional Metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            f"/pet/{pet_id}/uploadImage",
            content=read_file_content(image) if isinstance(image, os.PathLike) else image,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"additional_metadata": additional_metadata}, pet_upload_image_params.PetUploadImageParams
                ),
            ),
            cast_to=PetUploadImageResponse,
        )


class AsyncPetsResource(AsyncAPIResource):
    """Everything about your Pets"""

    @cached_property
    def with_raw_response(self) -> AsyncPetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/dedalus-python#with_streaming_response
        """
        return AsyncPetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        photo_urls: SequenceNotStr[str],
        id: int | Omit = omit,
        category: CategoryParam | Omit = omit,
        status: Literal["available", "pending", "sold"] | Omit = omit,
        tags: Iterable[pet_create_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pet:
        """
        Add a new pet to the store

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pet",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_create_params.PetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def retrieve(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pet:
        """
        Returns a single pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def update(
        self,
        *,
        name: str,
        photo_urls: SequenceNotStr[str],
        id: int | Omit = omit,
        category: CategoryParam | Omit = omit,
        status: Literal["available", "pending", "sold"] | Omit = omit,
        tags: Iterable[pet_update_params.Tag] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pet:
        """
        Update an existing pet by Id

        Args:
          status: pet status in the store

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/pet",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "photo_urls": photo_urls,
                    "id": id,
                    "category": category,
                    "status": status,
                    "tags": tags,
                },
                pet_update_params.PetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pet,
        )

    async def delete(
        self,
        pet_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        delete a pet

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def find_by_status(
        self,
        *,
        status: Literal["available", "pending", "sold"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PetFindByStatusResponse:
        """
        Multiple status values can be provided with comma separated strings

        Args:
          status: Status values that need to be considered for filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pet/findByStatus",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"status": status}, pet_find_by_status_params.PetFindByStatusParams),
            ),
            cast_to=PetFindByStatusResponse,
        )

    async def find_by_tags(
        self,
        *,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PetFindByTagsResponse:
        """Multiple tags can be provided with comma separated strings.

        Use tag1, tag2, tag3
        for testing.

        Args:
          tags: Tags to filter by

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pet/findByTags",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tags": tags}, pet_find_by_tags_params.PetFindByTagsParams),
            ),
            cast_to=PetFindByTagsResponse,
        )

    async def update_by_id(
        self,
        pet_id: int,
        *,
        name: str | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Updates a pet in the store with form data

        Args:
          name: Name of pet that needs to be updated

          status: Status of pet that needs to be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/pet/{pet_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "status": status,
                    },
                    pet_update_by_id_params.PetUpdateByIDParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def upload_image(
        self,
        pet_id: int,
        image: FileContent | AsyncBinaryTypes,
        *,
        additional_metadata: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PetUploadImageResponse:
        """
        uploads an image

        Args:
          additional_metadata: Additional Metadata

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            f"/pet/{pet_id}/uploadImage",
            content=await async_read_file_content(image) if isinstance(image, os.PathLike) else image,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"additional_metadata": additional_metadata}, pet_upload_image_params.PetUploadImageParams
                ),
            ),
            cast_to=PetUploadImageResponse,
        )


class PetsResourceWithRawResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

        self.create = to_raw_response_wrapper(
            pets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pets.update,
        )
        self.delete = to_raw_response_wrapper(
            pets.delete,
        )
        self.find_by_status = to_raw_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = to_raw_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = to_raw_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = to_raw_response_wrapper(
            pets.upload_image,
        )


class AsyncPetsResourceWithRawResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

        self.create = async_to_raw_response_wrapper(
            pets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pets.update,
        )
        self.delete = async_to_raw_response_wrapper(
            pets.delete,
        )
        self.find_by_status = async_to_raw_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = async_to_raw_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = async_to_raw_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = async_to_raw_response_wrapper(
            pets.upload_image,
        )


class PetsResourceWithStreamingResponse:
    def __init__(self, pets: PetsResource) -> None:
        self._pets = pets

        self.create = to_streamed_response_wrapper(
            pets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pets.update,
        )
        self.delete = to_streamed_response_wrapper(
            pets.delete,
        )
        self.find_by_status = to_streamed_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = to_streamed_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = to_streamed_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = to_streamed_response_wrapper(
            pets.upload_image,
        )


class AsyncPetsResourceWithStreamingResponse:
    def __init__(self, pets: AsyncPetsResource) -> None:
        self._pets = pets

        self.create = async_to_streamed_response_wrapper(
            pets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pets.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            pets.delete,
        )
        self.find_by_status = async_to_streamed_response_wrapper(
            pets.find_by_status,
        )
        self.find_by_tags = async_to_streamed_response_wrapper(
            pets.find_by_tags,
        )
        self.update_by_id = async_to_streamed_response_wrapper(
            pets.update_by_id,
        )
        self.upload_image = async_to_streamed_response_wrapper(
            pets.upload_image,
        )
