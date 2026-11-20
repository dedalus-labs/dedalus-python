# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestUploads:
    @smoke_case("images.uploads.create:single", operation="create", path="/v1/images/uploads")
    def test_method_create(self) -> None:
        upload = client.images.uploads.create(
            platform="",
            sha256="",
            size_bytes=0,
            idempotency_key="",
        )
