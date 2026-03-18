# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.pagination import SyncArtifactList, AsyncArtifactList
from dedalus_sdk.types.workspaces import Artifact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        artifact = client.workspaces.artifacts.retrieve(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.workspaces.artifacts.with_raw_response.retrieve(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.workspaces.artifacts.with_streaming_response.retrieve(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.artifacts.with_raw_response.retrieve(
                artifact_id="artifact_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.workspaces.artifacts.with_raw_response.retrieve(
                artifact_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        artifact = client.workspaces.artifacts.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncArtifactList[Artifact], artifact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        artifact = client.workspaces.artifacts.list(
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncArtifactList[Artifact], artifact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.workspaces.artifacts.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(SyncArtifactList[Artifact], artifact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.workspaces.artifacts.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(SyncArtifactList[Artifact], artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.artifacts.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        artifact = client.workspaces.artifacts.delete(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.workspaces.artifacts.with_raw_response.delete(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.workspaces.artifacts.with_streaming_response.delete(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.artifacts.with_raw_response.delete(
                artifact_id="artifact_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.workspaces.artifacts.with_raw_response.delete(
                artifact_id="",
                workspace_id="workspace_id",
            )


class TestAsyncArtifacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.workspaces.artifacts.retrieve(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.artifacts.with_raw_response.retrieve(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.artifacts.with_streaming_response.retrieve(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.artifacts.with_raw_response.retrieve(
                artifact_id="artifact_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.workspaces.artifacts.with_raw_response.retrieve(
                artifact_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.workspaces.artifacts.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncArtifactList[Artifact], artifact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.workspaces.artifacts.list(
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncArtifactList[Artifact], artifact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.artifacts.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(AsyncArtifactList[Artifact], artifact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.artifacts.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(AsyncArtifactList[Artifact], artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.artifacts.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.workspaces.artifacts.delete(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.artifacts.with_raw_response.delete(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.artifacts.with_streaming_response.delete(
            artifact_id="artifact_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.artifacts.with_raw_response.delete(
                artifact_id="artifact_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.workspaces.artifacts.with_raw_response.delete(
                artifact_id="",
                workspace_id="workspace_id",
            )
