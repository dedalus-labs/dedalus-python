# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .ssh import (
    SSHResource,
    AsyncSSHResource,
    SSHResourceWithRawResponse,
    AsyncSSHResourceWithRawResponse,
    SSHResourceWithStreamingResponse,
    AsyncSSHResourceWithStreamingResponse,
)
from ...types import machine_list_params, machine_create_params, machine_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from .previews import (
    PreviewsResource,
    AsyncPreviewsResource,
    PreviewsResourceWithRawResponse,
    AsyncPreviewsResourceWithRawResponse,
    PreviewsResourceWithStreamingResponse,
    AsyncPreviewsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .artifacts import (
    ArtifactsResource,
    AsyncArtifactsResource,
    ArtifactsResourceWithRawResponse,
    AsyncArtifactsResourceWithRawResponse,
    ArtifactsResourceWithStreamingResponse,
    AsyncArtifactsResourceWithStreamingResponse,
)
from .terminals import (
    TerminalsResource,
    AsyncTerminalsResource,
    TerminalsResourceWithRawResponse,
    AsyncTerminalsResourceWithRawResponse,
    TerminalsResourceWithStreamingResponse,
    AsyncTerminalsResourceWithStreamingResponse,
)
from .executions import (
    ExecutionsResource,
    AsyncExecutionsResource,
    ExecutionsResourceWithRawResponse,
    AsyncExecutionsResourceWithRawResponse,
    ExecutionsResourceWithStreamingResponse,
    AsyncExecutionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.machine import Machine
from ...types.machine_list_item import MachineListItem

__all__ = ["MachinesResource", "AsyncMachinesResource"]


class MachinesResource(SyncAPIResource):
    @cached_property
    def artifacts(self) -> ArtifactsResource:
        return ArtifactsResource(self._client)

    @cached_property
    def previews(self) -> PreviewsResource:
        return PreviewsResource(self._client)

    @cached_property
    def ssh(self) -> SSHResource:
        return SSHResource(self._client)

    @cached_property
    def executions(self) -> ExecutionsResource:
        return ExecutionsResource(self._client)

    @cached_property
    def terminals(self) -> TerminalsResource:
        return TerminalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MachinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return MachinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MachinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return MachinesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        memory_mib: int,
        storage_gib: int,
        vcpu: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Create machine

        Args:
          memory_mib: Memory in MiB.

          storage_gib: Storage in GiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/v1/machines",
            body=maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                machine_create_params.MachineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    def retrieve(
        self,
        *,
        machine_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Machine:
        """
        Get machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return self._get(
            path_template("/v1/machines/{machine_id}", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Machine,
        )

    def update(
        self,
        *,
        machine_id: str,
        if_match: str,
        memory_mib: int | Omit = omit,
        storage_gib: int | Omit = omit,
        vcpu: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Update machine

        Args:
          memory_mib: Memory in MiB.

          storage_gib: Storage in GiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._patch(
            path_template("/v1/machines/{machine_id}", machine_id=machine_id),
            body=maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                machine_update_params.MachineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MachineListItem]:
        """
        List machines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/machines",
            page=SyncCursorPage[MachineListItem],
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
                    machine_list_params.MachineListParams,
                ),
            ),
            model=MachineListItem,
        )

    def delete(
        self,
        *,
        machine_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Destroy machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._delete(
            path_template("/v1/machines/{machine_id}", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    def sleep(
        self,
        *,
        machine_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Sleep a running machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/v1/machines/{machine_id}/sleep", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    def wake(
        self,
        *,
        machine_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Wake a sleeping machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._post(
            path_template("/v1/machines/{machine_id}/wake", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    def watch(
        self,
        *,
        machine_id: str,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[Machine]:
        """Streams machine lifecycle updates over Server-Sent Events.

        Each `status` event
        contains a full `LifecycleResponse` payload. The stream closes after the machine
        reaches its current desired state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Last-Event-ID": last_event_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/machines/{machine_id}/status/stream", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Machine,
            stream=True,
            stream_cls=Stream[Machine],
        )


class AsyncMachinesResource(AsyncAPIResource):
    @cached_property
    def artifacts(self) -> AsyncArtifactsResource:
        return AsyncArtifactsResource(self._client)

    @cached_property
    def previews(self) -> AsyncPreviewsResource:
        return AsyncPreviewsResource(self._client)

    @cached_property
    def ssh(self) -> AsyncSSHResource:
        return AsyncSSHResource(self._client)

    @cached_property
    def executions(self) -> AsyncExecutionsResource:
        return AsyncExecutionsResource(self._client)

    @cached_property
    def terminals(self) -> AsyncTerminalsResource:
        return AsyncTerminalsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMachinesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMachinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMachinesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return AsyncMachinesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        memory_mib: int,
        storage_gib: int,
        vcpu: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Create machine

        Args:
          memory_mib: Memory in MiB.

          storage_gib: Storage in GiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/v1/machines",
            body=await async_maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                machine_create_params.MachineCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    async def retrieve(
        self,
        *,
        machine_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Machine:
        """
        Get machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        return await self._get(
            path_template("/v1/machines/{machine_id}", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Machine,
        )

    async def update(
        self,
        *,
        machine_id: str,
        if_match: str,
        memory_mib: int | Omit = omit,
        storage_gib: int | Omit = omit,
        vcpu: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Update machine

        Args:
          memory_mib: Memory in MiB.

          storage_gib: Storage in GiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/machines/{machine_id}", machine_id=machine_id),
            body=await async_maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                machine_update_params.MachineUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MachineListItem, AsyncCursorPage[MachineListItem]]:
        """
        List machines

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/machines",
            page=AsyncCursorPage[MachineListItem],
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
                    machine_list_params.MachineListParams,
                ),
            ),
            model=MachineListItem,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Destroy machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/machines/{machine_id}", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    async def sleep(
        self,
        *,
        machine_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Sleep a running machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/v1/machines/{machine_id}/sleep", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    async def wake(
        self,
        *,
        machine_id: str,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Machine:
        """
        Wake a sleeping machine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._post(
            path_template("/v1/machines/{machine_id}/wake", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )

    async def watch(
        self,
        *,
        machine_id: str,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[Machine]:
        """Streams machine lifecycle updates over Server-Sent Events.

        Each `status` event
        contains a full `LifecycleResponse` payload. The stream closes after the machine
        reaches its current desired state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not machine_id:
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Last-Event-ID": last_event_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/machines/{machine_id}/status/stream", machine_id=machine_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Machine,
            stream=True,
            stream_cls=AsyncStream[Machine],
        )


class MachinesResourceWithRawResponse:
    def __init__(self, machines: MachinesResource) -> None:
        self._machines = machines

        self.create = to_raw_response_wrapper(
            machines.create,
        )
        self.retrieve = to_raw_response_wrapper(
            machines.retrieve,
        )
        self.update = to_raw_response_wrapper(
            machines.update,
        )
        self.list = to_raw_response_wrapper(
            machines.list,
        )
        self.delete = to_raw_response_wrapper(
            machines.delete,
        )
        self.sleep = to_raw_response_wrapper(
            machines.sleep,
        )
        self.wake = to_raw_response_wrapper(
            machines.wake,
        )
        self.watch = to_raw_response_wrapper(
            machines.watch,
        )

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self._machines.artifacts)

    @cached_property
    def previews(self) -> PreviewsResourceWithRawResponse:
        return PreviewsResourceWithRawResponse(self._machines.previews)

    @cached_property
    def ssh(self) -> SSHResourceWithRawResponse:
        return SSHResourceWithRawResponse(self._machines.ssh)

    @cached_property
    def executions(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self._machines.executions)

    @cached_property
    def terminals(self) -> TerminalsResourceWithRawResponse:
        return TerminalsResourceWithRawResponse(self._machines.terminals)


class AsyncMachinesResourceWithRawResponse:
    def __init__(self, machines: AsyncMachinesResource) -> None:
        self._machines = machines

        self.create = async_to_raw_response_wrapper(
            machines.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            machines.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            machines.update,
        )
        self.list = async_to_raw_response_wrapper(
            machines.list,
        )
        self.delete = async_to_raw_response_wrapper(
            machines.delete,
        )
        self.sleep = async_to_raw_response_wrapper(
            machines.sleep,
        )
        self.wake = async_to_raw_response_wrapper(
            machines.wake,
        )
        self.watch = async_to_raw_response_wrapper(
            machines.watch,
        )

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self._machines.artifacts)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithRawResponse:
        return AsyncPreviewsResourceWithRawResponse(self._machines.previews)

    @cached_property
    def ssh(self) -> AsyncSSHResourceWithRawResponse:
        return AsyncSSHResourceWithRawResponse(self._machines.ssh)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self._machines.executions)

    @cached_property
    def terminals(self) -> AsyncTerminalsResourceWithRawResponse:
        return AsyncTerminalsResourceWithRawResponse(self._machines.terminals)


class MachinesResourceWithStreamingResponse:
    def __init__(self, machines: MachinesResource) -> None:
        self._machines = machines

        self.create = to_streamed_response_wrapper(
            machines.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            machines.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            machines.update,
        )
        self.list = to_streamed_response_wrapper(
            machines.list,
        )
        self.delete = to_streamed_response_wrapper(
            machines.delete,
        )
        self.sleep = to_streamed_response_wrapper(
            machines.sleep,
        )
        self.wake = to_streamed_response_wrapper(
            machines.wake,
        )
        self.watch = to_streamed_response_wrapper(
            machines.watch,
        )

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self._machines.artifacts)

    @cached_property
    def previews(self) -> PreviewsResourceWithStreamingResponse:
        return PreviewsResourceWithStreamingResponse(self._machines.previews)

    @cached_property
    def ssh(self) -> SSHResourceWithStreamingResponse:
        return SSHResourceWithStreamingResponse(self._machines.ssh)

    @cached_property
    def executions(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self._machines.executions)

    @cached_property
    def terminals(self) -> TerminalsResourceWithStreamingResponse:
        return TerminalsResourceWithStreamingResponse(self._machines.terminals)


class AsyncMachinesResourceWithStreamingResponse:
    def __init__(self, machines: AsyncMachinesResource) -> None:
        self._machines = machines

        self.create = async_to_streamed_response_wrapper(
            machines.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            machines.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            machines.update,
        )
        self.list = async_to_streamed_response_wrapper(
            machines.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            machines.delete,
        )
        self.sleep = async_to_streamed_response_wrapper(
            machines.sleep,
        )
        self.wake = async_to_streamed_response_wrapper(
            machines.wake,
        )
        self.watch = async_to_streamed_response_wrapper(
            machines.watch,
        )

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self._machines.artifacts)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithStreamingResponse:
        return AsyncPreviewsResourceWithStreamingResponse(self._machines.previews)

    @cached_property
    def ssh(self) -> AsyncSSHResourceWithStreamingResponse:
        return AsyncSSHResourceWithStreamingResponse(self._machines.ssh)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._machines.executions)

    @cached_property
    def terminals(self) -> AsyncTerminalsResourceWithStreamingResponse:
        return AsyncTerminalsResourceWithStreamingResponse(self._machines.terminals)
