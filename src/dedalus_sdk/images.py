"""Image import workflows using the SDK transport and a separate signed-upload client."""

from __future__ import annotations

import base64
import hashlib
import math
import os
import stat
import time
from datetime import datetime, timezone
from typing import BinaryIO, Callable, Literal, Optional, Union, cast
from urllib.parse import parse_qs, quote, urlsplit
from uuid import uuid4

import anyio
import httpx
from typing_extensions import TypedDict

from . import APITimeoutError, AsyncDedalus, Dedalus


class Image(TypedDict):
    image_id: str
    state: str


class ImagePreparationError(RuntimeError):
    def __init__(self, image: Image, message: str) -> None:
        self.image = image
        super().__init__(f"Image {image['image_id']}: {message}")


def _record(value: object) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError("Invalid image API response")
    return cast("dict[str, object]", value)


def _image(value: object, expected: Optional[str] = None) -> Image:
    result = _record(value)
    if (
        not isinstance(result.get("image_id"), str)
        or not result["image_id"]
        or not isinstance(result.get("state"), str)
        or not result["state"]
        or (expected is not None and result["image_id"] != expected)
    ):
        raise ValueError("Invalid or mismatched image API response")
    return cast(Image, result)


def _ready(image: Image, progress: Optional[Callable[[Image], None]]) -> bool:
    if progress:
        progress(image)
    if image["state"] in ("failed", "rejected", "revoked"):
        details = _record(image)
        error = _record(details.get("error") or {})
        message = error.get("message") or details.get("reason") or image["state"]
        code = f"{error['error_code']}: " if error.get("error_code") else ""
        raise ImagePreparationError(image, f"{code}{message}")
    return image["state"] == "ready"


def _duration(value: float, name: str) -> float:
    if not math.isfinite(value) or not 0 < value <= 86400:
        raise ValueError(f"{name} must be between 0 and 86400 seconds")
    return value


def _remaining(end: float, image: Optional[Image] = None) -> float:
    remaining = end - time.monotonic()
    if remaining <= 0:
        if image is not None:
            raise ImagePreparationError(
                image, "Timed out waiting. Preparation continues; use this image ID to resume polling."
            )
        raise TimeoutError("Image import timed out before receiving an image ID")
    return remaining


def _identity(image: Union[str, Image]) -> str:
    value = image if isinstance(image, str) else image["image_id"]
    if not value or any(char.isspace() for char in value):
        raise ValueError("image ID must be a nonempty string without whitespace")
    return value


def poll_image(
    client: Dedalus,
    image: Union[str, Image],
    *,
    timeout: float = 3600,
    poll_interval: float = 2,
    on_progress: Optional[Callable[[Image], None]] = None,
) -> Image:
    """Wait for readiness. Timeout stops polling, never server preparation."""
    end = time.monotonic() + _duration(timeout, "timeout")
    interval = _duration(poll_interval, "poll_interval")
    image_id = _identity(image)
    current = None if isinstance(image, str) else _image(image, image_id)
    while True:
        remaining = _remaining(end, current or Image(image_id=image_id, state="unknown"))
        if current is None:
            try:
                response = client.get(
                    f"/v1/images/{quote(image_id, safe='')}",
                    cast_to=httpx.Response,
                    options={"timeout": remaining, "max_retries": 0},
                )
            except APITimeoutError as error:
                raise ImagePreparationError(
                    Image(image_id=image_id, state="unknown"),
                    "Status request timed out. Preparation continues; use this image ID to resume polling.",
                ) from error
            current = _image(response.json(), image_id)
        _remaining(end, current)
        if _ready(current, on_progress):
            return current
        time.sleep(min(interval, _remaining(end, current)))
        _remaining(end, current)
        current = None


async def async_poll_image(
    client: AsyncDedalus,
    image: Union[str, Image],
    *,
    timeout: float = 3600,
    poll_interval: float = 2,
    on_progress: Optional[Callable[[Image], None]] = None,
) -> Image:
    """Async readiness polling; task cancellation leaves preparation running."""
    image_id = _identity(image)
    interval = _duration(poll_interval, "poll_interval")
    current = None if isinstance(image, str) else _image(image, image_id)
    try:
        with anyio.fail_after(_duration(timeout, "timeout")):
            while True:
                if current is None:
                    response = await client.get(f"/v1/images/{quote(image_id, safe='')}", cast_to=httpx.Response)
                    current = _image(response.json(), image_id)
                if _ready(current, on_progress):
                    return current
                await anyio.sleep(interval)
                current = None
    except (TimeoutError, APITimeoutError) as error:
        raise ImagePreparationError(
            Image(image_id=image_id, state="unknown"),
            "Timed out waiting. Preparation continues; use this image ID to resume polling.",
        ) from error


def _hash(file: BinaryIO, end: float) -> tuple[str, int]:
    before = os.fstat(file.fileno())
    if not stat.S_ISREG(before.st_mode) or not 0 < before.st_size <= 5 * 1024**3:
        raise ValueError("Image archive must be a regular file between 1 byte and 5 GiB")
    digest = hashlib.sha256()
    count = 0
    while True:
        _remaining(end)
        chunk = file.read(1024 * 1024)
        if not chunk:
            break
        digest.update(chunk)
        count += len(chunk)
    after = os.fstat(file.fileno())
    if count != before.st_size or after.st_size != before.st_size or after.st_mtime_ns != before.st_mtime_ns:
        raise ValueError("Image archive changed while hashing")
    file.seek(0)
    return digest.hexdigest(), count


def _capability(value: object, sha256: str, size: int) -> tuple[dict[str, object], str, httpx.Headers]:
    reservation = _record(value)
    source, upload = _record(reservation.get("source")), _record(reservation.get("upload"))
    try:
        url = upload["url"]
        if not isinstance(url, str) or not isinstance(upload["expires_at"], str):
            raise ValueError()
        endpoint = urlsplit(url)
        expires = datetime.fromisoformat(upload["expires_at"].replace("Z", "+00:00"))
        headers = httpx.Headers()
        for key, values in _record(upload.get("headers")).items():
            if key.lower() in ("authorization", "proxy-authorization", "cookie") or not isinstance(values, list):
                raise ValueError()
            if not all(isinstance(value, str) for value in values):
                raise ValueError()
            headers[key] = ", ".join(values)
        checksum = (
            headers.get("x-amz-checksum-sha256") or parse_qs(endpoint.query).get("X-Amz-Checksum-Sha256", [""])[0]
        )
        if (
            source.get("kind") != "docker_archive"
            or source.get("sha256") != sha256
            or not isinstance(source.get("upload_id"), str)
            or not source["upload_id"]
            or upload.get("method") != "PUT"
            or endpoint.scheme != "https"
            or not endpoint.hostname
            or endpoint.username
            or endpoint.password
            or endpoint.fragment
            or expires <= datetime.now(timezone.utc)
            or headers.get("content-length") != str(size)
            or headers.get("if-none-match") != "*"
            or checksum != base64.b64encode(bytes.fromhex(sha256)).decode()
        ):
            raise ValueError()
        return source, url, headers
    except (KeyError, ValueError, TypeError):
        raise ValueError("Invalid image upload capability") from None


def _uploaded(response: httpx.Response) -> None:
    # Registration verifies an existing immutable object after a repeated PUT.
    if not response.is_success and response.status_code != 412:
        raise RuntimeError(f"Image archive upload failed: HTTP {response.status_code}")


def import_image(
    client: Dedalus,
    path: Union[str, os.PathLike[str]],
    *,
    wait: bool = True,
    name: Optional[str] = None,
    platform: Literal["linux/amd64"] = "linux/amd64",
    timeout: float = 3600,
    poll_interval: float = 2,
    idempotency_key: Optional[str] = None,
    on_progress: Optional[Callable[[Image], None]] = None,
    upload_transport: Optional[httpx.BaseTransport] = None,
) -> Image:
    """Stream a docker-save archive, register it, and wait by default.

    The sync deadline is checked between I/O operations; each request has a
    remaining-budget inactivity timeout and automatic API retries are disabled.
    """
    if platform != "linux/amd64":
        raise ValueError("Custom images currently require linux/amd64")
    end = time.monotonic() + _duration(timeout, "timeout")
    _duration(poll_interval, "poll_interval")
    key = idempotency_key or str(uuid4())
    with open(path, "rb") as file:
        sha256, size = _hash(file, end)
        response = client.post(
            "/v1/images/uploads",
            cast_to=httpx.Response,
            body={"sha256": sha256, "size_bytes": size, "platform": platform},
            options={"idempotency_key": key, "timeout": _remaining(end), "max_retries": 0},
        )
        source, url, headers = _capability(response.json(), sha256, size)
        with httpx.Client(transport=upload_transport, follow_redirects=False) as storage:
            _uploaded(storage.put(url, content=file, headers=headers, timeout=_remaining(end)))
        response = client.post(
            "/v1/images",
            cast_to=httpx.Response,
            body={"source": source, "platform": platform, **({"name": name} if name is not None else {})},
            options={"idempotency_key": key, "timeout": _remaining(end), "max_retries": 0},
        )
    image = _image(response.json())
    if not wait:
        _ready(image, on_progress)
        return image
    return poll_image(
        client, image, timeout=_remaining(end, image), poll_interval=poll_interval, on_progress=on_progress
    )


async def async_import_image(
    client: AsyncDedalus,
    path: Union[str, os.PathLike[str]],
    *,
    wait: bool = True,
    name: Optional[str] = None,
    platform: Literal["linux/amd64"] = "linux/amd64",
    timeout: float = 3600,
    poll_interval: float = 2,
    idempotency_key: Optional[str] = None,
    on_progress: Optional[Callable[[Image], None]] = None,
    upload_transport: Optional[httpx.AsyncBaseTransport] = None,
) -> Image:
    """Async import with automatic waiting; cancellation never deletes an image."""
    if platform != "linux/amd64":
        raise ValueError("Custom images currently require linux/amd64")
    end = time.monotonic() + _duration(timeout, "timeout")
    _duration(poll_interval, "poll_interval")
    key = idempotency_key or str(uuid4())
    image = None
    try:
        with anyio.fail_after(timeout):
            with open(path, "rb") as file:
                sha256, size = await anyio.to_thread.run_sync(_hash, file, end)
                response = await client.post(
                    "/v1/images/uploads",
                    cast_to=httpx.Response,
                    body={"sha256": sha256, "size_bytes": size, "platform": platform},
                    options={"idempotency_key": key},
                )
                source, url, headers = _capability(response.json(), sha256, size)

                async def chunks():
                    while True:
                        chunk = await anyio.to_thread.run_sync(file.read, 1024 * 1024)
                        if not chunk:
                            break
                        yield chunk

                async with httpx.AsyncClient(transport=upload_transport, follow_redirects=False) as storage:
                    _uploaded(await storage.put(url, content=chunks(), headers=headers, timeout=_remaining(end)))
                response = await client.post(
                    "/v1/images",
                    cast_to=httpx.Response,
                    body={"source": source, "platform": platform, **({"name": name} if name is not None else {})},
                    options={"idempotency_key": key},
                )
            image = _image(response.json())
            if not wait:
                _ready(image, on_progress)
                return image
            return await async_poll_image(
                client, image, timeout=_remaining(end, image), poll_interval=poll_interval, on_progress=on_progress
            )
    except TimeoutError:
        _remaining(end, image)
        raise
