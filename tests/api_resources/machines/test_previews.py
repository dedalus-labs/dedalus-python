# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.pagination import SyncCursorPage, AsyncCursorPage
from dedalus_sdk.types.machines import Preview

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dedalus) -> None:
        preview = client.machines.previews.create(
            machine_id="machine_id",
            port=0,
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dedalus) -> None:
        preview = client.machines.previews.create(
            machine_id="machine_id",
            port=0,
            protocol="http",
            visibility="public",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dedalus) -> None:
        response = client.machines.previews.with_raw_response.create(
            machine_id="machine_id",
            port=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dedalus) -> None:
        with client.machines.previews.with_streaming_response.create(
            machine_id="machine_id",
            port=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.previews.with_raw_response.create(
                machine_id="",
                port=0,
            )

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        preview = client.machines.previews.retrieve(
            machine_id="machine_id",
            preview_id="preview_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.machines.previews.with_raw_response.retrieve(
            machine_id="machine_id",
            preview_id="preview_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.machines.previews.with_streaming_response.retrieve(
            machine_id="machine_id",
            preview_id="preview_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.previews.with_raw_response.retrieve(
                machine_id="",
                preview_id="preview_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            client.machines.previews.with_raw_response.retrieve(
                machine_id="machine_id",
                preview_id="",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        preview = client.machines.previews.list(
            machine_id="machine_id",
        )
        assert_matches_type(SyncCursorPage[Preview], preview, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        preview = client.machines.previews.list(
            machine_id="machine_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncCursorPage[Preview], preview, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.machines.previews.with_raw_response.list(
            machine_id="machine_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(SyncCursorPage[Preview], preview, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.machines.previews.with_streaming_response.list(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(SyncCursorPage[Preview], preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.previews.with_raw_response.list(
                machine_id="",
            )

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        preview = client.machines.previews.delete(
            machine_id="machine_id",
            preview_id="preview_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.machines.previews.with_raw_response.delete(
            machine_id="machine_id",
            preview_id="preview_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.machines.previews.with_streaming_response.delete(
            machine_id="machine_id",
            preview_id="preview_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.previews.with_raw_response.delete(
                machine_id="",
                preview_id="preview_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            client.machines.previews.with_raw_response.delete(
                machine_id="machine_id",
                preview_id="",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.machines.previews.create(
            machine_id="machine_id",
            port=0,
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.machines.previews.create(
            machine_id="machine_id",
            port=0,
            protocol="http",
            visibility="public",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.previews.with_raw_response.create(
            machine_id="machine_id",
            port=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.previews.with_streaming_response.create(
            machine_id="machine_id",
            port=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.previews.with_raw_response.create(
                machine_id="",
                port=0,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.machines.previews.retrieve(
            machine_id="machine_id",
            preview_id="preview_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.previews.with_raw_response.retrieve(
            machine_id="machine_id",
            preview_id="preview_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.previews.with_streaming_response.retrieve(
            machine_id="machine_id",
            preview_id="preview_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.previews.with_raw_response.retrieve(
                machine_id="",
                preview_id="preview_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            await async_client.machines.previews.with_raw_response.retrieve(
                machine_id="machine_id",
                preview_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.machines.previews.list(
            machine_id="machine_id",
        )
        assert_matches_type(AsyncCursorPage[Preview], preview, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.machines.previews.list(
            machine_id="machine_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncCursorPage[Preview], preview, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.previews.with_raw_response.list(
            machine_id="machine_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(AsyncCursorPage[Preview], preview, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.previews.with_streaming_response.list(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(AsyncCursorPage[Preview], preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.previews.with_raw_response.list(
                machine_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        preview = await async_client.machines.previews.delete(
            machine_id="machine_id",
            preview_id="preview_id",
        )
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.previews.with_raw_response.delete(
            machine_id="machine_id",
            preview_id="preview_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(Preview, preview, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.previews.with_streaming_response.delete(
            machine_id="machine_id",
            preview_id="preview_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(Preview, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.previews.with_raw_response.delete(
                machine_id="",
                preview_id="preview_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `preview_id` but received ''"):
            await async_client.machines.previews.with_raw_response.delete(
                machine_id="machine_id",
                preview_id="",
            )
