from __future__ import annotations

import base64
import hashlib
import json

import httpx
import pytest

from dedalus_sdk import AsyncDedalus, Dedalus
from dedalus_sdk.images import async_import_image, async_poll_image, import_image, poll_image, ImagePreparationError

IMAGE_ID = "01994a10-1234-7000-8000-000000000001"
ARCHIVE = b"fixture docker-save archive"
DIGEST = hashlib.sha256(ARCHIVE).hexdigest()


def fixture(states=None, mutate=lambda grant: None, upload_status=200):
    requests, uploads, keys = [], [], []
    states = iter(states or ["ready"])
    grant = {
        "source": {"kind": "docker_archive", "upload_id": IMAGE_ID, "sha256": DIGEST},
        "upload": {
            "url": "https://storage.example/image?signature=secret",
            "method": "PUT",
            "expires_at": "2099-01-01T00:00:00Z",
            "headers": {
                "content-length": [str(len(ARCHIVE))],
                "if-none-match": ["*"],
                "x-amz-checksum-sha256": [base64.b64encode(bytes.fromhex(DIGEST)).decode()],
            },
        },
    }
    mutate(grant)

    def api(request):
        requests.append(request.url.path)
        assert "fixture-secret" in request.headers["authorization"]
        if request.method == "POST":
            keys.append(request.headers["idempotency-key"])
        if request.url.path.endswith("/uploads"):
            assert json.loads(request.content)["sha256"] == DIGEST
            return httpx.Response(200, json=grant)
        state = "submitted" if request.method == "POST" else next(states, "preparing")
        return httpx.Response(202 if request.method == "POST" else 200, json={"image_id": IMAGE_ID, "state": state})

    def storage(request):
        uploads.append(request)
        assert "authorization" not in request.headers
        assert request.content == ARCHIVE
        return httpx.Response(upload_status)

    return httpx.MockTransport(api), httpx.MockTransport(storage), requests, uploads, keys


@pytest.fixture
def archive(tmp_path):
    path = tmp_path / "image.tar"
    path.write_bytes(ARCHIVE)
    return path


@pytest.mark.parametrize("wait", [True, False])
def test_import_sync(archive, wait):
    api, storage, requests, uploads, keys = fixture(["preparing", "ready"])
    progress = []
    with Dedalus(api_key="fixture-secret", http_client=httpx.Client(transport=api)) as client:
        result = import_image(
            client,
            archive,
            wait=wait,
            poll_interval=0.001,
            upload_transport=storage,
            on_progress=lambda image: progress.append(image["state"]),
        )
    assert result["state"] == ("ready" if wait else "submitted")
    assert progress == (["submitted", "preparing", "ready"] if wait else ["submitted"])
    assert len(uploads) == 1 and keys[0] == keys[1]
    assert len(requests) == (4 if wait else 2)


@pytest.mark.asyncio
@pytest.mark.parametrize("wait", [True, False])
async def test_import_async(archive, wait):
    api, storage, requests, uploads, keys = fixture(["preparing", "ready"])
    async with AsyncDedalus(api_key="fixture-secret", http_client=httpx.AsyncClient(transport=api)) as client:
        result = await async_import_image(client, archive, wait=wait, poll_interval=0.001, upload_transport=storage)
    assert result["state"] == ("ready" if wait else "submitted")
    assert len(uploads) == 1 and keys[0] == keys[1]
    assert len(requests) == (4 if wait else 2)


@pytest.mark.parametrize(
    "change",
    [
        lambda g: g["upload"].update(url="http://storage.example/x"),
        lambda g: g["upload"].update(method="POST"),
        lambda g: g["upload"].update(expires_at="invalid"),
        lambda g: g["source"].update(sha256="wrong"),
        lambda g: g["upload"]["headers"].update(authorization=["secret"]),
        lambda g: g["upload"]["headers"].update({"content-length": ["1"]}),
    ],
)
def test_invalid_capability_never_uploads_or_registers(archive, change):
    api, storage, requests, uploads, _ = fixture(mutate=change)
    with Dedalus(api_key="fixture-secret", http_client=httpx.Client(transport=api)) as client:
        with pytest.raises(ValueError, match="Invalid image upload"):
            import_image(client, archive, upload_transport=storage)
    assert len(requests) == 1 and not uploads


@pytest.mark.parametrize("state", ["failed", "rejected", "revoked"])
def test_failure_preserves_image_id(state):
    api, _, requests, _, _ = fixture([state])
    with Dedalus(api_key="fixture-secret", http_client=httpx.Client(transport=api)) as client:
        with pytest.raises(ImagePreparationError, match=state) as error:
            poll_image(client, IMAGE_ID)
    assert error.value.image["image_id"] == IMAGE_ID
    assert requests == [f"/v1/images/{IMAGE_ID}"]


@pytest.mark.asyncio
async def test_async_failure_timeout_and_cancellation():
    import asyncio

    api, _, requests, _, _ = fixture(["failed"])
    async with AsyncDedalus(api_key="fixture-secret", http_client=httpx.AsyncClient(transport=api)) as client:
        with pytest.raises(ImagePreparationError, match="failed"):
            await async_poll_image(client, IMAGE_ID)
        with pytest.raises(ImagePreparationError, match="Preparation continues"):
            await async_poll_image(client, IMAGE_ID, timeout=0.02, poll_interval=0.005)
        task = asyncio.create_task(async_poll_image(client, IMAGE_ID, poll_interval=0.005))
        await asyncio.sleep(0.01)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
    assert all(path == f"/v1/images/{IMAGE_ID}" for path in requests)


def test_sync_unknown_states_and_timeout():
    api, _, _, _, _ = fixture(["future-state", "ready"])
    with Dedalus(api_key="fixture-secret", http_client=httpx.Client(transport=api)) as client:
        assert poll_image(client, IMAGE_ID, poll_interval=0.001)["state"] == "ready"
        with pytest.raises(ImagePreparationError, match="Preparation continues"):
            poll_image(client, IMAGE_ID, timeout=0.02, poll_interval=0.005)


@pytest.mark.parametrize("status", [302, 500, 412])
def test_upload_failure_never_registers_but_repeated_put_can(archive, status):
    api, storage, requests, _, _ = fixture(upload_status=status)
    with Dedalus(api_key="fixture-secret", http_client=httpx.Client(transport=api)) as client:
        if status == 412:
            assert import_image(client, archive, wait=False, upload_transport=storage)["state"] == "submitted"
        else:
            with pytest.raises(RuntimeError, match=f"HTTP {status}"):
                import_image(client, archive, upload_transport=storage)
            assert len(requests) == 1
