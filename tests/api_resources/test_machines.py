# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.types import (
    Machine,
    MachineListItem,
)
from dedalus_sdk.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMachines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dedalus) -> None:
        machine = client.machines.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        machine = client.machines.retrieve(
            machine_id="machine_id",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.retrieve(
            machine_id="machine_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.retrieve(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.with_raw_response.retrieve(
                machine_id="",
            )

    @parametrize
    def test_method_update(self, client: Dedalus) -> None:
        machine = client.machines.update(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Dedalus) -> None:
        machine = client.machines.update(
            machine_id="machine_id",
            if_match="If-Match",
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.update(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.update(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.with_raw_response.update(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        machine = client.machines.list()
        assert_matches_type(SyncCursorPage[MachineListItem], machine, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        machine = client.machines.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncCursorPage[MachineListItem], machine, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(SyncCursorPage[MachineListItem], machine, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(SyncCursorPage[MachineListItem], machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        machine = client.machines.delete(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.delete(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.delete(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.with_raw_response.delete(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_sleep(self, client: Dedalus) -> None:
        machine = client.machines.sleep(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_raw_response_sleep(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.sleep(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_streaming_response_sleep(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.sleep(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_sleep(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.with_raw_response.sleep(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_wake(self, client: Dedalus) -> None:
        machine = client.machines.wake(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_raw_response_wake(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.wake(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    def test_streaming_response_wake(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.wake(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_wake(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.with_raw_response.wake(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    def test_method_watch(self, client: Dedalus) -> None:
        machine_stream = client.machines.watch(
            machine_id="machine_id",
        )
        machine_stream.response.close()

    @parametrize
    def test_method_watch_with_all_params(self, client: Dedalus) -> None:
        machine_stream = client.machines.watch(
            machine_id="machine_id",
            last_event_id="Last-Event-ID",
        )
        machine_stream.response.close()

    @parametrize
    def test_raw_response_watch(self, client: Dedalus) -> None:
        response = client.machines.with_raw_response.watch(
            machine_id="machine_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_watch(self, client: Dedalus) -> None:
        with client.machines.with_streaming_response.watch(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_watch(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            client.machines.with_raw_response.watch(
                machine_id="",
            )


class TestAsyncMachines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.create(
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.retrieve(
            machine_id="machine_id",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.retrieve(
            machine_id="machine_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.retrieve(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.with_raw_response.retrieve(
                machine_id="",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.update(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.update(
            machine_id="machine_id",
            if_match="If-Match",
            memory_mib=0,
            storage_gib=0,
            vcpu=0,
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.update(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.update(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.with_raw_response.update(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.list()
        assert_matches_type(AsyncCursorPage[MachineListItem], machine, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.list(
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncCursorPage[MachineListItem], machine, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(AsyncCursorPage[MachineListItem], machine, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(AsyncCursorPage[MachineListItem], machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.delete(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.delete(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.delete(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.with_raw_response.delete(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_sleep(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.sleep(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_raw_response_sleep(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.sleep(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_streaming_response_sleep(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.sleep(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_sleep(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.with_raw_response.sleep(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_wake(self, async_client: AsyncDedalus) -> None:
        machine = await async_client.machines.wake(
            machine_id="machine_id",
            if_match="If-Match",
        )
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_raw_response_wake(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.wake(
            machine_id="machine_id",
            if_match="If-Match",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        machine = await response.parse()
        assert_matches_type(Machine, machine, path=["response"])

    @parametrize
    async def test_streaming_response_wake(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.wake(
            machine_id="machine_id",
            if_match="If-Match",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            machine = await response.parse()
            assert_matches_type(Machine, machine, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_wake(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.with_raw_response.wake(
                machine_id="",
                if_match="If-Match",
            )

    @parametrize
    async def test_method_watch(self, async_client: AsyncDedalus) -> None:
        machine_stream = await async_client.machines.watch(
            machine_id="machine_id",
        )
        await machine_stream.response.aclose()

    @parametrize
    async def test_method_watch_with_all_params(self, async_client: AsyncDedalus) -> None:
        machine_stream = await async_client.machines.watch(
            machine_id="machine_id",
            last_event_id="Last-Event-ID",
        )
        await machine_stream.response.aclose()

    @parametrize
    async def test_raw_response_watch(self, async_client: AsyncDedalus) -> None:
        response = await async_client.machines.with_raw_response.watch(
            machine_id="machine_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_watch(self, async_client: AsyncDedalus) -> None:
        async with async_client.machines.with_streaming_response.watch(
            machine_id="machine_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_watch(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `machine_id` but received ''"):
            await async_client.machines.with_raw_response.watch(
                machine_id="",
            )
