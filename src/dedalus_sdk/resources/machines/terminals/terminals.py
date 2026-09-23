# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict
from typing import Callable

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given
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
from ....types.machines import terminal_list_params, terminal_create_params
from ....types.machines.terminal import Terminal
from ....types.websocket_connection_options import WebSocketConnectionOptions
from ....types.websocket_reconnection import ReconnectingEvent, ReconnectingOverrides
from .ws import (
    TerminalsResourceConnectionManager as TerminalsResourceConnectionManager,
    AsyncTerminalsResourceConnectionManager as AsyncTerminalsResourceConnectionManager,
    TerminalsResourceConnection as TerminalsResourceConnection,
    AsyncTerminalsResourceConnection as AsyncTerminalsResourceConnection,
)

__all__ = ["TerminalsResource", "AsyncTerminalsResource"]


class TerminalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TerminalsResourceWithRawResponse:
        return TerminalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TerminalsResourceWithStreamingResponse:
        return TerminalsResourceWithStreamingResponse(self)

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
    ) -> SyncCursorPage[Terminal]:
        """
        List terminals

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
            SyncCursorPage[Terminal]: OK

        Example:
            ```python
            page = client.machines.terminals.list(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/terminals", **{"machine_id": machine_id}),
            page=SyncCursorPage[Terminal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, terminal_list_params.TerminalListParams),
            ),
            model=Terminal,
            method="get",
        )

    def create(
        self,
        *,
        machine_id: str,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        height: int,
        shell: str | Omit = omit,
        width: int,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Terminal:
        """
        Create terminal

        Args:
            machine_id: Path parameter.
            cwd: Body parameter.
            env: Body parameter.
            height: Body parameter.
            shell: Body parameter.
            width: Body parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Terminal: OK

        Example:
            ```python
            terminal = client.machines.terminals.create(
                machine_id="machineID",
                height=0,
                width=0,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/machines/{machine_id}/terminals", **{"machine_id": machine_id}),
            body=maybe_transform(
                {
                    "cwd": cwd,
                    "env": env,
                    "height": height,
                    "shell": shell,
                    "width": width,
                },
                terminal_create_params.TerminalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Terminal,
        )

    def retrieve(
        self,
        *,
        machine_id: str,
        terminal_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Terminal:
        """
        Get terminal

        Args:
            machine_id: Path parameter.
            terminal_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Terminal: OK

        Example:
            ```python
            terminal = client.machines.terminals.retrieve(
                machine_id="machineID",
                terminal_id="terminalID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if terminal_id is None or (isinstance(terminal_id, str) and not terminal_id):
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}",
                **{"machine_id": machine_id, "terminal_id": terminal_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Terminal,
        )

    def delete(
        self,
        *,
        machine_id: str,
        terminal_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Terminal:
        """
        Delete terminal

        Args:
            machine_id: Path parameter.
            terminal_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Terminal: OK

        Example:
            ```python
            terminal = client.machines.terminals.delete(
                machine_id="machineID",
                terminal_id="terminalID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if terminal_id is None or (isinstance(terminal_id, str) and not terminal_id):
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}",
                **{"machine_id": machine_id, "terminal_id": terminal_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Terminal,
        )

    def connect(
        self,
        *,
        machine_id: str,
        terminal_id: str,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> TerminalsResourceConnectionManager:
        return TerminalsResourceConnectionManager(
            client=self._client,
            machine_id=machine_id,
            terminal_id=terminal_id,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
            on_reconnecting=on_reconnecting,
            max_retries=max_retries,
            initial_delay=initial_delay,
            max_delay=max_delay,
            max_queue_size=max_queue_size,
        )


class AsyncTerminalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTerminalsResourceWithRawResponse:
        return AsyncTerminalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTerminalsResourceWithStreamingResponse:
        return AsyncTerminalsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Terminal, AsyncCursorPage[Terminal]]:
        """
        List terminals

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
            AsyncPaginator[Terminal, AsyncCursorPage[Terminal]]: OK

        Example:
            ```python
            page = client.machines.terminals.list(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/terminals", **{"machine_id": machine_id}),
            page=AsyncCursorPage[Terminal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, terminal_list_params.TerminalListParams),
            ),
            model=Terminal,
            method="get",
        )

    async def create(
        self,
        *,
        machine_id: str,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        height: int,
        shell: str | Omit = omit,
        width: int,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Terminal:
        """
        Create terminal

        Args:
            machine_id: Path parameter.
            cwd: Body parameter.
            env: Body parameter.
            height: Body parameter.
            shell: Body parameter.
            width: Body parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Terminal: OK

        Example:
            ```python
            terminal = await client.machines.terminals.create(
                machine_id="machineID",
                height=0,
                width=0,
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/machines/{machine_id}/terminals", **{"machine_id": machine_id}),
            body=await async_maybe_transform(
                {
                    "cwd": cwd,
                    "env": env,
                    "height": height,
                    "shell": shell,
                    "width": width,
                },
                terminal_create_params.TerminalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Terminal,
        )

    async def retrieve(
        self,
        *,
        machine_id: str,
        terminal_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Terminal:
        """
        Get terminal

        Args:
            machine_id: Path parameter.
            terminal_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Terminal: OK

        Example:
            ```python
            terminal = await client.machines.terminals.retrieve(
                machine_id="machineID",
                terminal_id="terminalID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if terminal_id is None or (isinstance(terminal_id, str) and not terminal_id):
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}",
                **{"machine_id": machine_id, "terminal_id": terminal_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Terminal,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        terminal_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Terminal:
        """
        Delete terminal

        Args:
            machine_id: Path parameter.
            terminal_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Terminal: OK

        Example:
            ```python
            terminal = await client.machines.terminals.delete(
                machine_id="machineID",
                terminal_id="terminalID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if terminal_id is None or (isinstance(terminal_id, str) and not terminal_id):
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}",
                **{"machine_id": machine_id, "terminal_id": terminal_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Terminal,
        )

    def connect(
        self,
        *,
        machine_id: str,
        terminal_id: str,
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
        on_reconnecting: Callable[[ReconnectingEvent], ReconnectingOverrides | None] | None = None,
        max_retries: int = 5,
        initial_delay: float = 0.5,
        max_delay: float = 8.0,
        max_queue_size: int = 1_048_576,
    ) -> AsyncTerminalsResourceConnectionManager:
        return AsyncTerminalsResourceConnectionManager(
            client=self._client,
            machine_id=machine_id,
            terminal_id=terminal_id,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
            on_reconnecting=on_reconnecting,
            max_retries=max_retries,
            initial_delay=initial_delay,
            max_delay=max_delay,
            max_queue_size=max_queue_size,
        )


class TerminalsResourceWithRawResponse:
    def __init__(self, terminals: TerminalsResource) -> None:
        self._terminals = terminals

        self.list = to_raw_response_wrapper(
            terminals.list,
        )
        self.create = to_raw_response_wrapper(
            terminals.create,
        )
        self.retrieve = to_raw_response_wrapper(
            terminals.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            terminals.delete,
        )


class AsyncTerminalsResourceWithRawResponse:
    def __init__(self, terminals: AsyncTerminalsResource) -> None:
        self._terminals = terminals

        self.list = async_to_raw_response_wrapper(
            terminals.list,
        )
        self.create = async_to_raw_response_wrapper(
            terminals.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            terminals.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            terminals.delete,
        )


class TerminalsResourceWithStreamingResponse:
    def __init__(self, terminals: TerminalsResource) -> None:
        self._terminals = terminals

        self.list = to_streamed_response_wrapper(
            terminals.list,
        )
        self.create = to_streamed_response_wrapper(
            terminals.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            terminals.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            terminals.delete,
        )


class AsyncTerminalsResourceWithStreamingResponse:
    def __init__(self, terminals: AsyncTerminalsResource) -> None:
        self._terminals = terminals

        self.list = async_to_streamed_response_wrapper(
            terminals.list,
        )
        self.create = async_to_streamed_response_wrapper(
            terminals.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            terminals.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            terminals.delete,
        )
