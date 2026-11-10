"""Verify automatic retry keys through the installed SDK's real request builder."""

from __future__ import annotations

import re

import httpx
import pytest

from dedalus_sdk import Dedalus, AsyncDedalus


def transport(keys: list[str]) -> httpx.MockTransport:
    def handle(request: httpx.Request) -> httpx.Response:
        key = request.headers["Idempotency-Key"]
        assert re.fullmatch(r"[0-9a-f]{12}7[0-9a-f]{3}[89ab][0-9a-f]{15}", key)
        keys.append(key)
        if len(keys) == 1:
            return httpx.Response(503, json={}, headers={"retry-after-ms": "1"})
        return httpx.Response(201, json={"id": "fb_" + key})

    return httpx.MockTransport(handle)


def verify(keys: list[str]) -> None:
    assert len(keys) == 3
    assert keys[0] == keys[1]
    assert keys[1] != keys[2]


@pytest.mark.asyncio
async def test_invariant_async_retry_preserves_valid_feedback_identity() -> None:
    keys: list[str] = []
    http_client = httpx.AsyncClient(transport=transport(keys))
    async with AsyncDedalus(
        base_url="https://feedback.invalid", api_key="fixture", max_retries=1, http_client=http_client
    ) as client:
        await client.post("/v1/feedback", cast_to=httpx.Response, body={"message": "fixture", "source": "cli"})
        await client.post("/v1/feedback", cast_to=httpx.Response, body={"message": "new submission", "source": "cli"})
    verify(keys)


def test_invariant_sync_retry_preserves_valid_feedback_identity() -> None:
    keys: list[str] = []
    http_client = httpx.Client(transport=transport(keys))
    with Dedalus(
        base_url="https://feedback.invalid", api_key="fixture", max_retries=1, http_client=http_client
    ) as client:
        client.post("/v1/feedback", cast_to=httpx.Response, body={"message": "fixture", "source": "cli"})
        client.post("/v1/feedback", cast_to=httpx.Response, body={"message": "new submission", "source": "cli"})
    verify(keys)
