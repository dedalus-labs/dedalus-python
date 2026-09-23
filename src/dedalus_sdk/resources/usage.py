# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

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
from ..types import usage_retrieve_params, usage_machine_compute_params, usage_machine_storage_params
from ..types.machine_compute_usage import MachineComputeUsage
from ..types.machine_storage_usage import MachineStorageUsage

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
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
        """
        Get usage summary

        Args:
            period_start: Billing period start (YYYY-MM-DD). Defaults to first of current month.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrgUsage: OK

        Example:
            ```python
            usage = client.usage.retrieve()
            ```
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
        period_start: str | Omit = omit,
        period_end: str | Omit = omit,
        machine_id: str | Omit = omit,
        granularity: str | Omit = omit,
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
            period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.
            period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.
            machine_id: Optional machine ID filter.
            granularity: Usage breakdown granularity: hour or day. Defaults to hour.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineComputeUsage: OK

        Example:
            ```python
            usage = client.usage.machine_compute()
            ```
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
                        "period_start": period_start,
                        "period_end": period_end,
                        "machine_id": machine_id,
                        "granularity": granularity,
                    },
                    usage_machine_compute_params.UsageMachineComputeParams,
                ),
            ),
            cast_to=MachineComputeUsage,
        )

    def machine_storage(
        self,
        *,
        period_start: str | Omit = omit,
        period_end: str | Omit = omit,
        machine_id: str | Omit = omit,
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
            period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.
            period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.
            machine_id: Optional machine ID filter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineStorageUsage: OK

        Example:
            ```python
            usage = client.usage.machine_storage()
            ```
        """
        return self._get(
            "/v1/usage/machines/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"period_start": period_start, "period_end": period_end, "machine_id": machine_id},
                    usage_machine_storage_params.UsageMachineStorageParams,
                ),
            ),
            cast_to=MachineStorageUsage,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
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
        """
        Get usage summary

        Args:
            period_start: Billing period start (YYYY-MM-DD). Defaults to first of current month.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            OrgUsage: OK

        Example:
            ```python
            usage = await client.usage.retrieve()
            ```
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
        period_start: str | Omit = omit,
        period_end: str | Omit = omit,
        machine_id: str | Omit = omit,
        granularity: str | Omit = omit,
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
            period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.
            period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.
            machine_id: Optional machine ID filter.
            granularity: Usage breakdown granularity: hour or day. Defaults to hour.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineComputeUsage: OK

        Example:
            ```python
            usage = await client.usage.machine_compute()
            ```
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
                        "period_start": period_start,
                        "period_end": period_end,
                        "machine_id": machine_id,
                        "granularity": granularity,
                    },
                    usage_machine_compute_params.UsageMachineComputeParams,
                ),
            ),
            cast_to=MachineComputeUsage,
        )

    async def machine_storage(
        self,
        *,
        period_start: str | Omit = omit,
        period_end: str | Omit = omit,
        machine_id: str | Omit = omit,
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
            period_start: Usage period start (YYYY-MM-DD). Defaults to first of current month.
            period_end: Last UTC usage date to include (YYYY-MM-DD). Defaults to current time.
            machine_id: Optional machine ID filter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineStorageUsage: OK

        Example:
            ```python
            usage = await client.usage.machine_storage()
            ```
        """
        return await self._get(
            "/v1/usage/machines/storage",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"period_start": period_start, "period_end": period_end, "machine_id": machine_id},
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
