# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAccessKeys:
    @smoke_case(
        "machines.ports.accessKeys.list:required",
        operation="list",
        path="/v1/machines/{machine_id}/ports/{port_id}/access-keys",
    )
    def test_method_list(self) -> None:
        access_key = client.machines.ports.access_keys.list(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
        )

    @smoke_case(
        "machines.ports.accessKeys.list:all",
        operation="list",
        path="/v1/machines/{machine_id}/ports/{port_id}/access-keys",
    )
    def test_method_list_with_all_params(self) -> None:
        access_key = client.machines.ports.access_keys.list(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
            limit=1,
            cursor="cursor",
        )

    @smoke_case(
        "machines.ports.accessKeys.mint:single",
        operation="mint",
        path="/v1/machines/{machine_id}/ports/{port_id}/access-keys",
    )
    def test_method_mint(self) -> None:
        access_key = client.machines.ports.access_keys.mint(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
            expires_in=1,
            idempotency_key="",
        )

    @smoke_case(
        "machines.ports.accessKeys.revoke:single",
        operation="revoke",
        path="/v1/machines/{machine_id}/ports/{port_id}/access-keys/{access_key_id}",
    )
    def test_method_revoke(self) -> None:
        access_key = client.machines.ports.access_keys.revoke(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
            access_key_id="accessKeyID",
            idempotency_key="",
        )

    @smoke_case(
        "machines.ports.accessKeys.rotate:single",
        operation="rotate",
        path="/v1/machines/{machine_id}/ports/{port_id}/access-keys/{access_key_id}/rotate",
    )
    def test_method_rotate(self) -> None:
        access_key = client.machines.ports.access_keys.rotate(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            port_id="portID",
            access_key_id="accessKeyID",
            expires_in=1,
            idempotency_key="",
        )
