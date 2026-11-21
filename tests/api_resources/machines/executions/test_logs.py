# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestLogs:
    @smoke_case(
        "machines.executions.logs.retrieve:single",
        operation="retrieve",
        path="/v1/machines/{machine_id}/executions/{execution_id}/logs",
    )
    def test_method_retrieve(self) -> None:
        log = client.machines.executions.logs.retrieve(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            execution_id="executionID",
        )

    @smoke_case(
        "machines.executions.logs.createToken:single",
        operation="createToken",
        path="/v1/machines/{machine_id}/executions/{execution_id}/logs/token",
    )
    def test_method_create_token(self) -> None:
        log = client.machines.executions.logs.create_token(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            execution_id="executionID",
            idempotency_key="",
        )
