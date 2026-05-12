# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.types import (
    OrgUsage,
    MachineComputeUsage,
    MachineStorageUsage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        usage = client.usage.retrieve()
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Dedalus) -> None:
        usage = client.usage.retrieve(
            period_start="period_start",
        )
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.usage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(OrgUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_machine_compute(self, client: Dedalus) -> None:
        usage = client.usage.machine_compute()
        assert_matches_type(MachineComputeUsage, usage, path=["response"])

    @parametrize
    def test_method_machine_compute_with_all_params(self, client: Dedalus) -> None:
        usage = client.usage.machine_compute(
            granularity="granularity",
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineComputeUsage, usage, path=["response"])

    @parametrize
    def test_raw_response_machine_compute(self, client: Dedalus) -> None:
        response = client.usage.with_raw_response.machine_compute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(MachineComputeUsage, usage, path=["response"])

    @parametrize
    def test_streaming_response_machine_compute(self, client: Dedalus) -> None:
        with client.usage.with_streaming_response.machine_compute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(MachineComputeUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_machine_storage(self, client: Dedalus) -> None:
        usage = client.usage.machine_storage()
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    def test_method_machine_storage_with_all_params(self, client: Dedalus) -> None:
        usage = client.usage.machine_storage(
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    def test_raw_response_machine_storage(self, client: Dedalus) -> None:
        response = client.usage.with_raw_response.machine_storage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    def test_streaming_response_machine_storage(self, client: Dedalus) -> None:
        with client.usage.with_streaming_response.machine_storage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(MachineStorageUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.usage.retrieve()
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.usage.retrieve(
            period_start="period_start",
        )
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.usage.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.usage.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(OrgUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_machine_compute(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.usage.machine_compute()
        assert_matches_type(MachineComputeUsage, usage, path=["response"])

    @parametrize
    async def test_method_machine_compute_with_all_params(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.usage.machine_compute(
            granularity="granularity",
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineComputeUsage, usage, path=["response"])

    @parametrize
    async def test_raw_response_machine_compute(self, async_client: AsyncDedalus) -> None:
        response = await async_client.usage.with_raw_response.machine_compute()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(MachineComputeUsage, usage, path=["response"])

    @parametrize
    async def test_streaming_response_machine_compute(self, async_client: AsyncDedalus) -> None:
        async with async_client.usage.with_streaming_response.machine_compute() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(MachineComputeUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_machine_storage(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.usage.machine_storage()
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    async def test_method_machine_storage_with_all_params(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.usage.machine_storage(
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    async def test_raw_response_machine_storage(self, async_client: AsyncDedalus) -> None:
        response = await async_client.usage.with_raw_response.machine_storage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    async def test_streaming_response_machine_storage(self, async_client: AsyncDedalus) -> None:
        async with async_client.usage.with_streaming_response.machine_storage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(MachineStorageUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
