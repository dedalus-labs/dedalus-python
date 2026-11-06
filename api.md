# Dedalus Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Machines`](#machines)
  - [List machines](#list-machines)
  - [Create machine](#create-machine)
  - [Get machine](#get-machine)
  - [Update machine](#update-machine)
  - [Destroy machine](#destroy-machine)
  - [Sleep a running machine](#sleep-a-running-machine)
  - [Wake a sleeping machine](#wake-a-sleeping-machine)
  - [Reboot a machine with fresh memory](#reboot-a-machine-with-fresh-memory)
  - [Resize machine](#resize-machine)
  - [`Machines Ssh`](#machines-ssh)
    - [List SSH sessions](#list-ssh-sessions)
    - [Create SSH session](#create-ssh-session)
    - [Get SSH session](#get-ssh-session)
    - [Delete SSH session](#delete-ssh-session)
  - [`Machines Executions`](#machines-executions)
    - [List executions](#list-executions)
    - [Create execution](#create-execution)
    - [Get execution](#get-execution)
    - [Delete execution](#delete-execution)
    - [Get execution output](#get-execution-output)
    - [List execution events](#list-execution-events)
    - [`Machines Executions Logs`](#machines-executions-logs)
      - [Get execution log status](#get-execution-log-status)
      - [Create execution log read token](#create-execution-log-read-token)
  - [`Machines Autoresizing`](#machines-autoresizing)
    - [Read this machine's autoresizing settings](#read-this-machines-autoresizing-settings)
    - [Set this machine's autoresizing settings](#set-this-machines-autoresizing-settings)
- [`Organization`](#organization)
  - [`Organization Autoresizing`](#organization-autoresizing)
    - [Read organization autoresizing policy](#read-organization-autoresizing-policy)
    - [Set organization autoresizing policy](#set-organization-autoresizing-policy)
- [`Images`](#images)
  - [List image IDs owned by the authenticated organization](#list-image-ids-owned-by-the-authenticated-organization)
  - [Register an immutable OCI image for preparation](#register-an-immutable-oci-image-for-preparation)
  - [Read preparation status for an organization-owned image](#read-preparation-status-for-an-organization-owned-image)
  - [Rename an organization-owned image](#rename-an-organization-owned-image)
  - [Delete an organization-owned image](#delete-an-organization-owned-image)
  - [`Images Uploads`](#images-uploads)
    - [Reserve an immutable Docker image archive upload](#reserve-an-immutable-docker-image-archive-upload)

## Setup

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    browser_token=os.environ.get("DEDALUS_BROWSER_TOKEN"),
)
```

## `Machines`

### List machines

| Direction | Type |
| --- | --- |
| Request | [`MachineListParams`](./src/dedalus_sdk/types/machine_list_params.py) |

```python
page = client.machines.list()
```

### Create machine

| Direction | Type |
| --- | --- |
| Request | [`MachineCreateParams`](./src/dedalus_sdk/types/machine_create_params.py) |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.create(
    autosleep="300s",
    memory_mib=4096,
    storage_gib=10,
    vcpu=1,
    idempotency_key="",
)
```

### Get machine

| Direction | Type |
| --- | --- |
| Response | [`MachineRetrieveResponse`](./src/dedalus_sdk/types/machine_retrieve_response.py) |

```python
machine = client.machines.retrieve(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
)
```

### Update machine

Changes settings such as autosleep.

| Direction | Type |
| --- | --- |
| Request | [`MachineUpdateParams`](./src/dedalus_sdk/types/machine_update_params.py) |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.update(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

### Destroy machine

| Direction | Type |
| --- | --- |
| Request | [`MachineDeleteParams`](./src/dedalus_sdk/types/machine_delete_params.py) |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.delete(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

### Sleep a running machine

| Direction | Type |
| --- | --- |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.sleep(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

### Wake a sleeping machine

| Direction | Type |
| --- | --- |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.wake(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

### Reboot a machine with fresh memory

Checkpoints files and replaces the runtime. The machine ID and filesystem are preserved. RAM, processes, and temporary mounts are cleared. Poll the machine until its phase is running. Retry the same Idempotency-Key after a lost response.

| Direction | Type |
| --- | --- |
| Request | [`MachineRebootParams`](./src/dedalus_sdk/types/machine_reboot_params.py) |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.reboot(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

### Resize machine

Wakes a sleeping Machine, then waits up to 30 seconds for the host to confirm CPU and RAM. Returns the Machine with its confirmed size. After RESIZE_TIMEOUT, repeat the same request and Idempotency-Key to wait again.

| Direction | Type |
| --- | --- |
| Request | [`MachineResizeParams`](./src/dedalus_sdk/types/machine_resize_params.py) |
| Response | [`MachineResizeResponse`](./src/dedalus_sdk/types/machine_resize_response.py) |

```python
machine = client.machines.resize(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

### `Machines Ssh`

#### List SSH sessions

| Direction | Type |
| --- | --- |
| Request | [`SSHListParams`](./src/dedalus_sdk/types/machines/ssh_list_params.py) |

```python
page = client.machines.ssh.list(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
)
```

#### Create SSH session

| Direction | Type |
| --- | --- |
| Request | [`SSHCreateParams`](./src/dedalus_sdk/types/machines/ssh_create_params.py) |
| Response | [`SSHSession`](./src/dedalus_sdk/types/machines/ssh_session.py) |

```python
ssh = client.machines.ssh.create(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    public_key="",
    idempotency_key="",
)
```

#### Get SSH session

| Direction | Type |
| --- | --- |
| Response | [`SSHSession`](./src/dedalus_sdk/types/machines/ssh_session.py) |

```python
ssh = client.machines.ssh.retrieve(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    session_id="sessionID",
)
```

#### Delete SSH session

| Direction | Type |
| --- | --- |
| Response | [`SSHSession`](./src/dedalus_sdk/types/machines/ssh_session.py) |

```python
ssh = client.machines.ssh.delete(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    session_id="sessionID",
    idempotency_key="",
)
```

### `Machines Executions`

#### List executions

| Direction | Type |
| --- | --- |
| Request | [`ExecutionListParams`](./src/dedalus_sdk/types/machines/execution_list_params.py) |

```python
page = client.machines.executions.list(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
)
```

#### Create execution

| Direction | Type |
| --- | --- |
| Request | [`ExecutionCreateParams`](./src/dedalus_sdk/types/machines/execution_create_params.py) |
| Response | [`Execution`](./src/dedalus_sdk/types/machines/execution.py) |

```python
execution = client.machines.executions.create(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    command=[""],
    idempotency_key="",
)
```

#### Get execution

| Direction | Type |
| --- | --- |
| Response | [`Execution`](./src/dedalus_sdk/types/machines/execution.py) |

```python
execution = client.machines.executions.retrieve(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
)
```

#### Delete execution

| Direction | Type |
| --- | --- |
| Response | [`Execution`](./src/dedalus_sdk/types/machines/execution.py) |

```python
execution = client.machines.executions.delete(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
    idempotency_key="",
)
```

#### Get execution output

| Direction | Type |
| --- | --- |
| Response | [`ExecutionOutput`](./src/dedalus_sdk/types/machines/execution_output.py) |

```python
execution = client.machines.executions.output(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
)
```

#### List execution events

| Direction | Type |
| --- | --- |
| Request | [`ExecutionEventsParams`](./src/dedalus_sdk/types/machines/execution_events_params.py) |

```python
page = client.machines.executions.events(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
)
```

#### `Machines Executions Logs`

##### Get execution log status

| Direction | Type |
| --- | --- |
| Response | [`Status`](./src/dedalus_sdk/types/machines/executions/status.py) |

```python
log = client.machines.executions.logs.retrieve(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
)
```

##### Create execution log read token

| Direction | Type |
| --- | --- |
| Response | [`ReadToken`](./src/dedalus_sdk/types/machines/executions/read_token.py) |

```python
log = client.machines.executions.logs.create_token(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
    idempotency_key="",
)
```

### `Machines Autoresizing`

#### Read this machine's autoresizing settings

| Direction | Type |
| --- | --- |
| Response | [`Policy`](./src/dedalus_sdk/types/machines/policy.py) |

```python
autoresizing = client.machines.autoresizing.retrieve(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
)
```

#### Set this machine's autoresizing settings

Changes RAM, CPU or both for this machine. An absent resource keeps its setting.

| Direction | Type |
| --- | --- |
| Request | [`AutoresizingUpdateParams`](./src/dedalus_sdk/types/machines/autoresizing_update_params.py) |
| Response | [`Policy`](./src/dedalus_sdk/types/machines/policy.py) |

```python
autoresizing = client.machines.autoresizing.update(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    idempotency_key="",
)
```

## `Organization`

### `Organization Autoresizing`

#### Read organization autoresizing policy

| Direction | Type |
| --- | --- |
| Response | [`Policy`](./src/dedalus_sdk/types/machines/policy.py) |

```python
autoresizing = client.organization.autoresizing.retrieve()
```

#### Set organization autoresizing policy

Changes defaults copied to new Machines. Existing Machines retain their own policy.

| Direction | Type |
| --- | --- |
| Request | [`AutoresizingUpdateParams`](./src/dedalus_sdk/types/organization/autoresizing_update_params.py) |
| Response | [`Policy`](./src/dedalus_sdk/types/machines/policy.py) |

```python
autoresizing = client.organization.autoresizing.update(
    idempotency_key="",
)
```

## `Images`

### List image IDs owned by the authenticated organization

Pages through the organization's images in ID order. A deleted image is left out; it still reads by ID.

| Direction | Type |
| --- | --- |
| Request | [`ImageListParams`](./src/dedalus_sdk/types/image_list_params.py) |
| Response | [`ImageList`](./src/dedalus_sdk/types/image_list.py) |

```python
image = client.images.list(
    limit=100,
)
```

### Register an immutable OCI image for preparation

Requires an entitled organization and linux/amd64 on the current fleet. Acceptance queues preparation; only a ready image can launch a machine. Private registry credentials are not yet supported.

| Direction | Type |
| --- | --- |
| Request | [`ImageCreateParams`](./src/dedalus_sdk/types/image_create_params.py) |
| Response | [`Image`](./src/dedalus_sdk/types/image.py) |

```python
image = client.images.create(
    platform="linux/amd64",
    source={"kind": ""},
    idempotency_key="",
)
```

### Read preparation status for an organization-owned image

A preparing image reports its stage, the worker's last step and an estimated percent of the whole preparation. A failed image names the cause: IMAGE_OS_UNSUPPORTED, IMAGE_SOURCE_INVALID, IMAGE_SOURCE_NOT_FOUND and IMAGE_SOURCE_UNAUTHORIZED describe the image or its reference and are final; IMAGE_SOURCE_UNAVAILABLE, IMAGE_REGISTRY_UNREACHABLE, IMAGE_REGISTRY_RATE_LIMITED, IMAGE_ARCHIVE_UNAVAILABLE and IMAGE_EXECUTION_FAILED describe this attempt and are retryable with a new idempotency key.

| Direction | Type |
| --- | --- |
| Response | [`Image`](./src/dedalus_sdk/types/image.py) |

```python
image = client.images.retrieve(
    image_id="imageID",
)
```

### Rename an organization-owned image

Changes only the name. The image's source, platform and state are immutable.

| Direction | Type |
| --- | --- |
| Request | [`ImageUpdateParams`](./src/dedalus_sdk/types/image_update_params.py) |
| Response | [`Image`](./src/dedalus_sdk/types/image.py) |

```python
image = client.images.update(
    image_id="imageID",
    name="",
    idempotency_key="",
)
```

### Delete an organization-owned image

The image can create no new Machine and no longer counts against the organization's image limit. Machines already running from it keep working. The image stays readable, and deleting it again returns the same image.

| Direction | Type |
| --- | --- |
| Response | [`Image`](./src/dedalus_sdk/types/image.py) |

```python
image = client.images.delete(
    image_id="imageID",
    idempotency_key="",
)
```

### `Images Uploads`

#### Reserve an immutable Docker image archive upload

| Direction | Type |
| --- | --- |
| Request | [`UploadCreateParams`](./src/dedalus_sdk/types/images/upload_create_params.py) |
| Response | [`Reservation`](./src/dedalus_sdk/types/images/reservation.py) |

```python
upload = client.images.uploads.create(
    platform="",
    sha256="",
    size_bytes=0,
    idempotency_key="",
)
```
