# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.machines import port_list_params, port_create_params
from ...types.machines.port import Port

__all__ = ["PortsResource", "AsyncPortsResource"]


class PortsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortsResourceWithRawResponse:
        return PortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortsResourceWithStreamingResponse:
        return PortsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        machine_id: str,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Port]:
        """
        List ports

        Args:
            machine_id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SyncCursorPage[Port]: OK

        Example:
            ```python
            page = client.machines.ports.list(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/ports", **{"machine_id": machine_id}),
            page=SyncCursorPage[Port],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, port_list_params.PortListParams),
            ),
            model=Port,
            method="get",
        )

    def create(
        self,
        *,
        machine_id: str,
        port: int,
        protocol: Literal["http", "https"] | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Port:
        """
        Create port

        Args:
            machine_id: Path parameter.
            port: Body parameter.
            protocol: Body parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Port: OK

        Example:
            ```python
            port = client.machines.ports.create(
                machine_id="machineID",
                port=0,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/machines/{machine_id}/ports", **{"machine_id": machine_id}),
            body=maybe_transform(
                {
                    "port": port,
                    "protocol": protocol,
                },
                port_create_params.PortCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Port,
        )

    def retrieve(
        self,
        *,
        machine_id: str,
        port_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Get port

        Args:
            machine_id: Path parameter.
            port_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Port: OK

        Example:
            ```python
            port = client.machines.ports.retrieve(
                machine_id="machineID",
                port_id="portID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Port,
        )

    def delete(
        self,
        *,
        machine_id: str,
        port_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Port:
        """
        Delete port

        Args:
            machine_id: Path parameter.
            port_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Port: OK

        Example:
            ```python
            port = client.machines.ports.delete(
                machine_id="machineID",
                port_id="portID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Port,
        )


class AsyncPortsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortsResourceWithRawResponse:
        return AsyncPortsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortsResourceWithStreamingResponse:
        return AsyncPortsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        machine_id: str,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Port, AsyncCursorPage[Port]]:
        """
        List ports

        Args:
            machine_id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncPaginator[Port, AsyncCursorPage[Port]]: OK

        Example:
            ```python
            page = client.machines.ports.list(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/ports", **{"machine_id": machine_id}),
            page=AsyncCursorPage[Port],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, port_list_params.PortListParams),
            ),
            model=Port,
            method="get",
        )

    async def create(
        self,
        *,
        machine_id: str,
        port: int,
        protocol: Literal["http", "https"] | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Port:
        """
        Create port

        Args:
            machine_id: Path parameter.
            port: Body parameter.
            protocol: Body parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Port: OK

        Example:
            ```python
            port = await client.machines.ports.create(
                machine_id="machineID",
                port=0,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/machines/{machine_id}/ports", **{"machine_id": machine_id}),
            body=await async_maybe_transform(
                {
                    "port": port,
                    "protocol": protocol,
                },
                port_create_params.PortCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Port,
        )

    async def retrieve(
        self,
        *,
        machine_id: str,
        port_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Port:
        """
        Get port

        Args:
            machine_id: Path parameter.
            port_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Port: OK

        Example:
            ```python
            port = await client.machines.ports.retrieve(
                machine_id="machineID",
                port_id="portID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Port,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        port_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Port:
        """
        Delete port

        Args:
            machine_id: Path parameter.
            port_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Port: OK

        Example:
            ```python
            port = await client.machines.ports.delete(
                machine_id="machineID",
                port_id="portID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Port,
        )


class PortsResourceWithRawResponse:
    def __init__(self, ports: PortsResource) -> None:
        self._ports = ports

        self.list = to_raw_response_wrapper(
            ports.list,
        )
        self.create = to_raw_response_wrapper(
            ports.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ports.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            ports.delete,
        )


class AsyncPortsResourceWithRawResponse:
    def __init__(self, ports: AsyncPortsResource) -> None:
        self._ports = ports

        self.list = async_to_raw_response_wrapper(
            ports.list,
        )
        self.create = async_to_raw_response_wrapper(
            ports.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ports.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            ports.delete,
        )


class PortsResourceWithStreamingResponse:
    def __init__(self, ports: PortsResource) -> None:
        self._ports = ports

        self.list = to_streamed_response_wrapper(
            ports.list,
        )
        self.create = to_streamed_response_wrapper(
            ports.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ports.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            ports.delete,
        )


class AsyncPortsResourceWithStreamingResponse:
    def __init__(self, ports: AsyncPortsResource) -> None:
        self._ports = ports

        self.list = async_to_streamed_response_wrapper(
            ports.list,
        )
        self.create = async_to_streamed_response_wrapper(
            ports.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ports.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            ports.delete,
        )
