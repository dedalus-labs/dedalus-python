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
      - [Reauthorize execution log publication](#reauthorize-execution-log-publication)
      - [Create execution log read token](#create-execution-log-read-token)
  - [`Machines Autoresizing`](#machines-autoresizing)
    - [Read this machine's RAM autoresizing settings](#read-this-machines-ram-autoresizing-settings)
    - [Set this machine's RAM autoresizing settings](#set-this-machines-ram-autoresizing-settings)
- [`Organization`](#organization)
  - [`Organization Autoresizing`](#organization-autoresizing)
    - [Read organization RAM autoresizing policy](#read-organization-ram-autoresizing-policy)
    - [Set organization RAM autoresizing policy](#set-organization-ram-autoresizing-policy)

## Setup

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    x_api_key=os.environ.get("DEDALUS_X_API_KEY"),
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

##### Reauthorize execution log publication

| Direction | Type |
| --- | --- |
| Response | [`Status`](./src/dedalus_sdk/types/machines/executions/status.py) |

```python
log = client.machines.executions.logs.reauthorize(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    execution_id="executionID",
    idempotency_key="",
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

#### Read this machine's RAM autoresizing settings

| Direction | Type |
| --- | --- |
| Response | [`Settings`](./src/dedalus_sdk/types/machines/settings.py) |

```python
autoresizing = client.machines.autoresizing.retrieve(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
)
```

#### Set this machine's RAM autoresizing settings

| Direction | Type |
| --- | --- |
| Request | [`AutoresizingUpdateParams`](./src/dedalus_sdk/types/machines/autoresizing_update_params.py) |
| Response | [`Settings`](./src/dedalus_sdk/types/machines/settings.py) |

```python
autoresizing = client.machines.autoresizing.update(
    machine_id="017f22e2-79b0-7cc3-98c4-dc0c0c07398f",
    enabled=False,
    idempotency_key="",
)
```

## `Organization`

### `Organization Autoresizing`

#### Read organization RAM autoresizing policy

| Direction | Type |
| --- | --- |
| Response | [`Policy`](./src/dedalus_sdk/types/organization/policy.py) |

```python
autoresizing = client.organization.autoresizing.retrieve()
```

#### Set organization RAM autoresizing policy

| Direction | Type |
| --- | --- |
| Request | [`AutoresizingUpdateParams`](./src/dedalus_sdk/types/organization/autoresizing_update_params.py) |
| Response | [`Policy`](./src/dedalus_sdk/types/organization/policy.py) |

```python
autoresizing = client.organization.autoresizing.update(
    enabled=False,
    idempotency_key="",
)
```
