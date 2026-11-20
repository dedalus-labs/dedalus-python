# File generated from our OpenAPI spec by Scalar. See README.md for details.

# Smoke tests for one part of the client; see tests/smoke_support.py for how to run them.
from __future__ import annotations

from tests.smoke_support import client, smoke_case


class TestImages:
    @smoke_case("images.list:required", operation="list", path="/v1/images")
    def test_method_list(self) -> None:
        images = client.images.list(
            limit=100,
        )

    @smoke_case("images.list:all", operation="list", path="/v1/images")
    def test_method_list_with_all_params(self) -> None:
        images = client.images.list(
            limit=100,
            cursor="cursor",
        )

    @smoke_case("images.create:required", operation="create", path="/v1/images")
    def test_method_create(self) -> None:
        image = client.images.create(
            platform="linux/amd64",
            source={"kind": ""},
            idempotency_key="",
        )

    @smoke_case("images.create:all", operation="create", path="/v1/images")
    def test_method_create_with_all_params(self) -> None:
        image = client.images.create(
            credential_ref="",
            name="",
            platform="linux/amd64",
            source={"kind": "", "reference": "", "sha256": "", "upload_id": ""},
            idempotency_key="",
        )

    @smoke_case("images.retrieve:single", operation="retrieve", path="/v1/images/{image_id}")
    def test_method_retrieve(self) -> None:
        image = client.images.retrieve(
            image_id="imageID",
        )

    @smoke_case("images.update:single", operation="update", path="/v1/images/{image_id}")
    def test_method_update(self) -> None:
        image = client.images.update(
            image_id="imageID",
            name="",
            idempotency_key="",
        )

    @smoke_case("images.delete:single", operation="delete", path="/v1/images/{image_id}")
    def test_method_delete(self) -> None:
        image = client.images.delete(
            image_id="imageID",
            idempotency_key="",
        )
