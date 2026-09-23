---
name: dedalus-python-sdk
description: "Python SDK for Dedalus API. Use when writing Python code that calls Dedalus API with the dedalus-sdk package: installing it, constructing and authenticating the client, and calling API operations."
---

# Dedalus Python SDK

Generated Python client for Dedalus API, published as `dedalus-sdk`. Use the generated client instead of hand-writing HTTP requests.

## Install

```sh
pip install dedalus-sdk
```

## Client setup and authentication

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    api_key=os.environ.get("DEDALUS_API_KEY"),
)
```

Provide credentials using the options below. Environment variables are read automatically when the target runtime supports them:

- `x_api_key` (env: `DEDALUS_X_API_KEY`) — API key authentication using X-API-Key header
- `bearer_auth` (env: `DEDALUS_BEARER_AUTH`) — Dedalus API key or short-lived delegated access token in Authorization: Bearer <credential>.
- `api_key` (env: `DEDALUS_API_KEY`) — API key authentication using Bearer token

## Calling operations

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    api_key=os.environ.get("DEDALUS_API_KEY"),
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

Method names, parameter shapes, and response types are generated from the API description — do not guess them. Look up the exact call signature in [api.md](../../../api.md) before writing a call.

## Pagination

List endpoints return paginated results you can iterate directly; the SDK fetches subsequent pages for you.

```python
page = client.machines.list()
```

## WebSockets

WebSocket endpoints open a persistent connection you can send messages to and receive messages from.

```python
with client.machines.terminals.connect(machine_id="machineID", terminal_id="terminalID") as connection:
    message = connection.recv()
    print(message)
```

## Error handling

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

## Requirements

- Python 3.8 or newer

## Reference files

- [README.md](../../../README.md) — full feature tour: client options, retries and timeouts, logging.
- [api.md](../../../api.md) — complete catalogue of every operation with request and response types.
