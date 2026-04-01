# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
import logging
from types import TracebackType
from typing import TYPE_CHECKING, Any, Dict, Iterator, cast
from typing_extensions import AsyncIterator

import httpx
from pydantic import BaseModel

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._models import construct_type_unchecked
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._exceptions import DedalusError
from ..._base_client import AsyncPaginator, _merge_mappings, make_request_options
from ...types.machines import terminal_list_params, terminal_create_params
from ...types.machines.terminal import Terminal
from ...types.websocket_connection_options import WebSocketConnectionOptions
from ...types.machines.terminal_client_event import TerminalClientEvent
from ...types.machines.terminal_server_event import TerminalServerEvent
from ...types.machines.terminal_client_event_param import TerminalClientEventParam

if TYPE_CHECKING:
    from websockets.sync.client import ClientConnection as WebSocketConnection
    from websockets.asyncio.client import ClientConnection as AsyncWebSocketConnection

    from ..._client import Dedalus, AsyncDedalus

__all__ = ["TerminalsResource", "AsyncTerminalsResource"]

log: logging.Logger = logging.getLogger(__name__)


class TerminalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TerminalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return TerminalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TerminalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return TerminalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        machine_id: str,
        height: int,
        width: int,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        shell: str | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._post(
            path_template("/v1/machines/{machine_id}/terminals", machine_id=machine_id),
            body=maybe_transform(
                {
                    "height": height,
                    "width": width,
                    "cwd": cwd,
                    "env": env,
                    "shell": shell,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}", machine_id=machine_id, terminal_id=terminal_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Terminal,
        )

    def list(
        self,
        *,
        machine_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/terminals", machine_id=machine_id),
            page=SyncCursorPage[Terminal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    terminal_list_params.TerminalListParams,
                ),
            ),
            model=Terminal,
        )

    def delete(
        self,
        *,
        machine_id: str,
        terminal_id: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}", machine_id=machine_id, terminal_id=terminal_id
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
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
    ) -> TerminalsResourceConnectionManager:
        return TerminalsResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
        )


class AsyncTerminalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTerminalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTerminalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTerminalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return AsyncTerminalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        machine_id: str,
        height: int,
        width: int,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        shell: str | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._post(
            path_template("/v1/machines/{machine_id}/terminals", machine_id=machine_id),
            body=await async_maybe_transform(
                {
                    "height": height,
                    "width": width,
                    "cwd": cwd,
                    "env": env,
                    "shell": shell,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}", machine_id=machine_id, terminal_id=terminal_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Terminal,
        )

    def list(
        self,
        *,
        machine_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/terminals", machine_id=machine_id),
            page=AsyncCursorPage[Terminal],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    terminal_list_params.TerminalListParams,
                ),
            ),
            model=Terminal,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        terminal_id: str,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/terminals/{terminal_id}", machine_id=machine_id, terminal_id=terminal_id
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
        extra_query: Query = {},
        extra_headers: Headers = {},
        websocket_connection_options: WebSocketConnectionOptions = {},
    ) -> AsyncTerminalsResourceConnectionManager:
        return AsyncTerminalsResourceConnectionManager(
            client=self._client,
            extra_query=extra_query,
            extra_headers=extra_headers,
            websocket_connection_options=websocket_connection_options,
        )


class TerminalsResourceWithRawResponse:
    def __init__(self, terminals: TerminalsResource) -> None:
        self._terminals = terminals

        self.create = to_raw_response_wrapper(
            terminals.create,
        )
        self.retrieve = to_raw_response_wrapper(
            terminals.retrieve,
        )
        self.list = to_raw_response_wrapper(
            terminals.list,
        )
        self.delete = to_raw_response_wrapper(
            terminals.delete,
        )


class AsyncTerminalsResourceWithRawResponse:
    def __init__(self, terminals: AsyncTerminalsResource) -> None:
        self._terminals = terminals

        self.create = async_to_raw_response_wrapper(
            terminals.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            terminals.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            terminals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            terminals.delete,
        )


class TerminalsResourceWithStreamingResponse:
    def __init__(self, terminals: TerminalsResource) -> None:
        self._terminals = terminals

        self.create = to_streamed_response_wrapper(
            terminals.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            terminals.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            terminals.list,
        )
        self.delete = to_streamed_response_wrapper(
            terminals.delete,
        )


class AsyncTerminalsResourceWithStreamingResponse:
    def __init__(self, terminals: AsyncTerminalsResource) -> None:
        self._terminals = terminals

        self.create = async_to_streamed_response_wrapper(
            terminals.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            terminals.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            terminals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            terminals.delete,
        )


class AsyncTerminalsResourceConnection:
    """Represents a live WebSocket connection to the Terminals API"""

    _connection: AsyncWebSocketConnection

    def __init__(self, connection: AsyncWebSocketConnection) -> None:
        self._connection = connection

    async def __aiter__(self) -> AsyncIterator[TerminalServerEvent]:
        """
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        """
        from websockets.exceptions import ConnectionClosedOK

        try:
            while True:
                yield await self.recv()
        except ConnectionClosedOK:
            return

    async def recv(self) -> TerminalServerEvent:
        """
        Receive the next message from the connection and parses it into a `TerminalServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(await self.recv_bytes())

    async def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `TerminalServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = await self._connection.recv(decode=False)
        log.debug(f"Received WebSocket message: %s", message)
        return message

    async def send(self, event: TerminalClientEvent | TerminalClientEventParam) -> None:
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(await async_maybe_transform(event, TerminalClientEventParam))
        )
        await self._connection.send(data)

    async def close(self, *, code: int = 1000, reason: str = "") -> None:
        await self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> TerminalServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `TerminalServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            TerminalServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, TerminalServerEvent))
        )


class AsyncTerminalsResourceConnectionManager:
    """
    Context manager over a `AsyncTerminalsResourceConnection` that is returned by `machines.terminals.connect()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = await client.machines.terminals.connect(...).enter()
    # ...
    await connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: AsyncDedalus,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebSocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__connection: AsyncTerminalsResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    async def __aenter__(self) -> AsyncTerminalsResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = await client.machines.terminals.connect(...).enter()
        # ...
        await connection.close()
        ```
        """
        try:
            from websockets.asyncio.client import connect
        except ImportError as exc:
            raise DedalusError("You need to install `dedalus-sdk[websockets]` to use this method") from exc

        url = self._prepare_url().copy_with(
            params={
                **self.__client.base_url.params,
                **self.__extra_query,
            },
        )
        log.debug("Connecting to %s", url)
        if self.__websocket_connection_options:
            log.debug("Connection options: %s", self.__websocket_connection_options)

        self.__connection = AsyncTerminalsResourceConnection(
            await connect(
                str(url),
                user_agent_header=self.__client.user_agent,
                additional_headers=_merge_mappings(
                    {
                        **self.__client.auth_headers,
                    },
                    self.__extra_headers,
                ),
                **self.__websocket_connection_options,
            )
        )

        return self.__connection

    enter = __aenter__

    def _prepare_url(self) -> httpx.URL:
        if self.__client.websocket_base_url is not None:
            base_url = httpx.URL(self.__client.websocket_base_url)
        else:
            scheme = self.__client._base_url.scheme
            ws_scheme = "ws" if scheme == "http" else "wss"
            base_url = self.__client._base_url.copy_with(scheme=ws_scheme)

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/v1/machines/{machine_id}/terminals/{terminal_id}/stream"
        return base_url.copy_with(raw_path=merge_raw_path)

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            await self.__connection.close()


class TerminalsResourceConnection:
    """Represents a live WebSocket connection to the Terminals API"""

    _connection: WebSocketConnection

    def __init__(self, connection: WebSocketConnection) -> None:
        self._connection = connection

    def __iter__(self) -> Iterator[TerminalServerEvent]:
        """
        An infinite-iterator that will continue to yield events until
        the connection is closed.
        """
        from websockets.exceptions import ConnectionClosedOK

        try:
            while True:
                yield self.recv()
        except ConnectionClosedOK:
            return

    def recv(self) -> TerminalServerEvent:
        """
        Receive the next message from the connection and parses it into a `TerminalServerEvent` object.

        Canceling this method is safe. There's no risk of losing data.
        """
        return self.parse_event(self.recv_bytes())

    def recv_bytes(self) -> bytes:
        """Receive the next message from the connection as raw bytes.

        Canceling this method is safe. There's no risk of losing data.

        If you want to parse the message into a `TerminalServerEvent` object like `.recv()` does,
        then you can call `.parse_event(data)`.
        """
        message = self._connection.recv(decode=False)
        log.debug(f"Received WebSocket message: %s", message)
        return message

    def send(self, event: TerminalClientEvent | TerminalClientEventParam) -> None:
        data = (
            event.to_json(use_api_names=True, exclude_defaults=True, exclude_unset=True)
            if isinstance(event, BaseModel)
            else json.dumps(maybe_transform(event, TerminalClientEventParam))
        )
        self._connection.send(data)

    def close(self, *, code: int = 1000, reason: str = "") -> None:
        self._connection.close(code=code, reason=reason)

    def parse_event(self, data: str | bytes) -> TerminalServerEvent:
        """
        Converts a raw `str` or `bytes` message into a `TerminalServerEvent` object.

        This is helpful if you're using `.recv_bytes()`.
        """
        return cast(
            TerminalServerEvent, construct_type_unchecked(value=json.loads(data), type_=cast(Any, TerminalServerEvent))
        )


class TerminalsResourceConnectionManager:
    """
    Context manager over a `TerminalsResourceConnection` that is returned by `machines.terminals.connect()`

    This context manager ensures that the connection will be closed when it exits.

    ---

    Note that if your application doesn't work well with the context manager approach then you
    can call the `.enter()` method directly to initiate a connection.

    **Warning**: You must remember to close the connection with `.close()`.

    ```py
    connection = client.machines.terminals.connect(...).enter()
    # ...
    connection.close()
    ```
    """

    def __init__(
        self,
        *,
        client: Dedalus,
        extra_query: Query,
        extra_headers: Headers,
        websocket_connection_options: WebSocketConnectionOptions,
    ) -> None:
        self.__client = client
        self.__connection: TerminalsResourceConnection | None = None
        self.__extra_query = extra_query
        self.__extra_headers = extra_headers
        self.__websocket_connection_options = websocket_connection_options

    def __enter__(self) -> TerminalsResourceConnection:
        """
        👋 If your application doesn't work well with the context manager approach then you
        can call this method directly to initiate a connection.

        **Warning**: You must remember to close the connection with `.close()`.

        ```py
        connection = client.machines.terminals.connect(...).enter()
        # ...
        connection.close()
        ```
        """
        try:
            from websockets.sync.client import connect
        except ImportError as exc:
            raise DedalusError("You need to install `dedalus-sdk[websockets]` to use this method") from exc

        url = self._prepare_url().copy_with(
            params={
                **self.__client.base_url.params,
                **self.__extra_query,
            },
        )
        log.debug("Connecting to %s", url)
        if self.__websocket_connection_options:
            log.debug("Connection options: %s", self.__websocket_connection_options)

        self.__connection = TerminalsResourceConnection(
            connect(
                str(url),
                user_agent_header=self.__client.user_agent,
                additional_headers=_merge_mappings(
                    {
                        **self.__client.auth_headers,
                    },
                    self.__extra_headers,
                ),
                **self.__websocket_connection_options,
            )
        )

        return self.__connection

    enter = __enter__

    def _prepare_url(self) -> httpx.URL:
        if self.__client.websocket_base_url is not None:
            base_url = httpx.URL(self.__client.websocket_base_url)
        else:
            scheme = self.__client._base_url.scheme
            ws_scheme = "ws" if scheme == "http" else "wss"
            base_url = self.__client._base_url.copy_with(scheme=ws_scheme)

        merge_raw_path = base_url.raw_path.rstrip(b"/") + b"/v1/machines/{machine_id}/terminals/{terminal_id}/stream"
        return base_url.copy_with(raw_path=merge_raw_path)

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        if self.__connection is not None:
            self.__connection.close()
