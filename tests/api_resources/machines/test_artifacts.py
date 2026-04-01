# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.pagination import SyncCursorPage, AsyncCursorPage
from dedalus_sdk.types.machines import Artifact

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifacts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        artifact = client.machines.artifacts.retrieve(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.machines.artifacts.with_raw_response.retrieve(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.machines.artifacts.with_streaming_response.retrieve(
            machine_id="machine_id",
            artifact_id="artifact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.artifacts.with_raw_response.retrieve(
                machine_id="",
                artifact_id="artifact_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.machines.artifacts.with_raw_response.retrieve(
                machine_id="machine_id",
                artifact_id="",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        artifact = client.machines.artifacts.list(
            machine_id="machine_id",
        )
        assert_matches_type(SyncCursorPage[Artifact], artifact, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        artifact = client.machines.artifacts.list(
            machine_id="machine_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncCursorPage[Artifact], artifact, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.machines.artifacts.with_raw_response.list(
            machine_id="machine_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(SyncCursorPage[Artifact], artifact, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.machines.artifacts.with_streaming_response.list(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(SyncCursorPage[Artifact], artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.artifacts.with_raw_response.list(
                machine_id="",
            )

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        artifact = client.machines.artifacts.delete(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.machines.artifacts.with_raw_response.delete(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.machines.artifacts.with_streaming_response.delete(
            machine_id="machine_id",
            artifact_id="artifact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.artifacts.with_raw_response.delete(
                machine_id="",
                artifact_id="artifact_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.machines.artifacts.with_raw_response.delete(
                machine_id="machine_id",
                artifact_id="",
            )


class TestAsyncArtifacts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.machines.artifacts.retrieve(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.artifacts.with_raw_response.retrieve(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.artifacts.with_streaming_response.retrieve(
            machine_id="machine_id",
            artifact_id="artifact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.artifacts.with_raw_response.retrieve(
                machine_id="",
                artifact_id="artifact_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.machines.artifacts.with_raw_response.retrieve(
                machine_id="machine_id",
                artifact_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.machines.artifacts.list(
            machine_id="machine_id",
        )
        assert_matches_type(AsyncCursorPage[Artifact], artifact, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.machines.artifacts.list(
            machine_id="machine_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncCursorPage[Artifact], artifact, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.artifacts.with_raw_response.list(
            machine_id="machine_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(AsyncCursorPage[Artifact], artifact, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.artifacts.with_streaming_response.list(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(AsyncCursorPage[Artifact], artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.artifacts.with_raw_response.list(
                machine_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        artifact = await async_client.machines.artifacts.delete(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.artifacts.with_raw_response.delete(
            machine_id="machine_id",
            artifact_id="artifact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(Artifact, artifact, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.artifacts.with_streaming_response.delete(
            machine_id="machine_id",
            artifact_id="artifact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(Artifact, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.artifacts.with_raw_response.delete(
                machine_id="",
                artifact_id="artifact_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.machines.artifacts.with_raw_response.delete(
                machine_id="machine_id",
                artifact_id="",
            )
