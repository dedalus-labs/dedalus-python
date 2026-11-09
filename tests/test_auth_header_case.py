import httpx
import pytest

from dedalus_sdk import AsyncDedalus, Dedalus, omit

HEADERS = [
    ("Authorization", "Bearer fixture"),
    ("authorization", "Bearer fixture"),
    ("AUTHORIZATION", "Bearer fixture"),
    ("x-api-key", "fixture"),
    ("X-API-Key", "fixture"),
    ("X-API-KEY", "fixture"),
]


@pytest.fixture(autouse=True)
def clear_auth_environment(monkeypatch: pytest.MonkeyPatch) -> None:
    for name in ("DEDALUS_API_KEY", "DEDALUS_X_API_KEY", "DEDALUS_CUSTOM_HEADERS"):
        monkeypatch.delenv(name, raising=False)


@pytest.mark.parametrize("header,value", HEADERS)
@pytest.mark.parametrize("location", ["default", "request"])
def test_sync_accepts_case_insensitive_auth_headers(header: str, value: str, location: str) -> None:
    seen = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"items": [], "next_cursor": None})

    with Dedalus(
        base_url="https://fixture.invalid",
        http_client=httpx.Client(transport=httpx.MockTransport(handle)),
        default_headers={header: value} if location == "default" else None,
    ) as client:
        page = client.machines.list(extra_headers={header: value} if location == "request" else None)
        assert list(page) == []
    assert len(seen) == 1
    assert seen[0].headers[header] == value


@pytest.mark.asyncio
@pytest.mark.parametrize("header,value", HEADERS)
@pytest.mark.parametrize("location", ["default", "request"])
async def test_async_accepts_case_insensitive_auth_headers(header: str, value: str, location: str) -> None:
    seen = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"items": [], "next_cursor": None})

    async with AsyncDedalus(
        base_url="https://fixture.invalid",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle)),
        default_headers={header: value} if location == "default" else None,
    ) as client:
        page = await client.machines.list(extra_headers={header: value} if location == "request" else None)
        assert [item async for item in page] == []
    assert len(seen) == 1
    assert seen[0].headers[header] == value


@pytest.mark.parametrize("header", ["Authorization", "authorization", "x-api-key", "X-API-Key"])
def test_sync_accepts_case_insensitive_explicit_omission(header: str) -> None:
    seen = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"items": []})

    with Dedalus(
        base_url="https://fixture.invalid", http_client=httpx.Client(transport=httpx.MockTransport(handle))
    ) as client:
        client.machines.list(extra_headers={header: omit})
    assert len(seen) == 1
    assert "authorization" not in seen[0].headers
    assert "x-api-key" not in seen[0].headers


@pytest.mark.asyncio
@pytest.mark.parametrize("header", ["Authorization", "authorization", "x-api-key", "X-API-Key"])
async def test_async_accepts_case_insensitive_explicit_omission(header: str) -> None:
    seen = []

    def handle(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"items": []})

    async with AsyncDedalus(
        base_url="https://fixture.invalid", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))
    ) as client:
        await client.machines.list(extra_headers={header: omit})
    assert len(seen) == 1
    assert "authorization" not in seen[0].headers
    assert "x-api-key" not in seen[0].headers


def test_sync_still_rejects_missing_auth() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        pytest.fail("An unauthenticated request must not be sent")

    with (
        Dedalus(
            base_url="https://fixture.invalid", http_client=httpx.Client(transport=httpx.MockTransport(handle))
        ) as client,
        pytest.raises(TypeError, match="Could not resolve authentication"),
    ):
        client.machines.list()


@pytest.mark.asyncio
async def test_async_still_rejects_missing_auth() -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        pytest.fail("An unauthenticated request must not be sent")

    async with AsyncDedalus(
        base_url="https://fixture.invalid", http_client=httpx.AsyncClient(transport=httpx.MockTransport(handle))
    ) as client:
        with pytest.raises(TypeError, match="Could not resolve authentication"):
            await client.machines.list()
