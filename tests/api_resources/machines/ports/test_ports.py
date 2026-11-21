# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestPorts:
    @smoke_case("machines.ports.list:single", operation="list", path="/v1/machines/{machine_id}/ports")
    def test_method_list(self) -> None:
        page = client.machines.ports.list(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        )

    @smoke_case("machines.ports.create:required", operation="create", path="/v1/machines/{machine_id}/ports")
    def test_method_create(self) -> None:
        port = client.machines.ports.create(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port=0,
            protocol="http",
            visibility="private",
            idempotency_key="",
        )

    @smoke_case("machines.ports.create:all", operation="create", path="/v1/machines/{machine_id}/ports")
    def test_method_create_with_all_params(self) -> None:
        port = client.machines.ports.create(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            expires=1,
            port=0,
            protocol="http",
            visibility="private",
            idempotency_key="",
        )

    @smoke_case(
        "machines.ports.retrieve:single", operation="retrieve", path="/v1/machines/{machine_id}/ports/{port_id}"
    )
    def test_method_retrieve(self) -> None:
        port = client.machines.ports.retrieve(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
        )

    @smoke_case("machines.ports.update:single", operation="update", path="/v1/machines/{machine_id}/ports/{port_id}")
    def test_method_update(self) -> None:
        port = client.machines.ports.update(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
            visibility="public",
            idempotency_key="",
        )

    @smoke_case("machines.ports.delete:single", operation="delete", path="/v1/machines/{machine_id}/ports/{port_id}")
    def test_method_delete(self) -> None:
        port = client.machines.ports.delete(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
            idempotency_key="",
        )
