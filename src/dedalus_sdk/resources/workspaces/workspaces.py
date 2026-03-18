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
from ...types import workspace_list_params, workspace_create_params, workspace_update_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...pagination import SyncWorkspaceList, AsyncWorkspaceList
from ..._base_client import AsyncPaginator, make_request_options
from ...types.workspace import Workspace
from ...types.workspace_list import Item

__all__ = ["WorkspacesResource", "AsyncWorkspacesResource"]


class WorkspacesResource(SyncAPIResource):
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
    def with_raw_response(self) -> WorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return WorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return WorkspacesResourceWithStreamingResponse(self)

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
    ) -> Workspace:
        """
        Create workspace

        Args:
          memory_mib: Memory in MiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/v1/workspaces",
            body=maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                workspace_create_params.WorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Workspace,
        )

    def retrieve(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """
        Get workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return self._get(
            f"/v1/workspaces/{workspace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    def update(
        self,
        workspace_id: str,
        *,
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
    ) -> Workspace:
        """
        Update workspace

        Args:
          memory_mib: Memory in MiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._patch(
            f"/v1/workspaces/{workspace_id}",
            body=maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Workspace,
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
    ) -> SyncWorkspaceList[Item]:
        """
        List workspaces

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/workspaces",
            page=SyncWorkspaceList[Item],
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
                    workspace_list_params.WorkspaceListParams,
                ),
            ),
            model=Item,
        )

    def delete(
        self,
        workspace_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Workspace:
        """
        Destroy workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return self._delete(
            f"/v1/workspaces/{workspace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Workspace,
        )


class AsyncWorkspacesResource(AsyncAPIResource):
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
    def with_raw_response(self) -> AsyncWorkspacesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWorkspacesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorkspacesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dedalus-labs/dedalus-python#with_streaming_response
        """
        return AsyncWorkspacesResourceWithStreamingResponse(self)

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
    ) -> Workspace:
        """
        Create workspace

        Args:
          memory_mib: Memory in MiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/v1/workspaces",
            body=await async_maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                workspace_create_params.WorkspaceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Workspace,
        )

    async def retrieve(
        self,
        workspace_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Workspace:
        """
        Get workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        return await self._get(
            f"/v1/workspaces/{workspace_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Workspace,
        )

    async def update(
        self,
        workspace_id: str,
        *,
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
    ) -> Workspace:
        """
        Update workspace

        Args:
          memory_mib: Memory in MiB.

          vcpu: CPU in vCPUs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._patch(
            f"/v1/workspaces/{workspace_id}",
            body=await async_maybe_transform(
                {
                    "memory_mib": memory_mib,
                    "storage_gib": storage_gib,
                    "vcpu": vcpu,
                },
                workspace_update_params.WorkspaceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Workspace,
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
    ) -> AsyncPaginator[Item, AsyncWorkspaceList[Item]]:
        """
        List workspaces

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/workspaces",
            page=AsyncWorkspaceList[Item],
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
                    workspace_list_params.WorkspaceListParams,
                ),
            ),
            model=Item,
        )

    async def delete(
        self,
        workspace_id: str,
        *,
        if_match: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Workspace:
        """
        Destroy workspace

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not workspace_id:
            raise ValueError(f"Expected a non-empty value for `workspace_id` but received {workspace_id!r}")
        extra_headers = {"If-Match": if_match, **(extra_headers or {})}
        return await self._delete(
            f"/v1/workspaces/{workspace_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Workspace,
        )


class WorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = to_raw_response_wrapper(
            workspaces.create,
        )
        self.retrieve = to_raw_response_wrapper(
            workspaces.retrieve,
        )
        self.update = to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = to_raw_response_wrapper(
            workspaces.list,
        )
        self.delete = to_raw_response_wrapper(
            workspaces.delete,
        )

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithRawResponse:
        return ArtifactsResourceWithRawResponse(self._workspaces.artifacts)

    @cached_property
    def previews(self) -> PreviewsResourceWithRawResponse:
        return PreviewsResourceWithRawResponse(self._workspaces.previews)

    @cached_property
    def ssh(self) -> SSHResourceWithRawResponse:
        return SSHResourceWithRawResponse(self._workspaces.ssh)

    @cached_property
    def executions(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self._workspaces.executions)

    @cached_property
    def terminals(self) -> TerminalsResourceWithRawResponse:
        return TerminalsResourceWithRawResponse(self._workspaces.terminals)


class AsyncWorkspacesResourceWithRawResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = async_to_raw_response_wrapper(
            workspaces.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            workspaces.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_raw_response_wrapper(
            workspaces.list,
        )
        self.delete = async_to_raw_response_wrapper(
            workspaces.delete,
        )

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithRawResponse:
        return AsyncArtifactsResourceWithRawResponse(self._workspaces.artifacts)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithRawResponse:
        return AsyncPreviewsResourceWithRawResponse(self._workspaces.previews)

    @cached_property
    def ssh(self) -> AsyncSSHResourceWithRawResponse:
        return AsyncSSHResourceWithRawResponse(self._workspaces.ssh)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self._workspaces.executions)

    @cached_property
    def terminals(self) -> AsyncTerminalsResourceWithRawResponse:
        return AsyncTerminalsResourceWithRawResponse(self._workspaces.terminals)


class WorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: WorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = to_streamed_response_wrapper(
            workspaces.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            workspaces.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = to_streamed_response_wrapper(
            workspaces.list,
        )
        self.delete = to_streamed_response_wrapper(
            workspaces.delete,
        )

    @cached_property
    def artifacts(self) -> ArtifactsResourceWithStreamingResponse:
        return ArtifactsResourceWithStreamingResponse(self._workspaces.artifacts)

    @cached_property
    def previews(self) -> PreviewsResourceWithStreamingResponse:
        return PreviewsResourceWithStreamingResponse(self._workspaces.previews)

    @cached_property
    def ssh(self) -> SSHResourceWithStreamingResponse:
        return SSHResourceWithStreamingResponse(self._workspaces.ssh)

    @cached_property
    def executions(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self._workspaces.executions)

    @cached_property
    def terminals(self) -> TerminalsResourceWithStreamingResponse:
        return TerminalsResourceWithStreamingResponse(self._workspaces.terminals)


class AsyncWorkspacesResourceWithStreamingResponse:
    def __init__(self, workspaces: AsyncWorkspacesResource) -> None:
        self._workspaces = workspaces

        self.create = async_to_streamed_response_wrapper(
            workspaces.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            workspaces.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            workspaces.update,
        )
        self.list = async_to_streamed_response_wrapper(
            workspaces.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            workspaces.delete,
        )

    @cached_property
    def artifacts(self) -> AsyncArtifactsResourceWithStreamingResponse:
        return AsyncArtifactsResourceWithStreamingResponse(self._workspaces.artifacts)

    @cached_property
    def previews(self) -> AsyncPreviewsResourceWithStreamingResponse:
        return AsyncPreviewsResourceWithStreamingResponse(self._workspaces.previews)

    @cached_property
    def ssh(self) -> AsyncSSHResourceWithStreamingResponse:
        return AsyncSSHResourceWithStreamingResponse(self._workspaces.ssh)

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._workspaces.executions)

    @cached_property
    def terminals(self) -> AsyncTerminalsResourceWithStreamingResponse:
        return AsyncTerminalsResourceWithStreamingResponse(self._workspaces.terminals)
