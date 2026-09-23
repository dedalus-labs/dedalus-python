# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Callable

from ...._types import Query, Headers
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
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


class AsyncTerminalsResourceWithRawResponse:
    def __init__(self, terminals: AsyncTerminalsResource) -> None:
        self._terminals = terminals


class TerminalsResourceWithStreamingResponse:
    def __init__(self, terminals: TerminalsResource) -> None:
        self._terminals = terminals


class AsyncTerminalsResourceWithStreamingResponse:
    def __init__(self, terminals: AsyncTerminalsResource) -> None:
        self._terminals = terminals
