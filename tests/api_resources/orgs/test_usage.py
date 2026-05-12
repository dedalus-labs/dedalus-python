# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.types.orgs import (
    OrgUsage,
    MachineUsage,
    MachineStorageUsage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        usage = client.orgs.usage.retrieve(
            org_id="org_id",
        )
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Dedalus) -> None:
        usage = client.orgs.usage.retrieve(
            org_id="org_id",
            period_start="period_start",
        )
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.orgs.usage.with_raw_response.retrieve(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.orgs.usage.with_streaming_response.retrieve(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(OrgUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.usage.with_raw_response.retrieve(
                org_id="",
            )

    @parametrize
    def test_method_get_machine_storage_usage(self, client: Dedalus) -> None:
        usage = client.orgs.usage.get_machine_storage_usage(
            org_id="org_id",
        )
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    def test_method_get_machine_storage_usage_with_all_params(self, client: Dedalus) -> None:
        usage = client.orgs.usage.get_machine_storage_usage(
            org_id="org_id",
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    def test_raw_response_get_machine_storage_usage(self, client: Dedalus) -> None:
        response = client.orgs.usage.with_raw_response.get_machine_storage_usage(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    def test_streaming_response_get_machine_storage_usage(self, client: Dedalus) -> None:
        with client.orgs.usage.with_streaming_response.get_machine_storage_usage(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(MachineStorageUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_machine_storage_usage(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.usage.with_raw_response.get_machine_storage_usage(
                org_id="",
            )

    @parametrize
    def test_method_get_machine_usage(self, client: Dedalus) -> None:
        usage = client.orgs.usage.get_machine_usage(
            org_id="org_id",
        )
        assert_matches_type(MachineUsage, usage, path=["response"])

    @parametrize
    def test_method_get_machine_usage_with_all_params(self, client: Dedalus) -> None:
        usage = client.orgs.usage.get_machine_usage(
            org_id="org_id",
            granularity="granularity",
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineUsage, usage, path=["response"])

    @parametrize
    def test_raw_response_get_machine_usage(self, client: Dedalus) -> None:
        response = client.orgs.usage.with_raw_response.get_machine_usage(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(MachineUsage, usage, path=["response"])

    @parametrize
    def test_streaming_response_get_machine_usage(self, client: Dedalus) -> None:
        with client.orgs.usage.with_streaming_response.get_machine_usage(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(MachineUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_machine_usage(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            client.orgs.usage.with_raw_response.get_machine_usage(
                org_id="",
            )


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.orgs.usage.retrieve(
            org_id="org_id",
        )
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.orgs.usage.retrieve(
            org_id="org_id",
            period_start="period_start",
        )
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.orgs.usage.with_raw_response.retrieve(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(OrgUsage, usage, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.orgs.usage.with_streaming_response.retrieve(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(OrgUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.usage.with_raw_response.retrieve(
                org_id="",
            )

    @parametrize
    async def test_method_get_machine_storage_usage(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.orgs.usage.get_machine_storage_usage(
            org_id="org_id",
        )
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    async def test_method_get_machine_storage_usage_with_all_params(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.orgs.usage.get_machine_storage_usage(
            org_id="org_id",
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    async def test_raw_response_get_machine_storage_usage(self, async_client: AsyncDedalus) -> None:
        response = await async_client.orgs.usage.with_raw_response.get_machine_storage_usage(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(MachineStorageUsage, usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_machine_storage_usage(self, async_client: AsyncDedalus) -> None:
        async with async_client.orgs.usage.with_streaming_response.get_machine_storage_usage(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(MachineStorageUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_machine_storage_usage(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.usage.with_raw_response.get_machine_storage_usage(
                org_id="",
            )

    @parametrize
    async def test_method_get_machine_usage(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.orgs.usage.get_machine_usage(
            org_id="org_id",
        )
        assert_matches_type(MachineUsage, usage, path=["response"])

    @parametrize
    async def test_method_get_machine_usage_with_all_params(self, async_client: AsyncDedalus) -> None:
        usage = await async_client.orgs.usage.get_machine_usage(
            org_id="org_id",
            granularity="granularity",
            machine_id="machine_id",
            period_end="period_end",
            period_start="period_start",
        )
        assert_matches_type(MachineUsage, usage, path=["response"])

    @parametrize
    async def test_raw_response_get_machine_usage(self, async_client: AsyncDedalus) -> None:
        response = await async_client.orgs.usage.with_raw_response.get_machine_usage(
            org_id="org_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(MachineUsage, usage, path=["response"])

    @parametrize
    async def test_streaming_response_get_machine_usage(self, async_client: AsyncDedalus) -> None:
        async with async_client.orgs.usage.with_streaming_response.get_machine_usage(
            org_id="org_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(MachineUsage, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_machine_usage(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `org_id` but received ''"):
            await async_client.orgs.usage.with_raw_response.get_machine_usage(
                org_id="",
            )
