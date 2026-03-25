# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from dedalus_sdk import Dedalus, AsyncDedalus
from tests.utils import assert_matches_type
from dedalus_sdk.pagination import SyncCursorPage, AsyncCursorPage
from dedalus_sdk.types.workspaces import (
    Execution,
    ExecutionEvent,
    ExecutionOutput,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.create(
            workspace_id="workspace_id",
            command=["string"],
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.create(
            workspace_id="workspace_id",
            command=["string"],
            cwd="cwd",
            env={"foo": "string"},
            stdin="stdin",
            timeout_ms=0,
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Dedalus) -> None:
        response = client.workspaces.executions.with_raw_response.create(
            workspace_id="workspace_id",
            command=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Dedalus) -> None:
        with client.workspaces.executions.with_streaming_response.create(
            workspace_id="workspace_id",
            command=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.executions.with_raw_response.create(
                workspace_id="",
                command=["string"],
            )

    @parametrize
    def test_method_retrieve(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.retrieve(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Dedalus) -> None:
        response = client.workspaces.executions.with_raw_response.retrieve(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Dedalus) -> None:
        with client.workspaces.executions.with_streaming_response.retrieve(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.executions.with_raw_response.retrieve(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.workspaces.executions.with_raw_response.retrieve(
                execution_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_list(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncCursorPage[Execution], execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.list(
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncCursorPage[Execution], execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Dedalus) -> None:
        response = client.workspaces.executions.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(SyncCursorPage[Execution], execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Dedalus) -> None:
        with client.workspaces.executions.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(SyncCursorPage[Execution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.executions.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    def test_method_delete(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.delete(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Dedalus) -> None:
        response = client.workspaces.executions.with_raw_response.delete(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Dedalus) -> None:
        with client.workspaces.executions.with_streaming_response.delete(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.executions.with_raw_response.delete(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.workspaces.executions.with_raw_response.delete(
                execution_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_events(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(SyncCursorPage[ExecutionEvent], execution, path=["response"])

    @parametrize
    def test_method_events_with_all_params(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(SyncCursorPage[ExecutionEvent], execution, path=["response"])

    @parametrize
    def test_raw_response_events(self, client: Dedalus) -> None:
        response = client.workspaces.executions.with_raw_response.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(SyncCursorPage[ExecutionEvent], execution, path=["response"])

    @parametrize
    def test_streaming_response_events(self, client: Dedalus) -> None:
        with client.workspaces.executions.with_streaming_response.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(SyncCursorPage[ExecutionEvent], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_events(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.executions.with_raw_response.events(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.workspaces.executions.with_raw_response.events(
                execution_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    def test_method_output(self, client: Dedalus) -> None:
        execution = client.workspaces.executions.output(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(ExecutionOutput, execution, path=["response"])

    @parametrize
    def test_raw_response_output(self, client: Dedalus) -> None:
        response = client.workspaces.executions.with_raw_response.output(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionOutput, execution, path=["response"])

    @parametrize
    def test_streaming_response_output(self, client: Dedalus) -> None:
        with client.workspaces.executions.with_streaming_response.output(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionOutput, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_output(self, client: Dedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            client.workspaces.executions.with_raw_response.output(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            client.workspaces.executions.with_raw_response.output(
                execution_id="",
                workspace_id="workspace_id",
            )


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.create(
            workspace_id="workspace_id",
            command=["string"],
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.create(
            workspace_id="workspace_id",
            command=["string"],
            cwd="cwd",
            env={"foo": "string"},
            stdin="stdin",
            timeout_ms=0,
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.executions.with_raw_response.create(
            workspace_id="workspace_id",
            command=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.executions.with_streaming_response.create(
            workspace_id="workspace_id",
            command=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.create(
                workspace_id="",
                command=["string"],
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.retrieve(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.executions.with_raw_response.retrieve(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.executions.with_streaming_response.retrieve(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.retrieve(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.retrieve(
                execution_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.list(
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncCursorPage[Execution], execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.list(
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncCursorPage[Execution], execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.executions.with_raw_response.list(
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(AsyncCursorPage[Execution], execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.executions.with_streaming_response.list(
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(AsyncCursorPage[Execution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.list(
                workspace_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.delete(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.executions.with_raw_response.delete(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(Execution, execution, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.executions.with_streaming_response.delete(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(Execution, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.delete(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.delete(
                execution_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_events(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(AsyncCursorPage[ExecutionEvent], execution, path=["response"])

    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
            cursor="cursor",
            limit=0,
        )
        assert_matches_type(AsyncCursorPage[ExecutionEvent], execution, path=["response"])

    @parametrize
    async def test_raw_response_events(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.executions.with_raw_response.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(AsyncCursorPage[ExecutionEvent], execution, path=["response"])

    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.executions.with_streaming_response.events(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(AsyncCursorPage[ExecutionEvent], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_events(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.events(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.events(
                execution_id="",
                workspace_id="workspace_id",
            )

    @parametrize
    async def test_method_output(self, async_client: AsyncDedalus) -> None:
        execution = await async_client.workspaces.executions.output(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )
        assert_matches_type(ExecutionOutput, execution, path=["response"])

    @parametrize
    async def test_raw_response_output(self, async_client: AsyncDedalus) -> None:
        response = await async_client.workspaces.executions.with_raw_response.output(
            execution_id="execution_id",
            workspace_id="workspace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionOutput, execution, path=["response"])

    @parametrize
    async def test_streaming_response_output(self, async_client: AsyncDedalus) -> None:
        async with async_client.workspaces.executions.with_streaming_response.output(
            execution_id="execution_id",
            workspace_id="workspace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionOutput, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_output(self, async_client: AsyncDedalus) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workspace_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.output(
                execution_id="execution_id",
                workspace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `execution_id` but received ''"):
            await async_client.workspaces.executions.with_raw_response.output(
                execution_id="",
                workspace_id="workspace_id",
            )
