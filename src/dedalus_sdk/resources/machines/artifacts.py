# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, strip_not_given
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
from ...types.machines import artifact_list_params
from ...types.machines.artifact import Artifact

__all__ = ["ArtifactsResource", "AsyncArtifactsResource"]


class ArtifactsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self)

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
    ) -> SyncCursorPage[Artifact]:
        """
        List artifacts

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
            SyncCursorPage[Artifact]: OK

        Example:
            ```python
            page = client.machines.artifacts.list(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/artifacts", **{"machine_id": machine_id}),
            page=SyncCursorPage[Artifact],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, artifact_list_params.ArtifactListParams),
            ),
            model=Artifact,
            method="get",
        )

    def retrieve(
        self,
        *,
        machine_id: str,
        artifact_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Artifact:
        """
        Get artifact

        Args:
            machine_id: Path parameter.
            artifact_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Artifact: OK

        Example:
            ```python
            artifact = client.machines.artifacts.retrieve(
                machine_id="machineID",
                artifact_id="artifactID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get(
            path_template(
                "/v1/machines/{machine_id}/artifacts/{artifact_id}",
                **{"machine_id": machine_id, "artifact_id": artifact_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Artifact,
        )

    def delete(
        self,
        *,
        machine_id: str,
        artifact_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Artifact:
        """
        Delete artifact

        Args:
            machine_id: Path parameter.
            artifact_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Artifact: OK

        Example:
            ```python
            artifact = client.machines.artifacts.delete(
                machine_id="machineID",
                artifact_id="artifactID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/machines/{machine_id}/artifacts/{artifact_id}",
                **{"machine_id": machine_id, "artifact_id": artifact_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Artifact,
        )


class AsyncArtifactsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self)

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
    ) -> AsyncPaginator[Artifact, AsyncCursorPage[Artifact]]:
        """
        List artifacts

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
            AsyncPaginator[Artifact, AsyncCursorPage[Artifact]]: OK

        Example:
            ```python
            page = client.machines.artifacts.list(
                machine_id="machineID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return self._get_api_list(
            path_template("/v1/machines/{machine_id}/artifacts", **{"machine_id": machine_id}),
            page=AsyncCursorPage[Artifact],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit, "cursor": cursor}, artifact_list_params.ArtifactListParams),
            ),
            model=Artifact,
            method="get",
        )

    async def retrieve(
        self,
        *,
        machine_id: str,
        artifact_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Artifact:
        """
        Get artifact

        Args:
            machine_id: Path parameter.
            artifact_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.

        Returns:
            Artifact: OK

        Example:
            ```python
            artifact = await client.machines.artifacts.retrieve(
                machine_id="machineID",
                artifact_id="artifactID",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v1/machines/{machine_id}/artifacts/{artifact_id}",
                **{"machine_id": machine_id, "artifact_id": artifact_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Artifact,
        )

    async def delete(
        self,
        *,
        machine_id: str,
        artifact_id: str,
        x_dedalus_org_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Artifact:
        """
        Delete artifact

        Args:
            machine_id: Path parameter.
            artifact_id: Path parameter.
            x_dedalus_org_id: Header parameter.
            extra_headers: Send extra headers with the request.
            extra_query: Send extra query parameters with the request.
            extra_body: Send extra JSON properties with the request.
            timeout: Override the client-level default timeout for this request, in seconds.
            idempotency_key: Override or provide the idempotency key for this request.

        Returns:
            Artifact: OK

        Example:
            ```python
            artifact = await client.machines.artifacts.delete(
                machine_id="machineID",
                artifact_id="artifactID",
                idempotency_key="",
            )
            ```
        """
        if machine_id is None or (isinstance(machine_id, str) and not machine_id):
            raise ValueError(f"Expected a non-empty value for `machine_id` but received {machine_id!r}")
        if artifact_id is None or (isinstance(artifact_id, str) and not artifact_id):
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {**strip_not_given({"X-Dedalus-Org-Id": x_dedalus_org_id}), **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/machines/{machine_id}/artifacts/{artifact_id}",
                **{"machine_id": machine_id, "artifact_id": artifact_id},
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Artifact,
        )


class ArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = to_raw_response_wrapper(
            artifacts.list,
        )
        self.retrieve = to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            artifacts.delete,
        )


class AsyncArtifactsResourceWithRawResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = async_to_raw_response_wrapper(
            artifacts.list,
        )
        self.retrieve = async_to_raw_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            artifacts.delete,
        )


class ArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: ArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = to_streamed_response_wrapper(
            artifacts.list,
        )
        self.retrieve = to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            artifacts.delete,
        )


class AsyncArtifactsResourceWithStreamingResponse:
    def __init__(self, artifacts: AsyncArtifactsResource) -> None:
        self._artifacts = artifacts

        self.list = async_to_streamed_response_wrapper(
            artifacts.list,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            artifacts.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            artifacts.delete,
        )
