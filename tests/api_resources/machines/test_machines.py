# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestMachines:
    @smoke_case("machines.list:single", operation="list", path="/v1/machines")
    def test_method_list(self) -> None:
        page = client.machines.list()

    @smoke_case("machines.create:required", operation="create", path="/v1/machines")
    def test_method_create(self) -> None:
        machine = client.machines.create(
            autosleep="300s",
            memory_mib=4096,
            storage_gib=10,
            vcpu=1,
            idempotency_key="",
        )

    @smoke_case("machines.create:all", operation="create", path="/v1/machines")
    def test_method_create_with_all_params(self) -> None:
        machine = client.machines.create(
            autosleep="300s",
            image_id="x",
            memory_mib=4096,
            storage_gib=10,
            vcpu=1,
            idempotency_key="",
        )

    @smoke_case("machines.retrieve:single", operation="retrieve", path="/v1/machines/{machine_id}")
    def test_method_retrieve(self) -> None:
        machine = client.machines.retrieve(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        )

    @smoke_case("machines.update:required", operation="update", path="/v1/machines/{machine_id}")
    def test_method_update(self) -> None:
        machine = client.machines.update(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.update:all", operation="update", path="/v1/machines/{machine_id}")
    def test_method_update_with_all_params(self) -> None:
        machine = client.machines.update(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            autosleep="",
            storage_gib=0,
            idempotency_key="",
        )

    @smoke_case("machines.delete:required", operation="delete", path="/v1/machines/{machine_id}")
    def test_method_delete(self) -> None:
        machine = client.machines.delete(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.delete:all", operation="delete", path="/v1/machines/{machine_id}")
    def test_method_delete_with_all_params(self) -> None:
        machine = client.machines.delete(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            force=True,
            idempotency_key="",
        )

    @smoke_case("machines.sleep:single", operation="sleep", path="/v1/machines/{machine_id}/sleep")
    def test_method_sleep(self) -> None:
        machine = client.machines.sleep(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.wake:single", operation="wake", path="/v1/machines/{machine_id}/wake")
    def test_method_wake(self) -> None:
        machine = client.machines.wake(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.reboot:required", operation="reboot", path="/v1/machines/{machine_id}/reboot")
    def test_method_reboot(self) -> None:
        machine = client.machines.reboot(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.reboot:all", operation="reboot", path="/v1/machines/{machine_id}/reboot")
    def test_method_reboot_with_all_params(self) -> None:
        machine = client.machines.reboot(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            force=True,
            idempotency_key="",
        )

    @smoke_case("machines.resize:required", operation="resize", path="/v1/machines/{machine_id}/resize")
    def test_method_resize(self) -> None:
        machine = client.machines.resize(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            idempotency_key="",
        )

    @smoke_case("machines.resize:all", operation="resize", path="/v1/machines/{machine_id}/resize")
    def test_method_resize_with_all_params(self) -> None:
        machine = client.machines.resize(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            memory_mib=0,
            vcpu=0,
            idempotency_key="",
        )
