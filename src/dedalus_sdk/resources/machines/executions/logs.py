# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._utils import path_template
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.machines.executions.status import Status
from ....types.machines.executions.read_token import ReadToken

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        return LogsResourceWithStreamingResponse(self)

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
    ) -> Status:
        """
        Get execution log status

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Status: OK

        Example:
            ```python
            log = client.machines.executions.logs.retrieve(
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
                "/v1/machines/{machine_id}/executions/{execution_id}/logs",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Status,
        )

    def reauthorize(
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
    ) -> Status:
        """
        Reauthorize execution log publication

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Status: OK

        Example:
            ```python
            log = client.machines.executions.logs.reauthorize(
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
        return self._post(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/logs/reauthorize",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Status,
        )

    def create_token(
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
    ) -> ReadToken:
        """
        Create execution log read token

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            ReadToken: OK

        Example:
            ```python
            log = client.machines.executions.logs.create_token(
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
        return self._post(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/logs/token",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ReadToken,
        )


class AsyncLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        return AsyncLogsResourceWithStreamingResponse(self)

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
    ) -> Status:
        """
        Get execution log status

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Status: OK

        Example:
            ```python
            log = await client.machines.executions.logs.retrieve(
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
                "/v1/machines/{machine_id}/executions/{execution_id}/logs",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Status,
        )

    async def reauthorize(
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
    ) -> Status:
        """
        Reauthorize execution log publication

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Status: OK

        Example:
            ```python
            log = await client.machines.executions.logs.reauthorize(
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
        return await self._post(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/logs/reauthorize",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Status,
        )

    async def create_token(
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
    ) -> ReadToken:
        """
        Create execution log read token

        Args:
            machine_id: Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged.
            execution_id: Path parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            ReadToken: OK

        Example:
            ```python
            log = await client.machines.executions.logs.create_token(
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
        return await self._post(
            path_template(
                "/v1/machines/{machine_id}/executions/{execution_id}/logs/token",
                **{"machine_id": machine_id, "execution_id": execution_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ReadToken,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.retrieve = to_raw_response_wrapper(
            logs.retrieve,
        )
        self.reauthorize = to_raw_response_wrapper(
            logs.reauthorize,
        )
        self.create_token = to_raw_response_wrapper(
            logs.create_token,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.retrieve = async_to_raw_response_wrapper(
            logs.retrieve,
        )
        self.reauthorize = async_to_raw_response_wrapper(
            logs.reauthorize,
        )
        self.create_token = async_to_raw_response_wrapper(
            logs.create_token,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.retrieve = to_streamed_response_wrapper(
            logs.retrieve,
        )
        self.reauthorize = to_streamed_response_wrapper(
            logs.reauthorize,
        )
        self.create_token = to_streamed_response_wrapper(
            logs.create_token,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.retrieve = async_to_streamed_response_wrapper(
            logs.retrieve,
        )
        self.reauthorize = async_to_streamed_response_wrapper(
            logs.reauthorize,
        )
        self.create_token = async_to_streamed_response_wrapper(
            logs.create_token,
        )
