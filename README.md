# Dedalus

This library provides convenient access to the Dedalus REST API from Python.

The full API of this library can be found in [api.md](./api.md).

<br />

## Contents

- [Installation](#installation)
- [Usage](#usage)
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

## Usage

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    x_api_key=os.environ.get("DEDALUS_X_API_KEY"),
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
| `x_api_key` | `string \| provider` | - | Dedalus API key. Alternative to Bearer token. Defaults to DEDALUS_X_API_KEY. |
| `api_key` | `string \| provider` | - | Dedalus API key or short-lived delegated access token in Authorization: Bearer <credential>. Defaults to DEDALUS_API_KEY. |

Declared schemes:

- `ApiKeyAuth` API key in header `x-api-key`
- `BearerAuth` bearer token

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

Documented error statuses: `401`, `403`, `409`, `429`, `503`, `default`.

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
| `api_key` | `str \| None` | `os.environ.get("DEDALUS_API_KEY")` | Dedalus API key or short-lived delegated access token in Authorization: Bearer <credential>. |
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

<br />

## Requirements

- Python 3.8 or newer

Powered by Scalar.
