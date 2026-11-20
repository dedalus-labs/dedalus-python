# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Optional
from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.machines.policy import Policy
from ...types.organization import autoresizing_update_params

__all__ = ["AutoresizingResource", "AsyncAutoresizingResource"]


class AutoresizingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutoresizingResourceWithRawResponse:
        return AutoresizingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutoresizingResourceWithStreamingResponse:
        return AutoresizingResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Read organization autoresizing policy

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Policy: OK

        Example:
            ```python
            autoresizing = client.organization.autoresizing.retrieve()
            ```
        """
        return self._get(
            "/v1/organization/autoresizing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def update(
        self,
        *,
        cpu: Literal["on", "off"] | Omit = omit,
        cpu_max_vcpu: Optional[float] | Omit = omit,
        memory: Literal["on", "off"] | Omit = omit,
        memory_max_mib: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Policy:
        """
        Changes defaults copied to new Machines. Existing Machines retain their own policy.

        Args:
            cpu: Body parameter.
            cpu_max_vcpu: Body parameter.
            memory: Body parameter.
            memory_max_mib: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Policy: OK

        Example:
            ```python
            autoresizing = client.organization.autoresizing.update(
                idempotency_key="",
            )
            ```
        """
        return self._patch(
            "/v1/organization/autoresizing",
            body=maybe_transform(
                {
                    "cpu": cpu,
                    "cpu_max_vcpu": cpu_max_vcpu,
                    "memory": memory,
                    "memory_max_mib": memory_max_mib,
                },
                autoresizing_update_params.AutoresizingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Policy,
        )


class AsyncAutoresizingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutoresizingResourceWithRawResponse:
        return AsyncAutoresizingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutoresizingResourceWithStreamingResponse:
        return AsyncAutoresizingResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Read organization autoresizing policy

        Args:
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Policy: OK

        Example:
            ```python
            autoresizing = await client.organization.autoresizing.retrieve()
            ```
        """
        return await self._get(
            "/v1/organization/autoresizing",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def update(
        self,
        *,
        cpu: Literal["on", "off"] | Omit = omit,
        cpu_max_vcpu: Optional[float] | Omit = omit,
        memory: Literal["on", "off"] | Omit = omit,
        memory_max_mib: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Policy:
        """
        Changes defaults copied to new Machines. Existing Machines retain their own policy.

        Args:
            cpu: Body parameter.
            cpu_max_vcpu: Body parameter.
            memory: Body parameter.
            memory_max_mib: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Policy: OK

        Example:
            ```python
            autoresizing = await client.organization.autoresizing.update(
                idempotency_key="",
            )
            ```
        """
        return await self._patch(
            "/v1/organization/autoresizing",
            body=await async_maybe_transform(
                {
                    "cpu": cpu,
                    "cpu_max_vcpu": cpu_max_vcpu,
                    "memory": memory,
                    "memory_max_mib": memory_max_mib,
                },
                autoresizing_update_params.AutoresizingUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Policy,
        )


class AutoresizingResourceWithRawResponse:
    def __init__(self, autoresizing: AutoresizingResource) -> None:
        self._autoresizing = autoresizing

        self.retrieve = to_raw_response_wrapper(
            autoresizing.retrieve,
        )
        self.update = to_raw_response_wrapper(
            autoresizing.update,
        )


class AsyncAutoresizingResourceWithRawResponse:
    def __init__(self, autoresizing: AsyncAutoresizingResource) -> None:
        self._autoresizing = autoresizing

        self.retrieve = async_to_raw_response_wrapper(
            autoresizing.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            autoresizing.update,
        )


class AutoresizingResourceWithStreamingResponse:
    def __init__(self, autoresizing: AutoresizingResource) -> None:
        self._autoresizing = autoresizing

        self.retrieve = to_streamed_response_wrapper(
            autoresizing.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            autoresizing.update,
        )


class AsyncAutoresizingResourceWithStreamingResponse:
    def __init__(self, autoresizing: AsyncAutoresizingResource) -> None:
        self._autoresizing = autoresizing

        self.retrieve = async_to_streamed_response_wrapper(
            autoresizing.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            autoresizing.update,
        )
