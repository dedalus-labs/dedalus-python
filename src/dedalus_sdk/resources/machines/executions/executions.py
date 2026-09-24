# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from typing import Dict, Optional
from ...._types import SequenceNotStr

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
from .logs import (
    LogsResource,
    AsyncLogsResource,
    LogsResourceWithRawResponse,
    AsyncLogsResourceWithRawResponse,
    LogsResourceWithStreamingResponse,
    AsyncLogsResourceWithStreamingResponse,
)
from ....types.machines import execution_list_params, execution_create_params, execution_events_params
from ....types.machines.execution import Execution
from ....types.machines.execution_output import ExecutionOutput
from ....types.machines.execution_event import ExecutionEvent

__all__ = ["ExecutionsResource", "AsyncExecutionsResource"]


class ExecutionsResource(SyncAPIResource):
    @cached_property
    def logs(self) -> LogsResource:
        return LogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self)

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
    ) -> SyncCursorPage[Execution]:
        """
        List executions

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SyncCursorPage[Execution]: OK

        Example:
            ```python
            page = client.machines.executions.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/executions", **{"machine_id": machine_id}),
            page=SyncCursorPage[Execution],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, execution_list_params.ExecutionListParams),
            ),
            model=Execution,
            method="get",
        )

    def create(
        self,
        *,
        machine_id: str,
        command: Optional[SequenceNotStr[str]],
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        stdin: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Execution:
        """
        Create execution

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            command: Body parameter.
            cwd: Body parameter.
            env: Body parameter.
            stdin: Body parameter.
            timeout_ms: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Execution: OK

        Example:
            ```python
            execution = client.machines.executions.create(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                command=[""],
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._post(
            path_template("/v1/machines/{machine_id}/executions", **{"machine_id": machine_id}),
            body=maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "stdin": stdin,
                    "timeout_ms": timeout_ms,
                },
                execution_create_params.ExecutionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Execution,
        )

    def retrieve(
        self,
        *,
        machine_id: str,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Execution:
        """
        Get execution

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Execution: OK

        Example:
            ```python
            execution = client.machines.executions.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Execution,
        )

    def delete(
        self,
        *,
        machine_id: str,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Execution:
        """
        Delete execution

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Execution: OK

        Example:
            ```python
            execution = client.machines.executions.delete(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Execution,
        )

    def output(
        self,
        *,
        machine_id: str,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionOutput:
        """
        Get execution output

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExecutionOutput: OK

        Example:
            ```python
            execution = client.machines.executions.output(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/output",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionOutput,
        )

    def events(
        self,
        *,
        machine_id: str,
        execution_id: str,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[ExecutionEvent]:
        """
        List execution events

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SyncCursorPage[ExecutionEvent]: OK

        Example:
            ```python
            page = client.machines.executions.events(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/events",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            page=SyncCursorPage[ExecutionEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor}, execution_events_params.ExecutionEventsParams
                ),
            ),
            model=ExecutionEvent,
            method="get",
        )


class AsyncExecutionsResource(AsyncAPIResource):
    @cached_property
    def logs(self) -> AsyncLogsResource:
        return AsyncLogsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Execution, AsyncCursorPage[Execution]]:
        """
        List executions

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncPaginator[Execution, AsyncCursorPage[Execution]]: OK

        Example:
            ```python
            page = client.machines.executions.list(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/executions", **{"machine_id": machine_id}),
            page=AsyncCursorPage[Execution],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, execution_list_params.ExecutionListParams),
            ),
            model=Execution,
            method="get",
        )

    async def create(
        self,
        *,
        machine_id: str,
        command: Optional[SequenceNotStr[str]],
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        stdin: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Execution:
        """
        Create execution

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            command: Body parameter.
            cwd: Body parameter.
            env: Body parameter.
            stdin: Body parameter.
            timeout_ms: Body parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Execution: OK

        Example:
            ```python
            execution = await client.machines.executions.create(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                command=[""],
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._post(
            path_template("/v1/machines/{machine_id}/executions", **{"machine_id": machine_id}),
            body=await async_maybe_transform(
                {
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "stdin": stdin,
                    "timeout_ms": timeout_ms,
                },
                execution_create_params.ExecutionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Execution,
        )

    async def retrieve(
        self,
        *,
        machine_id: str,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Execution:
        """
        Get execution

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Execution: OK

        Example:
            ```python
            execution = await client.machines.executions.retrieve(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Execution,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Execution:
        """
        Delete execution

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Execution: OK

        Example:
            ```python
            execution = await client.machines.executions.delete(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Execution,
        )

    async def output(
        self,
        *,
        machine_id: str,
        execution_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExecutionOutput:
        """
        Get execution output

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            ExecutionOutput: OK

        Example:
            ```python
            execution = await client.machines.executions.output(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/output",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExecutionOutput,
        )

    def events(
        self,
        *,
        machine_id: str,
        execution_id: str,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExecutionEvent, AsyncCursorPage[ExecutionEvent]]:
        """
        List execution events

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            limit: Query parameter.
            cursor: Query parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncPaginator[ExecutionEvent, AsyncCursorPage[ExecutionEvent]]: OK

        Example:
            ```python
            page = client.machines.executions.events(
                machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
                execution_id="executionID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if execution_id is None or (isinstance(execution_id, str) and not execution_id):
            raise ValueError(f"Expected a non-empty value for `execution_id` but received {execution_id!r}")
        return self._get_api_list(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/events",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            page=AsyncCursorPage[ExecutionEvent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"limit": limit, "cursor": cursor}, execution_events_params.ExecutionEventsParams
                ),
            ),
            model=ExecutionEvent,
            method="get",
        )


class ExecutionsResourceWithRawResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.list = to_raw_response_wrapper(
            executions.list,
        )
        self.create = to_raw_response_wrapper(
            executions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            executions.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            executions.delete,
        )
        self.output = to_raw_response_wrapper(
            executions.output,
        )
        self.events = to_raw_response_wrapper(
            executions.events,
        )

    @cached_property
    def logs(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self._executions.logs)


class AsyncExecutionsResourceWithRawResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.list = async_to_raw_response_wrapper(
            executions.list,
        )
        self.create = async_to_raw_response_wrapper(
            executions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            executions.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            executions.delete,
        )
        self.output = async_to_raw_response_wrapper(
            executions.output,
        )
        self.events = async_to_raw_response_wrapper(
            executions.events,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self._executions.logs)


class ExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: ExecutionsResource) -> None:
        self._executions = executions

        self.list = to_streamed_response_wrapper(
            executions.list,
        )
        self.create = to_streamed_response_wrapper(
            executions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            executions.delete,
        )
        self.output = to_streamed_response_wrapper(
            executions.output,
        )
        self.events = to_streamed_response_wrapper(
            executions.events,
        )

    @cached_property
    def logs(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self._executions.logs)


class AsyncExecutionsResourceWithStreamingResponse:
    def __init__(self, executions: AsyncExecutionsResource) -> None:
        self._executions = executions

        self.list = async_to_streamed_response_wrapper(
            executions.list,
        )
        self.create = async_to_streamed_response_wrapper(
            executions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            executions.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            executions.delete,
        )
        self.output = async_to_streamed_response_wrapper(
            executions.output,
        )
        self.events = async_to_streamed_response_wrapper(
            executions.events,
        )

    @cached_property
    def logs(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self._executions.logs)
