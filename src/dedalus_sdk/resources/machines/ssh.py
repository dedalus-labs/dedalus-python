# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

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
from ...types.machines import ssh_list_params, ssh_create_params
from ...types.machines.ssh_session import SSHSession

__all__ = ["SSHResource", "AsyncSSHResource"]


class SSHResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSHResourceWithRawResponse:
        return SSHResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSHResourceWithStreamingResponse:
        return SSHResourceWithStreamingResponse(self)

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
    ) -> SyncCursorPage[SSHSession]:
        """
        List SSH sessions

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SyncCursorPage[SSHSession]: OK

        Example:
            ```python
            page = client.machines.ssh.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/ssh", **{"machine_id": machine_id}),
            page=SyncCursorPage[SSHSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, ssh_list_params.SSHListParams),
            ),
            model=SSHSession,
            method="get",
        )

    def create(
        self,
        *,
        machine_id: str,
        public_key: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            public_key: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            SSHSession: OK

        Example:
            ```python
            ssh = client.machines.ssh.create(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                public_key="",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._post(
            path_template("/v1/machines/{machine_id}/ssh", **{"machine_id": machine_id}),
            body=maybe_transform(
                {"public_key": public_key},
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
        *,
        machine_id: str,
        session_id: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SSHSession: OK

        Example:
            ```python
            ssh = client.machines.ssh.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                session_id="sessionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/ssh/{session_id}", **{"machine_id": machine_id, "session_id": session_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHSession,
        )

    def delete(
        self,
        *,
        machine_id: str,
        session_id: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            SSHSession: OK

        Example:
            ```python
            ssh = client.machines.ssh.delete(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                session_id="sessionID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/ssh/{session_id}", **{"machine_id": machine_id, "session_id": session_id}
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


class AsyncSSHResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSHResourceWithRawResponse:
        return AsyncSSHResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSHResourceWithStreamingResponse:
        return AsyncSSHResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[SSHSession, AsyncCursorPage[SSHSession]]:
        """
        List SSH sessions

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncPaginator[SSHSession, AsyncCursorPage[SSHSession]]: OK

        Example:
            ```python
            page = client.machines.ssh.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/ssh", **{"machine_id": machine_id}),
            page=AsyncCursorPage[SSHSession],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, ssh_list_params.SSHListParams),
            ),
            model=SSHSession,
            method="get",
        )

    async def create(
        self,
        *,
        machine_id: str,
        public_key: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            public_key: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            SSHSession: OK

        Example:
            ```python
            ssh = await client.machines.ssh.create(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                public_key="",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._post(
            path_template("/v1/machines/{machine_id}/ssh", **{"machine_id": machine_id}),
            body=await async_maybe_transform(
                {"public_key": public_key},
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
        *,
        machine_id: str,
        session_id: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SSHSession: OK

        Example:
            ```python
            ssh = await client.machines.ssh.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                session_id="sessionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/ssh/{session_id}", **{"machine_id": machine_id, "session_id": session_id}
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSHSession,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        session_id: str,
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
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            session_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            SSHSession: OK

        Example:
            ```python
            ssh = await client.machines.ssh.delete(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                session_id="sessionID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if session_id is None or (isinstance(session_id, str) and not session_id):
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/ssh/{session_id}", **{"machine_id": machine_id, "session_id": session_id}
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


class SSHResourceWithRawResponse:
    def __init__(self, ssh: SSHResource) -> None:
        self._ssh = ssh

        self.list = to_raw_response_wrapper(
            ssh.list,
        )
        self.create = to_raw_response_wrapper(
            ssh.create,
        )
        self.retrieve = to_raw_response_wrapper(
            ssh.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            ssh.delete,
        )


class AsyncSSHResourceWithRawResponse:
    def __init__(self, ssh: AsyncSSHResource) -> None:
        self._ssh = ssh

        self.list = async_to_raw_response_wrapper(
            ssh.list,
        )
        self.create = async_to_raw_response_wrapper(
            ssh.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            ssh.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            ssh.delete,
        )


class SSHResourceWithStreamingResponse:
    def __init__(self, ssh: SSHResource) -> None:
        self._ssh = ssh

        self.list = to_streamed_response_wrapper(
            ssh.list,
        )
        self.create = to_streamed_response_wrapper(
            ssh.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            ssh.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            ssh.delete,
        )


class AsyncSSHResourceWithStreamingResponse:
    def __init__(self, ssh: AsyncSSHResource) -> None:
        self._ssh = ssh

        self.list = async_to_streamed_response_wrapper(
            ssh.list,
        )
        self.create = async_to_streamed_response_wrapper(
            ssh.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            ssh.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            ssh.delete,
        )
