# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.types import Workspace
from dedalus_sdk.pagination import SyncWorkspaceList, AsyncWorkspaceList
from dedalus_sdk.types.workspace_list import Item

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspaces:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dedalus) -> None:
        workspace = client.workspaces.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dedalus) -> None:
        response = client.workspaces.with_raw_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dedalus) -> None:
        with client.workspaces.with_streaming_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        workspace = client.workspaces.retrieve(
            "workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.workspaces.with_raw_response.retrieve(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.workspaces.with_streaming_response.retrieve(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Dedalus) -> None:
        workspace = client.workspaces.update(
            workspace_id="workspace_id",
            if_match="If-Match",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dedalus) -> None:
        workspace = client.workspaces.update(
            workspace_id="workspace_id",
            if_match="If-Match",
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dedalus) -> None:
        response = client.workspaces.with_raw_response.update(
            workspace_id="workspace_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Dedalus) -> None:
        with client.workspaces.with_streaming_response.update(
            workspace_id="workspace_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.update(
                workspace_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        workspace = client.workspaces.list()
        assert_matches_type(SyncWorkspaceList[Item], workspace, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        workspace = client.workspaces.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncWorkspaceList[Item], workspace, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(SyncWorkspaceList[Item], workspace, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(SyncWorkspaceList[Item], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        workspace = client.workspaces.delete(
            workspace_id="workspace_id",
            if_match="If-Match",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.workspaces.with_raw_response.delete(
            workspace_id="workspace_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.workspaces.with_streaming_response.delete(
            workspace_id="workspace_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.with_raw_response.delete(
                workspace_id="",
                if_match="If-Match",
            )


class TestAsyncWorkspaces:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.with_raw_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.with_streaming_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.retrieve(
            "workspace_id",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.with_raw_response.retrieve(
            "workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.with_streaming_response.retrieve(
            "workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.update(
            workspace_id="workspace_id",
            if_match="If-Match",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.update(
            workspace_id="workspace_id",
            if_match="If-Match",
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.with_raw_response.update(
            workspace_id="workspace_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.with_streaming_response.update(
            workspace_id="workspace_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.update(
                workspace_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.list()
        assert_matches_type(AsyncWorkspaceList[Item], workspace, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncWorkspaceList[Item], workspace, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(AsyncWorkspaceList[Item], workspace, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(AsyncWorkspaceList[Item], workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        workspace = await async_client.workspaces.delete(
            workspace_id="workspace_id",
            if_match="If-Match",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.with_raw_response.delete(
            workspace_id="workspace_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.with_streaming_response.delete(
            workspace_id="workspace_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.with_raw_response.delete(
                workspace_id="",
                if_match="If-Match",
            )
