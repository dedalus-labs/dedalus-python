# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.machines.machine_network import MachineNetwork

__all__ = ["NetworkResource", "AsyncNetworkResource"]


class NetworkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkResourceWithRawResponse:
        return NetworkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkResourceWithStreamingResponse:
        return NetworkResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        machine_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineNetwork:
        """
        Get machine network identity

        Args:
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineNetwork: OK

        Example:
            ```python
            network = client.machines.network.retrieve(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/machines/{machine_id}/network", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MachineNetwork,
        )


class AsyncNetworkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkResourceWithRawResponse:
        return AsyncNetworkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkResourceWithStreamingResponse:
        return AsyncNetworkResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        machine_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineNetwork:
        """
        Get machine network identity

        Args:
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineNetwork: OK

        Example:
            ```python
            network = await client.machines.network.retrieve(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/machines/{machine_id}/network", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MachineNetwork,
        )


class NetworkResourceWithRawResponse:
    def __init__(self, network: NetworkResource) -> None:
        self._network = network

        self.retrieve = to_raw_response_wrapper(
            network.retrieve,
        )


class AsyncNetworkResourceWithRawResponse:
    def __init__(self, network: AsyncNetworkResource) -> None:
        self._network = network

        self.retrieve = async_to_raw_response_wrapper(
            network.retrieve,
        )


class NetworkResourceWithStreamingResponse:
    def __init__(self, network: NetworkResource) -> None:
        self._network = network

        self.retrieve = to_streamed_response_wrapper(
            network.retrieve,
        )


class AsyncNetworkResourceWithStreamingResponse:
    def __init__(self, network: AsyncNetworkResource) -> None:
        self._network = network

        self.retrieve = async_to_streamed_response_wrapper(
            network.retrieve,
        )
