# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform, strip_not_given
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
from ..._streaming import Stream, AsyncStream
from .network import (
    NetworkResource,
    AsyncNetworkResource,
    NetworkResourceWithRawResponse,
    AsyncNetworkResourceWithRawResponse,
    NetworkResourceWithStreamingResponse,
    AsyncNetworkResourceWithStreamingResponse,
)
from .artifacts import (
    ArtifactsResource,
    AsyncArtifactsResource,
    ArtifactsResourceWithRawResponse,
    AsyncArtifactsResourceWithRawResponse,
    ArtifactsResourceWithStreamingResponse,
    AsyncArtifactsResourceWithStreamingResponse,
)
from .ports import (
    PortsResource,
    AsyncPortsResource,
    PortsResourceWithRawResponse,
    AsyncPortsResourceWithRawResponse,
    PortsResourceWithStreamingResponse,
    AsyncPortsResourceWithStreamingResponse,
)
from .ssh import (
    SSHResource,
    AsyncSSHResource,
    SSHResourceWithRawResponse,
    AsyncSSHResourceWithRawResponse,
    SSHResourceWithStreamingResponse,
    AsyncSSHResourceWithStreamingResponse,
)
from .executions import (
    ExecutionsResource,
    AsyncExecutionsResource,
    ExecutionsResourceWithRawResponse,
    AsyncExecutionsResourceWithRawResponse,
    ExecutionsResourceWithStreamingResponse,
    AsyncExecutionsResourceWithStreamingResponse,
)
from .terminals import (
    TerminalsResource,
    AsyncTerminalsResource,
    TerminalsResourceWithRawResponse,
    AsyncTerminalsResourceWithRawResponse,
    TerminalsResourceWithStreamingResponse,
    AsyncTerminalsResourceWithStreamingResponse,
)
from ...types import machine_list_params, machine_create_params, machine_update_params
from ...types.machine_list_item import MachineListItem
from ...types.machine import Machine
from ...types.machine_retrieve_response import MachineRetrieveResponse

__all__ = ["MachinesResource", "AsyncMachinesResource"]


class MachinesResource(SyncAPIResource):
    @cached_property
    def network(self) -> NetworkResource:
        return NetworkResource(self._client)

    @cached_property
    def artifacts(self) -> ArtifactsResource:
        return ArtifactsResource(self._client)

    @cached_property
    def ports(self) -> PortsResource:
        return PortsResource(self._client)

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
        return MachinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MachinesResourceWithStreamingResponse:
        return MachinesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
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
            limit: Query parameter.
            cursor: Query parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            SyncCursorPage[MachineListItem]: OK

        Example:
            ```python
            page = client.machines.list()
            ```
        """
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            "/v1/machines",
            page=SyncCursorPage[MachineListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, machine_list_params.MachineListParams),
            ),
            model=MachineListItem,
            method="get",
        )

    def create(
        self,
        *,
        autosleep: str | Omit = omit,
        memory_mib: int | Omit = omit,
        storage_gib: int | Omit = omit,
        vcpu: float | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
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
            autosleep: Idle window before autosleep. Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds ("1800"), or never to disable.
            memory_mib: Memory in MiB.
            storage_gib: Storage in GiB.
            vcpu: CPU in vCPUs.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: Create converged inline

        Example:
            ```python
            machine = client.machines.create(
                autosleep="300s",
                memory_mib=4096,
                storage_gib=10,
                vcpu=1,
                idempotency_key="",
            )
            ```
        """
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._post(
            "/v1/machines",
            body=maybe_transform(
                {
                    "autosleep": autosleep,
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
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineRetrieveResponse:
        """
        Get machine

        Args:
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineRetrieveResponse: OK

        Example:
            ```python
            machine = client.machines.retrieve(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get(
            path_template("/v1/machines/{machine_id}", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MachineRetrieveResponse,
        )

    def update(
        self,
        *,
        machine_id: str,
        autosleep: str | Omit = omit,
        memory_mib: int | Omit = omit,
        storage_gib: int | Omit = omit,
        vcpu: float | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            autosleep: Idle window before autosleep. Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds ("1800"), or never to disable.
            memory_mib: Memory in MiB.
            storage_gib: Storage in GiB.
            vcpu: CPU in vCPUs.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = client.machines.update(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._patch(
            path_template("/v1/machines/{machine_id}", **{"machine_id": machine_id}),
            body=maybe_transform(
                {
                    "autosleep": autosleep,
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

    def delete(
        self,
        *,
        machine_id: str,
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = client.machines.delete(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._delete(
            path_template("/v1/machines/{machine_id}", **{"machine_id": machine_id}),
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
        x_dedalus_org_id: str | Omit = omit,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[Machine]:
        """
        Streams machine lifecycle updates over Server-Sent Events. Each `status` event contains a full `LifecycleResponse` payload. The stream closes after the machine reaches its current desired state.

        Args:
            machine_id: Machine identifier.
            x_dedalus_org_id: Organization ID header applied to all DCS requests.
            last_event_id: Optional resourceVersion bookmark used to resume a previous stream.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Stream[Machine]: Server-Sent Event stream (`text/event-stream`) of machine lifecycle updates.

        Example:
            ```python
            stream = client.machines.watch(
                machine_id="machineID",
            )

            for machine in stream:
                print(machine)
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {
            **strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id, "Last-Event-ID": last_event_id}),
            **(extra_headers or {}),
        }
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            path_template("/v1/machines/{machine_id}/status/stream", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Machine,
            stream=True,
            stream_cls=Stream[Machine],
        )

    def sleep(
        self,
        *,
        machine_id: str,
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = client.machines.sleep(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/machines/{machine_id}/sleep", **{"machine_id": machine_id}),
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
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = client.machines.wake(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._post(
            path_template("/v1/machines/{machine_id}/wake", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )


class AsyncMachinesResource(AsyncAPIResource):
    @cached_property
    def network(self) -> AsyncNetworkResource:
        return AsyncNetworkResource(self._client)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResource:
        return AsyncArtifactsResource(self._client)

    @cached_property
    def ports(self) -> AsyncPortsResource:
        return AsyncPortsResource(self._client)

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
        return AsyncMachinesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMachinesResourceWithStreamingResponse:
        return AsyncMachinesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        cursor: str | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
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
            limit: Query parameter.
            cursor: Query parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncPaginator[MachineListItem, AsyncCursorPage[MachineListItem]]: OK

        Example:
            ```python
            page = client.machines.list()
            ```
        """
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            "/v1/machines",
            page=AsyncCursorPage[MachineListItem],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, machine_list_params.MachineListParams),
            ),
            model=MachineListItem,
            method="get",
        )

    async def create(
        self,
        *,
        autosleep: str | Omit = omit,
        memory_mib: int | Omit = omit,
        storage_gib: int | Omit = omit,
        vcpu: float | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
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
            autosleep: Idle window before autosleep. Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds ("1800"), or never to disable.
            memory_mib: Memory in MiB.
            storage_gib: Storage in GiB.
            vcpu: CPU in vCPUs.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: Create converged inline

        Example:
            ```python
            machine = await client.machines.create(
                autosleep="300s",
                memory_mib=4096,
                storage_gib=10,
                vcpu=1,
                idempotency_key="",
            )
            ```
        """
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._post(
            "/v1/machines",
            body=await async_maybe_transform(
                {
                    "autosleep": autosleep,
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
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MachineRetrieveResponse:
        """
        Get machine

        Args:
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            MachineRetrieveResponse: OK

        Example:
            ```python
            machine = await client.machines.retrieve(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._get(
            path_template("/v1/machines/{machine_id}", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MachineRetrieveResponse,
        )

    async def update(
        self,
        *,
        machine_id: str,
        autosleep: str | Omit = omit,
        memory_mib: int | Omit = omit,
        storage_gib: int | Omit = omit,
        vcpu: float | Omit = omit,
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            autosleep: Idle window before autosleep. Accepts fixed duration units like 30s, 30m, 2h, 7d3h4s, or 1w3d, raw seconds ("1800"), or never to disable.
            memory_mib: Memory in MiB.
            storage_gib: Storage in GiB.
            vcpu: CPU in vCPUs.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = await client.machines.update(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._patch(
            path_template("/v1/machines/{machine_id}", **{"machine_id": machine_id}),
            body=await async_maybe_transform(
                {
                    "autosleep": autosleep,
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

    async def delete(
        self,
        *,
        machine_id: str,
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = await client.machines.delete(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/machines/{machine_id}", **{"machine_id": machine_id}),
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
        x_dedalus_org_id: str | Omit = omit,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[Machine]:
        """
        Streams machine lifecycle updates over Server-Sent Events. Each `status` event contains a full `LifecycleResponse` payload. The stream closes after the machine reaches its current desired state.

        Args:
            machine_id: Machine identifier.
            x_dedalus_org_id: Organization ID header applied to all DCS requests.
            last_event_id: Optional resourceVersion bookmark used to resume a previous stream.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            AsyncStream[Machine]: Server-Sent Event stream (`text/event-stream`) of machine lifecycle updates.

        Example:
            ```python
            stream = await client.machines.watch(
                machine_id="machineID",
            )

            async for machine in stream:
                print(machine)
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {
            **strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id, "Last-Event-ID": last_event_id}),
            **(extra_headers or {}),
        }
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/machines/{machine_id}/status/stream", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Machine,
            stream=True,
            stream_cls=AsyncStream[Machine],
        )

    async def sleep(
        self,
        *,
        machine_id: str,
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = await client.machines.sleep(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/machines/{machine_id}/sleep", **{"machine_id": machine_id}),
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
        x_dedalus_org_id: str | Omit = omit,
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
            machine_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Machine: OK

        Example:
            ```python
            machine = await client.machines.wake(
                machine_id="machineID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._post(
            path_template("/v1/machines/{machine_id}/wake", **{"machine_id": machine_id}),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Machine,
        )


class MachinesResourceWithRawResponse:
    def __init__(self, machines: MachinesResource) -> None:
        self._machines = machines

        self.list = to_raw_response_wrapper(
            machines.list,
        )
        self.create = to_raw_response_wrapper(
            machines.create,
        )
        self.retrieve = to_raw_response_wrapper(
            machines.retrieve,
        )
        self.update = to_raw_response_wrapper(
            machines.update,
        )
        self.delete = to_raw_response_wrapper(
            machines.delete,
        )
        self.watch = to_raw_response_wrapper(
            machines.watch,
        )
        self.sleep = to_raw_response_wrapper(
            machines.sleep,
        )
        self.wake = to_raw_response_wrapper(
            machines.wake,
        )

    @cached_property
    def network(self) -> NetworkResourceWithRawResponse:
        return NetworkResourceWithRawResponse(self._machines.network)

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self._machines.artifacts)

    @cached_property
    def ports(self) -> PortsResourceWithRawResponse:
        return PortsResourceWithRawResponse(self._machines.ports)

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

        self.list = async_to_raw_response_wrapper(
            machines.list,
        )
        self.create = async_to_raw_response_wrapper(
            machines.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            machines.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            machines.update,
        )
        self.delete = async_to_raw_response_wrapper(
            machines.delete,
        )
        self.watch = async_to_raw_response_wrapper(
            machines.watch,
        )
        self.sleep = async_to_raw_response_wrapper(
            machines.sleep,
        )
        self.wake = async_to_raw_response_wrapper(
            machines.wake,
        )

    @cached_property
    def network(self) -> AsyncNetworkResourceWithRawResponse:
        return AsyncNetworkResourceWithRawResponse(self._machines.network)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self._machines.artifacts)

    @cached_property
    def ports(self) -> AsyncPortsResourceWithRawResponse:
        return AsyncPortsResourceWithRawResponse(self._machines.ports)

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

        self.list = to_streamed_response_wrapper(
            machines.list,
        )
        self.create = to_streamed_response_wrapper(
            machines.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            machines.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            machines.update,
        )
        self.delete = to_streamed_response_wrapper(
            machines.delete,
        )
        self.watch = to_streamed_response_wrapper(
            machines.watch,
        )
        self.sleep = to_streamed_response_wrapper(
            machines.sleep,
        )
        self.wake = to_streamed_response_wrapper(
            machines.wake,
        )

    @cached_property
    def network(self) -> NetworkResourceWithStreamingResponse:
        return NetworkResourceWithStreamingResponse(self._machines.network)

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self._machines.artifacts)

    @cached_property
    def ports(self) -> PortsResourceWithStreamingResponse:
        return PortsResourceWithStreamingResponse(self._machines.ports)

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

        self.list = async_to_streamed_response_wrapper(
            machines.list,
        )
        self.create = async_to_streamed_response_wrapper(
            machines.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            machines.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            machines.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            machines.delete,
        )
        self.watch = async_to_streamed_response_wrapper(
            machines.watch,
        )
        self.sleep = async_to_streamed_response_wrapper(
            machines.sleep,
        )
        self.wake = async_to_streamed_response_wrapper(
            machines.wake,
        )

    @cached_property
    def network(self) -> AsyncNetworkResourceWithStreamingResponse:
        return AsyncNetworkResourceWithStreamingResponse(self._machines.network)

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self._machines.artifacts)

    @cached_property
    def ports(self) -> AsyncPortsResourceWithStreamingResponse:
        return AsyncPortsResourceWithStreamingResponse(self._machines.ports)

    @cached_property
    def ssh(self) -> AsyncSSHResourceWithStreamingResponse:
        return AsyncSSHResourceWithStreamingResponse(self._machines.ssh)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._machines.executions)

    @cached_property
    def terminals(self) -> AsyncTerminalsResourceWithStreamingResponse:
        return AsyncTerminalsResourceWithStreamingResponse(self._machines.terminals)
