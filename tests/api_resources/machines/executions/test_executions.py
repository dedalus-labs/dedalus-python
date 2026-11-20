# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestExecutions:
    @smoke_case("machines.executions.list:single", operation="list", path="/v1/machines/{machine_id}/executions")
    def test_method_list(self) -> None:
        page = client.machines.executions.list(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        )

    @smoke_case("machines.executions.create:required", operation="create", path="/v1/machines/{machine_id}/executions")
    def test_method_create(self) -> None:
        execution = client.machines.executions.create(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            command=[""],
            idempotency_key="",
        )

    @smoke_case("machines.executions.create:all", operation="create", path="/v1/machines/{machine_id}/executions")
    def test_method_create_with_all_params(self) -> None:
        execution = client.machines.executions.create(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            command=[""],
            cwd="",
            env={},
            stdin="",
            timeout_ms=0,
            idempotency_key="",
        )

    @smoke_case(
        "machines.executions.retrieve:single",
        operation="retrieve",
        path="/v1/machines/{machine_id}/executions/{execution_id}",
    )
    def test_method_retrieve(self) -> None:
        execution = client.machines.executions.retrieve(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            execution_id="executionID",
        )

    @smoke_case(
        "machines.executions.delete:single",
        operation="delete",
        path="/v1/machines/{machine_id}/executions/{execution_id}",
    )
    def test_method_delete(self) -> None:
        execution = client.machines.executions.delete(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            execution_id="executionID",
            idempotency_key="",
        )

    @smoke_case(
        "machines.executions.output:single",
        operation="output",
        path="/v1/machines/{machine_id}/executions/{execution_id}/output",
    )
    def test_method_output(self) -> None:
        execution = client.machines.executions.output(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            execution_id="executionID",
        )

    @smoke_case(
        "machines.executions.events:single",
        operation="events",
        path="/v1/machines/{machine_id}/executions/{execution_id}/events",
    )
    def test_method_events(self) -> None:
        page = client.machines.executions.events(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            execution_id="executionID",
        )
