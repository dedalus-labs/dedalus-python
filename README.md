# Dedalus

This library provides convenient access to the Dedalus REST API from Python.

The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
- [Image import](#image-import)
- [API Reference](./api.md)
- [Async](#async)
- [Authentication](#authentication)
- [Errors](#errors)
- [Client Options](#client-options)
- [Retries and Timeouts](#retries-and-timeouts)
- [Pagination](#pagination)
- [Helpers](#helpers)
- [Logging](#logging)
- [Requirements](#requirements)

<br />

## Installation

```sh
pip install dedalus-sdk
```

<br />

## Image import

```python
from dedalus_sdk import Dedalus
from dedalus_sdk.images import import_image, poll_image

with Dedalus() as client:
    ready = import_image(client, "my-app.tar", name="my-app", platform="linux/amd64")

    # Return after upload and registration, then wait later.
    accepted = import_image(client, "my-app.tar", wait=False)
    image = poll_image(client, accepted["image_id"])
```

Async clients use `async_import_image` and `async_poll_image` with the same options:

```python
from dedalus_sdk import AsyncDedalus
from dedalus_sdk.images import async_import_image

async with AsyncDedalus() as client:
    ready = await async_import_image(client, "my-app.tar")
```

The helpers stream a `docker save` archive, register it, and wait for readiness by
default. Set `wait=False` to return after registration. `timeout` defaults to 3,600
seconds for the import and `poll_interval` defaults to 2 seconds. `on_progress`
receives each observed image. `ImagePreparationError.image` preserves the image ID
on terminal failure or polling deadline expiry; timeout or task cancellation does
not cancel server preparation.

The synchronous helper checks its deadline between I/O operations, uses the
remaining budget for request inactivity timeouts, and disables automatic API
retries. The async helper enforces its deadline with task cancellation and retains
the client's retry policy. Use the same `idempotency_key` when retrying an import
with unchanged input.

Archives must be regular, nonempty files of at most 5 GiB. Storage uploads use a
separate HTTP client without API credentials. The helpers require the image API
to be deployed and enabled for your organization; they do not bypass access controls.

Custom image imports currently require an Ubuntu 24.04 `linux/amd64` Docker-save
archive. On Apple silicon, build or pull with `--platform linux/amd64` before
saving the archive. The image provides the filesystem; container entrypoint,
CMD, environment, working directory, and user settings are not applied. Start
processes using Machine exec or SSH after the Machine reaches running.

## Usage

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    browser_token=os.environ.get("DEDALUS_BROWSER_TOKEN"),
)

machine = client.machines.create(
    autosleep="300s",
    memory_mib=4096,
    storage_gib=10,
    vcpu=1,
    idempotency_key="",
)

print(machine.machine_id)
```

The examples in the following sections assume a `client` configured as shown above.

See the [API reference](./api.md) for every available operation.

<br />

## Async

Every client has an `Async` counterpart (`AsyncDedalus`) exposing the same resource tree with `await`.

```python
import asyncio

from dedalus_sdk import AsyncDedalus


async def main() -> None:
    client = AsyncDedalus()
    machine = await client.machines.create(
        autosleep="300s",
        memory_mib=4096,
        storage_gib=10,
        vcpu=1,
        idempotency_key="",
    )


asyncio.run(main())
```

<br />

## Authentication

Pass credentials to the generated client constructor. Environment variables are read automatically when supported by the target runtime.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `x_api_key` | `str \| None` | - | Dedalus API key. Alternative to Bearer token. Defaults to DEDALUS_X_API_KEY. |
| `api_key` | `str \| None` | - | Dedalus API key or short-lived delegated access token in `Authorization: Bearer <credential>`. Defaults to DEDALUS_API_KEY. |
| `browser_token` | `str \| None` | - | Credential for the BrowserAuth scheme. Defaults to DEDALUS_BROWSER_TOKEN. |

Declared schemes:

- `ApiKeyAuth` API key in header `x-api-key`
- `BearerAuth` bearer token
- `BrowserAuth` OAuth2/OpenID Connect

<br />

## Errors

Non-success responses throw generated API errors. Error objects expose status, headers, response body, and request metadata where the target runtime supports it.

```python
from dedalus_sdk import APIStatusError

try:
    machine = client.machines.create(
        autosleep="300s",
        memory_mib=4096,
        storage_gib=10,
        vcpu=1,
        idempotency_key="",
    )
except APIStatusError as err:
    print(err.status_code, err.message)
    raise
```

Documented error statuses: `400`, `401`, `402`, `403`, `404`, `409`, `422`, `429`, `500`, `503`, `504`, `default`.

<br />

## Client Options

Configure the generated client by setting any of these options when you create it.

```python
from dedalus_sdk import Dedalus

client = Dedalus(
    timeout=60.0,
    max_retries=2,
)
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `x_api_key` | `str \| None` | `os.environ.get("DEDALUS_X_API_KEY")` | Dedalus API key. Alternative to Bearer token. |
| `api_key` | `str \| None` | `os.environ.get("DEDALUS_API_KEY")` | Dedalus API key or short-lived delegated access token in `Authorization: Bearer <credential>`. |
| `browser_token` | `str \| None` | `os.environ.get("DEDALUS_BROWSER_TOKEN")` | Credential for the BrowserAuth scheme. |
| `base_url` | `str \| httpx.URL \| None` | - | Override the default API base URL. |
| `timeout` | `float \| Timeout \| None` | `60.0` | Maximum time in seconds to wait for a response before aborting a request. |
| `max_retries` | `int` | `2` | Number of retries for temporary failures. |
| `default_headers` | `Mapping[str, str] \| None` | - | Headers sent with every request. |
| `default_query` | `Mapping[str, object] \| None` | - | Query parameters sent with every request. |

<br />

## Retries and Timeouts

Generated clients support request timeouts and retry temporary failures such as network errors, 408, 409, 429, and 5xx responses. Retry delays honor `Retry-After` headers when present. Tune the retry and timeout client options shown above, or override them per request.

<br />

## Pagination

List endpoints return paginated results you can iterate directly; the SDK fetches subsequent pages for you.

```python
page = client.machines.list()
```

<br />

## Helpers

- Use `client.with_raw_response.<resource>.<method>(...)` to access the raw `httpx.Response` and parse it yourself.
- Use `client.with_streaming_response.<resource>.<method>(...)` to stream a response body without buffering it.

<br />

## Logging

- Set the `DEDALUS_LOG` environment variable to `info` or `debug` to enable HTTP logging.
- Logs are emitted through the standard `logging` module under the `dedalus_sdk` logger.
- Importing the SDK wraps the process's log record factory: records from the SDK, `httpx`, `httpcore`, `hpack` and `websockets` loggers have credential headers, credential query parameters and URL userinfo logged as `***`. A record factory installed later that does not chain to the previous one turns this off.

<br />

## Requirements

- Python 3.9 or newer

Powered by Scalar.
