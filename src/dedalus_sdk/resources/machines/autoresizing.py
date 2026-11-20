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
from ...types.machines.policy import Policy
from ...types.machines import autoresizing_update_params

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
        machine_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Read this machine's autoresizing settings

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Policy: OK

        Example:
            ```python
            autoresizing = client.machines.autoresizing.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get(
            path_template("/v1/machines/{machine_id}/autoresizing", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    def update(
        self,
        *,
        machine_id: str,
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
        Changes RAM, CPU or both for this machine. An absent resource keeps its setting.

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
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
            autoresizing = client.machines.autoresizing.update(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._patch(
            path_template("/v1/machines/{machine_id}/autoresizing", **{"machine_id": machine_id}),
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
        machine_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Policy:
        """
        Read this machine's autoresizing settings

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Policy: OK

        Example:
            ```python
            autoresizing = await client.machines.autoresizing.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._get(
            path_template("/v1/machines/{machine_id}/autoresizing", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Policy,
        )

    async def update(
        self,
        *,
        machine_id: str,
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
        Changes RAM, CPU or both for this machine. An absent resource keeps its setting.

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
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
            autoresizing = await client.machines.autoresizing.update(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._patch(
            path_template("/v1/machines/{machine_id}/autoresizing", **{"machine_id": machine_id}),
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
