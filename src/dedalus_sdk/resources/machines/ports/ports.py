# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing_extensions import Literal

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from .access_keys import (
    AccessKeysResource,
    AsyncAccessKeysResource,
    AccessKeysResourceWithRawResponse,
    AsyncAccessKeysResourceWithRawResponse,
    AccessKeysResourceWithStreamingResponse,
    AsyncAccessKeysResourceWithStreamingResponse,
)
from ....types.machines import port_list_params, port_create_params, port_update_params
from ....types.machines.port import Port

__all__ = ["PortsResource", "AsyncPortsResource"]


class PortsResource(SyncAPIResource):
    @cached_property
    def access_keys(self) -> AccessKeysResource:
        return AccessKeysResource(self._client)

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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SyncCursorPage[Port]: OK

        Example:
            ```python
            page = client.machines.ports.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
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
        expires: int | Omit = omit,
        port: int,
        protocol: Literal["http"] | Omit = omit,
        visibility: Literal["public", "key_required", "private"] | Omit = omit,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            expires: Port lifetime in integer seconds. Omit for no expiry.
            port: Body parameter.
            protocol: Body parameter.
            visibility: Who may reach the port. private, the default, requires a Dedalus API key from the owning organization in the X-Dedalus-API-Key header. key_required requires a port access key in the X-Dedalus-Port-Key header, and creating the port returns its first key once. public accepts anonymous requests, which can wake the machine and incur compute charges.
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
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port=0,
                protocol="http",
                visibility="private",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._post(
            path_template("/v1/machines/{machine_id}/ports", **{"machine_id": machine_id}),
            body=maybe_transform(
                {
                    "expires": expires,
                    "port": port,
                    "protocol": protocol,
                    "visibility": visibility,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Port: OK

        Example:
            ```python
            port = client.machines.ports.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Port,
        )

    def update(
        self,
        *,
        machine_id: str,
        port_id: str,
        visibility: Literal["public", "key_required", "private"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Port:
        """
        Update port

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            visibility: Who may reach the port. private requires a Dedalus API key from the owning organization in the X-Dedalus-API-Key header. key_required requires a port access key in the X-Dedalus-Port-Key header. public accepts anonymous requests, which can wake the machine and incur compute charges.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Port: OK

        Example:
            ```python
            port = client.machines.ports.update(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                visibility="public",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return self._patch(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            body=maybe_transform(
                {"visibility": visibility},
                port_update_params.PortUpdateParams,
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

    def delete(
        self,
        *,
        machine_id: str,
        port_id: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
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
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
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
    def access_keys(self) -> AsyncAccessKeysResource:
        return AsyncAccessKeysResource(self._client)

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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncPaginator[Port, AsyncCursorPage[Port]]: OK

        Example:
            ```python
            page = client.machines.ports.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
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
        expires: int | Omit = omit,
        port: int,
        protocol: Literal["http"] | Omit = omit,
        visibility: Literal["public", "key_required", "private"] | Omit = omit,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            expires: Port lifetime in integer seconds. Omit for no expiry.
            port: Body parameter.
            protocol: Body parameter.
            visibility: Who may reach the port. private, the default, requires a Dedalus API key from the owning organization in the X-Dedalus-API-Key header. key_required requires a port access key in the X-Dedalus-Port-Key header, and creating the port returns its first key once. public accepts anonymous requests, which can wake the machine and incur compute charges.
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
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port=0,
                protocol="http",
                visibility="private",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._post(
            path_template("/v1/machines/{machine_id}/ports", **{"machine_id": machine_id}),
            body=await async_maybe_transform(
                {
                    "expires": expires,
                    "port": port,
                    "protocol": protocol,
                    "visibility": visibility,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Port: OK

        Example:
            ```python
            port = await client.machines.ports.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Port,
        )

    async def update(
        self,
        *,
        machine_id: str,
        port_id: str,
        visibility: Literal["public", "key_required", "private"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Port:
        """
        Update port

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
            visibility: Who may reach the port. private requires a Dedalus API key from the owning organization in the X-Dedalus-API-Key header. key_required requires a port access key in the X-Dedalus-Port-Key header. public accepts anonymous requests, which can wake the machine and incur compute charges.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Port: OK

        Example:
            ```python
            port = await client.machines.ports.update(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                visibility="public",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
        return await self._patch(
            path_template(
                "/v1/machines/{machine_id}/ports/{port_id}", **{"machine_id": machine_id, "port_id": port_id}
            ),
            body=await async_maybe_transform(
                {"visibility": visibility},
                port_update_params.PortUpdateParams,
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

    async def delete(
        self,
        *,
        machine_id: str,
        port_id: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            port_id: Path parameter.
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
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                port_id="portID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if port_id is None or (isinstance(port_id, str) and not port_id):
            raise ValueError(f"Expected a non-empty value for `port_id` but received {port_id!r}")
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
        self.update = to_raw_response_wrapper(
            ports.update,
        )
        self.delete = to_raw_response_wrapper(
            ports.delete,
        )

    @cached_property
    def access_keys(self) -> AccessKeysResourceWithRawResponse:
        return AccessKeysResourceWithRawResponse(self._ports.access_keys)


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
        self.update = async_to_raw_response_wrapper(
            ports.update,
        )
        self.delete = async_to_raw_response_wrapper(
            ports.delete,
        )

    @cached_property
    def access_keys(self) -> AsyncAccessKeysResourceWithRawResponse:
        return AsyncAccessKeysResourceWithRawResponse(self._ports.access_keys)


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
        self.update = to_streamed_response_wrapper(
            ports.update,
        )
        self.delete = to_streamed_response_wrapper(
            ports.delete,
        )

    @cached_property
    def access_keys(self) -> AccessKeysResourceWithStreamingResponse:
        return AccessKeysResourceWithStreamingResponse(self._ports.access_keys)


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
        self.update = async_to_streamed_response_wrapper(
            ports.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            ports.delete,
        )

    @cached_property
    def access_keys(self) -> AsyncAccessKeysResourceWithStreamingResponse:
        return AsyncAccessKeysResourceWithStreamingResponse(self._ports.access_keys)
