# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

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
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workspaces import terminal_list_params, terminal_create_params
from ...types.workspaces.terminal import Terminal

__all__ = ["TerminalsResource", "AsyncTerminalsResource"]


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
        workspace_id: str,
        *,
        height: int,
        width: int,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        shell: str | Omit = omit,
        wake_if_needed: bool | Omit = omit,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._post(
            path_template("/v1/workspaces/{workspace_id}/terminals", workspace_id=workspace_id),
            body=maybe_transform(
                {
                    "height": height,
                    "width": width,
                    "cwd": cwd,
                    "env": env,
                    "shell": shell,
                    "wake_if_needed": wake_if_needed,
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
        terminal_id: str,
        *,
        workspace_id: str,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/terminals/{terminal_id}",
                workspace_id=workspace_id,
                terminal_id=terminal_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Terminal,
        )

    def list(
        self,
        workspace_id: str,
        *,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/terminals", workspace_id=workspace_id),
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
        terminal_id: str,
        *,
        workspace_id: str,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/terminals/{terminal_id}",
                workspace_id=workspace_id,
                terminal_id=terminal_id,
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
        workspace_id: str,
        *,
        height: int,
        width: int,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        shell: str | Omit = omit,
        wake_if_needed: bool | Omit = omit,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._post(
            path_template("/v1/workspaces/{workspace_id}/terminals", workspace_id=workspace_id),
            body=await async_maybe_transform(
                {
                    "height": height,
                    "width": width,
                    "cwd": cwd,
                    "env": env,
                    "shell": shell,
                    "wake_if_needed": wake_if_needed,
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
        terminal_id: str,
        *,
        workspace_id: str,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return await self._get(
            path_template(
                "/v1/workspaces/{workspace_id}/terminals/{terminal_id}",
                workspace_id=workspace_id,
                terminal_id=terminal_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Terminal,
        )

    def list(
        self,
        workspace_id: str,
        *,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            path_template("/v1/workspaces/{workspace_id}/terminals", workspace_id=workspace_id),
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
        terminal_id: str,
        *,
        workspace_id: str,
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
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not terminal_id:
            raise ValueError(f"Expected a non-empty value for `terminal_id` but received {terminal_id!r}")
        return await self._delete(
            path_template(
                "/v1/workspaces/{workspace_id}/terminals/{terminal_id}",
                workspace_id=workspace_id,
                terminal_id=terminal_id,
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
