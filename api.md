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
  - [`Machines Terminals`](#machines-terminals)
    - [`connect`](#connect)

## Setup

```python
import os

from dedalus_sdk import Dedalus

client = Dedalus(
    api_key=os.environ.get("DEDALUS_API_KEY"),
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

### `Machines Terminals`

#### `connect`

```python
with client.machines.terminals.connect(machine_id="machineID", terminal_id="terminalID") as connection:
    message = connection.recv()
    print(message)
```
