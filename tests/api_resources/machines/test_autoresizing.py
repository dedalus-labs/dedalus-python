# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAutoresizing:
    @smoke_case(
        "machines.autoresizing.retrieve:single", operation="retrieve", path="/v1/machines/{machine_id}/autoresizing"
    )
    def test_method_retrieve(self) -> None:
        autoresizing = client.machines.autoresizing.retrieve(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        )

    @smoke_case(
        "machines.autoresizing.update:required", operation="update", path="/v1/machines/{machine_id}/autoresizing"
    )
    def test_method_update(self) -> None:
        autoresizing = client.machines.autoresizing.update(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.autoresizing.update:all", operation="update", path="/v1/machines/{machine_id}/autoresizing")
    def test_method_update_with_all_params(self) -> None:
        autoresizing = client.machines.autoresizing.update(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            cpu="on",
            cpu_max_vcpu=0.25,
            memory="on",
            memory_max_mib=256,
            idempotency_key="",
        )
