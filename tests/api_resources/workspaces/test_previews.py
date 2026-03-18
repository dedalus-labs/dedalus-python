# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.pagination import SyncPreviewList, AsyncPreviewList
from dedalus_sdk.types.workspaces import Preview

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dedalus) -> None:
        preview = client.workspaces.previews.create(
            workspace_id="workspace_id",
            port=0,
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dedalus) -> None:
        preview = client.workspaces.previews.create(
            workspace_id="workspace_id",
            port=0,
            protocol="http",
            wake_if_needed=True,
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dedalus) -> None:
        response = client.workspaces.previews.with_raw_response.create(
            workspace_id="workspace_id",
            port=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dedalus) -> None:
        with client.workspaces.previews.with_streaming_response.create(
            workspace_id="workspace_id",
            port=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.previews.with_raw_response.create(
                workspace_id="",
                port=0,
            )

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        preview = client.workspaces.previews.retrieve(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.workspaces.previews.with_raw_response.retrieve(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.workspaces.previews.with_streaming_response.retrieve(
            preview_id="preview_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.previews.with_raw_response.retrieve(
                preview_id="preview_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            client.workspaces.previews.with_raw_response.retrieve(
                preview_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        preview = client.workspaces.previews.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncPreviewList[Preview], preview, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        preview = client.workspaces.previews.list(
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncPreviewList[Preview], preview, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.workspaces.previews.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(SyncPreviewList[Preview], preview, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.workspaces.previews.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(SyncPreviewList[Preview], preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.previews.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        preview = client.workspaces.previews.delete(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.workspaces.previews.with_raw_response.delete(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.workspaces.previews.with_streaming_response.delete(
            preview_id="preview_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.previews.with_raw_response.delete(
                preview_id="preview_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            client.workspaces.previews.with_raw_response.delete(
                preview_id="",
                workspace_id="workspace_id",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.workspaces.previews.create(
            workspace_id="workspace_id",
            port=0,
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.workspaces.previews.create(
            workspace_id="workspace_id",
            port=0,
            protocol="http",
            wake_if_needed=True,
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.previews.with_raw_response.create(
            workspace_id="workspace_id",
            port=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.previews.with_streaming_response.create(
            workspace_id="workspace_id",
            port=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.previews.with_raw_response.create(
                workspace_id="",
                port=0,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.workspaces.previews.retrieve(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.previews.with_raw_response.retrieve(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.previews.with_streaming_response.retrieve(
            preview_id="preview_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.previews.with_raw_response.retrieve(
                preview_id="preview_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            await async_client.workspaces.previews.with_raw_response.retrieve(
                preview_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.workspaces.previews.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncPreviewList[Preview], preview, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.workspaces.previews.list(
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncPreviewList[Preview], preview, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.previews.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(AsyncPreviewList[Preview], preview, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.previews.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(AsyncPreviewList[Preview], preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.previews.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.workspaces.previews.delete(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.previews.with_raw_response.delete(
            preview_id="preview_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.previews.with_streaming_response.delete(
            preview_id="preview_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.previews.with_raw_response.delete(
                preview_id="preview_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            await async_client.workspaces.previews.with_raw_response.delete(
                preview_id="",
                workspace_id="workspace_id",
            )
