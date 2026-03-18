# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...pagination import SyncSSHSessionList, AsyncSSHSessionList
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workspaces import ssh_list_params, ssh_create_params
from ...types.workspaces.ssh_session import SSHSession

__all__ = ["SSHResource", "AsyncSSHResource"]


class SSHResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSHResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return SSHResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSHResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return SSHResourceWithStreamingResponse(self)

    def create(
        self,
        workspace_id: str,
        *,
        public_key: str,
        wake_if_needed: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SSHSession:
        """
        Create SSH session

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
            f"/v1/workspaces/{workspace_id}/ssh",
            body=maybe_transform(
                {
                    "public_key": public_key,
                    "wake_if_needed": wake_if_needed,
                },
                ssh_create_params.SSHCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SSHSession,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHSession:
        """
        Get SSH session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/v1/workspaces/{workspace_id}/ssh/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHSession,
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
    ) -> SyncSSHSessionList[SSHSession]:
        """
        List SSH sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            f"/v1/workspaces/{workspace_id}/ssh",
            page=SyncSSHSessionList[SSHSession],
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
                    ssh_list_params.SSHListParams,
                ),
            ),
            model=SSHSession,
        )

    def delete(
        self,
        session_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SSHSession:
        """
        Delete SSH session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            f"/v1/workspaces/{workspace_id}/ssh/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SSHSession,
        )


class AsyncSSHResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSHResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSHResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSHResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return AsyncSSHResourceWithStreamingResponse(self)

    async def create(
        self,
        workspace_id: str,
        *,
        public_key: str,
        wake_if_needed: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SSHSession:
        """
        Create SSH session

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
            f"/v1/workspaces/{workspace_id}/ssh",
            body=await async_maybe_transform(
                {
                    "public_key": public_key,
                    "wake_if_needed": wake_if_needed,
                },
                ssh_create_params.SSHCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SSHSession,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SSHSession:
        """
        Get SSH session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/v1/workspaces/{workspace_id}/ssh/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHSession,
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
    ) -> AsyncPaginator[SSHSession, AsyncSSHSessionList[SSHSession]]:
        """
        List SSH sessions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get_api_list(
            f"/v1/workspaces/{workspace_id}/ssh",
            page=AsyncSSHSessionList[SSHSession],
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
                    ssh_list_params.SSHListParams,
                ),
            ),
            model=SSHSession,
        )

    async def delete(
        self,
        session_id: str,
        *,
        workspace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> SSHSession:
        """
        Delete SSH session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            f"/v1/workspaces/{workspace_id}/ssh/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=SSHSession,
        )


class SSHResourceWithRawResponse:
    def __init__(self, ssh: SSHResource) -> None:
        self._ssh = ssh

        self.create = to_raw_response_wrapper(
            ssh.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ssh.retrieve,
        )
        self.list = to_raw_response_wrapper(
            ssh.list,
        )
        self.delete = to_raw_response_wrapper(
            ssh.delete,
        )


class AsyncSSHResourceWithRawResponse:
    def __init__(self, ssh: AsyncSSHResource) -> None:
        self._ssh = ssh

        self.create = async_to_raw_response_wrapper(
            ssh.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ssh.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            ssh.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ssh.delete,
        )


class SSHResourceWithStreamingResponse:
    def __init__(self, ssh: SSHResource) -> None:
        self._ssh = ssh

        self.create = to_streamed_response_wrapper(
            ssh.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ssh.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            ssh.list,
        )
        self.delete = to_streamed_response_wrapper(
            ssh.delete,
        )


class AsyncSSHResourceWithStreamingResponse:
    def __init__(self, ssh: AsyncSSHResource) -> None:
        self._ssh = ssh

        self.create = async_to_streamed_response_wrapper(
            ssh.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ssh.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            ssh.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ssh.delete,
        )
