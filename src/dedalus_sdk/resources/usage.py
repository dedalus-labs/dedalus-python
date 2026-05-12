# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import usage_retrieve_params, usage_machine_compute_params, usage_machine_storage_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.org_usage import OrgUsage
from ..types.machine_compute_usage import MachineComputeUsage
from ..types.machine_storage_usage import MachineStorageUsage

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgUsage:
        """Get usage summary

        Args:
          period_start: Billing period start (YYYY-MM-DD).

        Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period_start": period_start}, usage_retrieve_params.UsageRetrieveParams),
            ),
            cast_to=OrgUsage,
        )

    def machine_compute(
        self,
        *,
        granularity: str | Omit = omit,
        machine_id: str | Omit = omit,
        period_end: str | Omit = omit,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineComputeUsage:
        """
        List machine compute usage breakdown

        Args:
          granularity: Usage breakdown granularity: hour or day. Defaults to hour.

          machine_id: Optional machine ID filter.

          period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/usage/machines/compute",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "granularity": granularity,
                        "machine_id": machine_id,
                        "period_end": period_end,
                        "period_start": period_start,
                    },
                    usage_machine_compute_params.UsageMachineComputeParams,
                ),
            ),
            cast_to=MachineComputeUsage,
        )

    def machine_storage(
        self,
        *,
        machine_id: str | Omit = omit,
        period_end: str | Omit = omit,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineStorageUsage:
        """
        List machine storage usage breakdown

        Args:
          machine_id: Optional machine ID filter.

          period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/usage/machines/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "machine_id": machine_id,
                        "period_end": period_end,
                        "period_start": period_start,
                    },
                    usage_machine_storage_params.UsageMachineStorageParams,
                ),
            ),
            cast_to=MachineStorageUsage,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgUsage:
        """Get usage summary

        Args:
          period_start: Billing period start (YYYY-MM-DD).

        Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/usage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"period_start": period_start}, usage_retrieve_params.UsageRetrieveParams
                ),
            ),
            cast_to=OrgUsage,
        )

    async def machine_compute(
        self,
        *,
        granularity: str | Omit = omit,
        machine_id: str | Omit = omit,
        period_end: str | Omit = omit,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineComputeUsage:
        """
        List machine compute usage breakdown

        Args:
          granularity: Usage breakdown granularity: hour or day. Defaults to hour.

          machine_id: Optional machine ID filter.

          period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/usage/machines/compute",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "granularity": granularity,
                        "machine_id": machine_id,
                        "period_end": period_end,
                        "period_start": period_start,
                    },
                    usage_machine_compute_params.UsageMachineComputeParams,
                ),
            ),
            cast_to=MachineComputeUsage,
        )

    async def machine_storage(
        self,
        *,
        machine_id: str | Omit = omit,
        period_end: str | Omit = omit,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineStorageUsage:
        """
        List machine storage usage breakdown

        Args:
          machine_id: Optional machine ID filter.

          period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/usage/machines/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "machine_id": machine_id,
                        "period_end": period_end,
                        "period_start": period_start,
                    },
                    usage_machine_storage_params.UsageMachineStorageParams,
                ),
            ),
            cast_to=MachineStorageUsage,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = to_raw_response_wrapper(
            usage.retrieve,
        )
        self.machine_compute = to_raw_response_wrapper(
            usage.machine_compute,
        )
        self.machine_storage = to_raw_response_wrapper(
            usage.machine_storage,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = async_to_raw_response_wrapper(
            usage.retrieve,
        )
        self.machine_compute = async_to_raw_response_wrapper(
            usage.machine_compute,
        )
        self.machine_storage = async_to_raw_response_wrapper(
            usage.machine_storage,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = to_streamed_response_wrapper(
            usage.retrieve,
        )
        self.machine_compute = to_streamed_response_wrapper(
            usage.machine_compute,
        )
        self.machine_storage = to_streamed_response_wrapper(
            usage.machine_storage,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = async_to_streamed_response_wrapper(
            usage.retrieve,
        )
        self.machine_compute = async_to_streamed_response_wrapper(
            usage.machine_compute,
        )
        self.machine_storage = async_to_streamed_response_wrapper(
            usage.machine_storage,
        )
