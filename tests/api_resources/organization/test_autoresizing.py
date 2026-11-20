# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestAutoresizing:
    @smoke_case("organization.autoresizing.retrieve:single", operation="retrieve", path="/v1/organization/autoresizing")
    def test_method_retrieve(self) -> None:
        autoresizing = client.organization.autoresizing.retrieve()

    @smoke_case("organization.autoresizing.update:required", operation="update", path="/v1/organization/autoresizing")
    def test_method_update(self) -> None:
        autoresizing = client.organization.autoresizing.update(
            idempotency_key="",
        )

    @smoke_case("organization.autoresizing.update:all", operation="update", path="/v1/organization/autoresizing")
    def test_method_update_with_all_params(self) -> None:
        autoresizing = client.organization.autoresizing.update(
            cpu="on",
            cpu_max_vcpu=0.25,
            memory="on",
            memory_max_mib=256,
            idempotency_key="",
        )
