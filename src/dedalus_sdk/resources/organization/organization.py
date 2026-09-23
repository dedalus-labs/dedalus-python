# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .autoresizing import (
    AutoresizingResource,
    AsyncAutoresizingResource,
    AutoresizingResourceWithRawResponse,
    AsyncAutoresizingResourceWithRawResponse,
    AutoresizingResourceWithStreamingResponse,
    AsyncAutoresizingResourceWithStreamingResponse,
)

__all__ = ["OrganizationResource", "AsyncOrganizationResource"]


class OrganizationResource(SyncAPIResource):
    @cached_property
    def autoresizing(self) -> AutoresizingResource:
        return AutoresizingResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationResourceWithRawResponse:
        return OrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationResourceWithStreamingResponse:
        return OrganizationResourceWithStreamingResponse(self)


class AsyncOrganizationResource(AsyncAPIResource):
    @cached_property
    def autoresizing(self) -> AsyncAutoresizingResource:
        return AsyncAutoresizingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationResourceWithRawResponse:
        return AsyncOrganizationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationResourceWithStreamingResponse:
        return AsyncOrganizationResourceWithStreamingResponse(self)


class OrganizationResourceWithRawResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def autoresizing(self) -> AutoresizingResourceWithRawResponse:
        return AutoresizingResourceWithRawResponse(self._organization.autoresizing)


class AsyncOrganizationResourceWithRawResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def autoresizing(self) -> AsyncAutoresizingResourceWithRawResponse:
        return AsyncAutoresizingResourceWithRawResponse(self._organization.autoresizing)


class OrganizationResourceWithStreamingResponse:
    def __init__(self, organization: OrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def autoresizing(self) -> AutoresizingResourceWithStreamingResponse:
        return AutoresizingResourceWithStreamingResponse(self._organization.autoresizing)


class AsyncOrganizationResourceWithStreamingResponse:
    def __init__(self, organization: AsyncOrganizationResource) -> None:
        self._organization = organization

    @cached_property
    def autoresizing(self) -> AsyncAutoresizingResourceWithStreamingResponse:
        return AsyncAutoresizingResourceWithStreamingResponse(self._organization.autoresizing)
