# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.orgs import usage_retrieve_params, usage_get_machine_usage_params, usage_get_machine_storage_usage_params
from ..._base_client import make_request_options
from ...types.orgs.org_usage import OrgUsage
from ...types.orgs.machine_usage import MachineUsage
from ...types.orgs.machine_storage_usage import MachineStorageUsage

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
        org_id: str,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgUsage:
        """
        Get org billed machine usage

        Args:
          period_start: Billing period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v1/orgs/{org_id}/usage", org_id=org_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"period_start": period_start}, usage_retrieve_params.UsageRetrieveParams),
            ),
            cast_to=OrgUsage,
        )

    def get_machine_storage_usage(
        self,
        *,
        org_id: str,
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
        List machine storage usage evidence

        Args:
          machine_id: Optional machine ID filter.

          period_end: Last UTC evidence date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Evidence period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v1/orgs/{org_id}/usage/storage/machines", org_id=org_id),
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
                    usage_get_machine_storage_usage_params.UsageGetMachineStorageUsageParams,
                ),
            ),
            cast_to=MachineStorageUsage,
        )

    def get_machine_usage(
        self,
        *,
        org_id: str,
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
    ) -> MachineUsage:
        """
        List machine usage evidence

        Args:
          granularity: Evidence granularity: hour or day. Defaults to hour.

          machine_id: Optional machine ID filter.

          period_end: Last UTC evidence date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Evidence period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return self._get(
            path_template("/v1/orgs/{org_id}/usage/machines", org_id=org_id),
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
                    usage_get_machine_usage_params.UsageGetMachineUsageParams,
                ),
            ),
            cast_to=MachineUsage,
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
        org_id: str,
        period_start: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrgUsage:
        """
        Get org billed machine usage

        Args:
          period_start: Billing period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v1/orgs/{org_id}/usage", org_id=org_id),
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

    async def get_machine_storage_usage(
        self,
        *,
        org_id: str,
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
        List machine storage usage evidence

        Args:
          machine_id: Optional machine ID filter.

          period_end: Last UTC evidence date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Evidence period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v1/orgs/{org_id}/usage/storage/machines", org_id=org_id),
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
                    usage_get_machine_storage_usage_params.UsageGetMachineStorageUsageParams,
                ),
            ),
            cast_to=MachineStorageUsage,
        )

    async def get_machine_usage(
        self,
        *,
        org_id: str,
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
    ) -> MachineUsage:
        """
        List machine usage evidence

        Args:
          granularity: Evidence granularity: hour or day. Defaults to hour.

          machine_id: Optional machine ID filter.

          period_end: Last UTC evidence date to include (YYYY-MM-DD). Defaults to current time.

          period_start: Evidence period start (YYYY-MM-DD). Defaults to first of current month.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org_id:
            raise ValueError(f"Expected a non-empty value for `org_id` but received {org_id!r}")
        return await self._get(
            path_template("/v1/orgs/{org_id}/usage/machines", org_id=org_id),
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
                    usage_get_machine_usage_params.UsageGetMachineUsageParams,
                ),
            ),
            cast_to=MachineUsage,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = to_raw_response_wrapper(
            usage.retrieve,
        )
        self.get_machine_storage_usage = to_raw_response_wrapper(
            usage.get_machine_storage_usage,
        )
        self.get_machine_usage = to_raw_response_wrapper(
            usage.get_machine_usage,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = async_to_raw_response_wrapper(
            usage.retrieve,
        )
        self.get_machine_storage_usage = async_to_raw_response_wrapper(
            usage.get_machine_storage_usage,
        )
        self.get_machine_usage = async_to_raw_response_wrapper(
            usage.get_machine_usage,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.retrieve = to_streamed_response_wrapper(
            usage.retrieve,
        )
        self.get_machine_storage_usage = to_streamed_response_wrapper(
            usage.get_machine_storage_usage,
        )
        self.get_machine_usage = to_streamed_response_wrapper(
            usage.get_machine_usage,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.retrieve = async_to_streamed_response_wrapper(
            usage.retrieve,
        )
        self.get_machine_storage_usage = async_to_streamed_response_wrapper(
            usage.get_machine_storage_usage,
        )
        self.get_machine_usage = async_to_streamed_response_wrapper(
            usage.get_machine_usage,
        )
