# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestSSH:
    @smoke_case("machines.ssh.list:single", operation="list", path="/v1/machines/{machine_id}/ssh")
    def test_method_list(self) -> None:
        page = client.machines.ssh.list(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
        )

    @smoke_case("machines.ssh.create:single", operation="create", path="/v1/machines/{machine_id}/ssh")
    def test_method_create(self) -> None:
        ssh = client.machines.ssh.create(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            public_key="",
            idempotency_key="",
        )

    @smoke_case("machines.ssh.retrieve:single", operation="retrieve", path="/v1/machines/{machine_id}/ssh/{session_id}")
    def test_method_retrieve(self) -> None:
        ssh = client.machines.ssh.retrieve(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            session_id="sessionID",
        )

    @smoke_case("machines.ssh.delete:single", operation="delete", path="/v1/machines/{machine_id}/ssh/{session_id}")
    def test_method_delete(self) -> None:
        ssh = client.machines.ssh.delete(
            machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
            session_id="sessionID",
            idempotency_key="",
        )
