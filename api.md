# Dedalus Python API

Complete reference of every operation, grouped by resource. See [the README](./README.md) for usage and configuration.

## Contents

- [`Machines`](#machines)
  - [List machines](#list-machines)
  - [Create machine](#create-machine)
  - [Get machine](#get-machine)
  - [Update machine](#update-machine)
  - [Destroy machine](#destroy-machine)
  - [Watch machine lifecycle status](#watch-machine-lifecycle-status)
  - [Sleep a running machine](#sleep-a-running-machine)
  - [Wake a sleeping machine](#wake-a-sleeping-machine)
  - [`Machines Network`](#machines-network)
    - [Get machine network identity](#get-machine-network-identity)
  - [`Machines Artifacts`](#machines-artifacts)
    - [List artifacts](#list-artifacts)
    - [Get artifact](#get-artifact)
    - [Delete artifact](#delete-artifact)
  - [`Machines Ports`](#machines-ports)
    - [List ports](#list-ports)
    - [Create port](#create-port)
    - [Get port](#get-port)
    - [Delete port](#delete-port)
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
    - [List terminals](#list-terminals)
    - [Create terminal](#create-terminal)
    - [Get terminal](#get-terminal)
    - [Delete terminal](#delete-terminal)
    - [Connect to terminal WebSocket stream](#connect-to-terminal-websocket-stream)
- [`Networks`](#networks)
  - [Get network details](#get-network-details)
- [`Usage`](#usage)
  - [Get usage summary](#get-usage-summary)
  - [List machine compute usage breakdown](#list-machine-compute-usage-breakdown)
  - [List machine storage usage breakdown](#list-machine-storage-usage-breakdown)

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
    machine_id="machineID",
)
```

### Update machine

| Direction | Type |
| --- | --- |
| Request | [`MachineUpdateParams`](./src/dedalus_sdk/types/machine_update_params.py) |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.update(
    machine_id="machineID",
    idempotency_key="",
)
```

### Destroy machine

| Direction | Type |
| --- | --- |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.delete(
    machine_id="machineID",
    idempotency_key="",
)
```

### Watch machine lifecycle status

Streams machine lifecycle updates over Server-Sent Events. Each `status` event contains a full `LifecycleResponse` payload. The stream closes after the machine reaches its current desired state.

| Direction | Type |
| --- | --- |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
stream = client.machines.watch(
    machine_id="machineID",
)

for machine in stream:
    print(machine)
```

### Sleep a running machine

| Direction | Type |
| --- | --- |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.sleep(
    machine_id="machineID",
    idempotency_key="",
)
```

### Wake a sleeping machine

| Direction | Type |
| --- | --- |
| Response | [`Machine`](./src/dedalus_sdk/types/machine.py) |

```python
machine = client.machines.wake(
    machine_id="machineID",
    idempotency_key="",
)
```

### `Machines Network`

#### Get machine network identity

| Direction | Type |
| --- | --- |
| Response | [`MachineNetwork`](./src/dedalus_sdk/types/machines/machine_network.py) |

```python
network = client.machines.network.retrieve(
    machine_id="machineID",
)
```

### `Machines Artifacts`

#### List artifacts

| Direction | Type |
| --- | --- |
| Request | [`ArtifactListParams`](./src/dedalus_sdk/types/machines/artifact_list_params.py) |

```python
page = client.machines.artifacts.list(
    machine_id="machineID",
)
```

#### Get artifact

| Direction | Type |
| --- | --- |
| Response | [`Artifact`](./src/dedalus_sdk/types/machines/artifact.py) |

```python
artifact = client.machines.artifacts.retrieve(
    machine_id="machineID",
    artifact_id="artifactID",
)
```

#### Delete artifact

| Direction | Type |
| --- | --- |
| Response | [`Artifact`](./src/dedalus_sdk/types/machines/artifact.py) |

```python
artifact = client.machines.artifacts.delete(
    machine_id="machineID",
    artifact_id="artifactID",
    idempotency_key="",
)
```

### `Machines Ports`

#### List ports

| Direction | Type |
| --- | --- |
| Request | [`PortListParams`](./src/dedalus_sdk/types/machines/port_list_params.py) |

```python
page = client.machines.ports.list(
    machine_id="machineID",
)
```

#### Create port

| Direction | Type |
| --- | --- |
| Request | [`PortCreateParams`](./src/dedalus_sdk/types/machines/port_create_params.py) |
| Response | [`Port`](./src/dedalus_sdk/types/machines/port.py) |

```python
port = client.machines.ports.create(
    machine_id="machineID",
    port=0,
    idempotency_key="",
)
```

#### Get port

| Direction | Type |
| --- | --- |
| Response | [`Port`](./src/dedalus_sdk/types/machines/port.py) |

```python
port = client.machines.ports.retrieve(
    machine_id="machineID",
    port_id="portID",
)
```

#### Delete port

| Direction | Type |
| --- | --- |
| Response | [`Port`](./src/dedalus_sdk/types/machines/port.py) |

```python
port = client.machines.ports.delete(
    machine_id="machineID",
    port_id="portID",
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
    machine_id="machineID",
)
```

#### Create SSH session

| Direction | Type |
| --- | --- |
| Request | [`SSHCreateParams`](./src/dedalus_sdk/types/machines/ssh_create_params.py) |
| Response | [`SSHSession`](./src/dedalus_sdk/types/machines/ssh_session.py) |

```python
ssh = client.machines.ssh.create(
    machine_id="machineID",
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
    machine_id="machineID",
    session_id="sessionID",
)
```

#### Delete SSH session

| Direction | Type |
| --- | --- |
| Response | [`SSHSession`](./src/dedalus_sdk/types/machines/ssh_session.py) |

```python
ssh = client.machines.ssh.delete(
    machine_id="machineID",
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
    machine_id="machineID",
)
```

#### Create execution

| Direction | Type |
| --- | --- |
| Request | [`ExecutionCreateParams`](./src/dedalus_sdk/types/machines/execution_create_params.py) |
| Response | [`Execution`](./src/dedalus_sdk/types/machines/execution.py) |

```python
execution = client.machines.executions.create(
    machine_id="machineID",
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
    machine_id="machineID",
    execution_id="executionID",
)
```

#### Delete execution

| Direction | Type |
| --- | --- |
| Response | [`Execution`](./src/dedalus_sdk/types/machines/execution.py) |

```python
execution = client.machines.executions.delete(
    machine_id="machineID",
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
    machine_id="machineID",
    execution_id="executionID",
)
```

#### List execution events

| Direction | Type |
| --- | --- |
| Request | [`ExecutionEventsParams`](./src/dedalus_sdk/types/machines/execution_events_params.py) |

```python
page = client.machines.executions.events(
    machine_id="machineID",
    execution_id="executionID",
)
```

### `Machines Terminals`

#### List terminals

| Direction | Type |
| --- | --- |
| Request | [`TerminalListParams`](./src/dedalus_sdk/types/machines/terminal_list_params.py) |

```python
page = client.machines.terminals.list(
    machine_id="machineID",
)
```

#### Create terminal

| Direction | Type |
| --- | --- |
| Request | [`TerminalCreateParams`](./src/dedalus_sdk/types/machines/terminal_create_params.py) |
| Response | [`Terminal`](./src/dedalus_sdk/types/machines/terminal.py) |

```python
terminal = client.machines.terminals.create(
    machine_id="machineID",
    height=0,
    width=0,
    idempotency_key="",
)
```

#### Get terminal

| Direction | Type |
| --- | --- |
| Response | [`Terminal`](./src/dedalus_sdk/types/machines/terminal.py) |

```python
terminal = client.machines.terminals.retrieve(
    machine_id="machineID",
    terminal_id="terminalID",
)
```

#### Delete terminal

| Direction | Type |
| --- | --- |
| Response | [`Terminal`](./src/dedalus_sdk/types/machines/terminal.py) |

```python
terminal = client.machines.terminals.delete(
    machine_id="machineID",
    terminal_id="terminalID",
    idempotency_key="",
)
```

#### Connect to terminal WebSocket stream

Upgrades to a WebSocket connection for interactive terminal I/O. Clients send JSON `TerminalClientEvent` messages and receive JSON `TerminalServerEvent` messages. Terminal byte streams are base64-encoded inside `input` and `output` events; `resize` events use integer `width` and `height` fields.

```python
with client.machines.terminals.connect(machine_id="machineID", terminal_id="terminalID") as connection:
    message = connection.recv()
    print(message)
```

## `Networks`

### Get network details

| Direction | Type |
| --- | --- |
| Response | [`Network`](./src/dedalus_sdk/types/network.py) |

```python
network = client.networks.retrieve(
    network_id="networkID",
)
```

## `Usage`

### Get usage summary

| Direction | Type |
| --- | --- |
| Request | [`UsageRetrieveParams`](./src/dedalus_sdk/types/usage_retrieve_params.py) |
| Response | [`OrgUsage`](./src/dedalus_sdk/types/org_usage.py) |

```python
usage = client.usage.retrieve()
```

### List machine compute usage breakdown

| Direction | Type |
| --- | --- |
| Request | [`UsageMachineComputeParams`](./src/dedalus_sdk/types/usage_machine_compute_params.py) |
| Response | [`MachineComputeUsage`](./src/dedalus_sdk/types/machine_compute_usage.py) |

```python
usage = client.usage.machine_compute()
```

### List machine storage usage breakdown

| Direction | Type |
| --- | --- |
| Request | [`UsageMachineStorageParams`](./src/dedalus_sdk/types/usage_machine_storage_params.py) |
| Response | [`MachineStorageUsage`](./src/dedalus_sdk/types/machine_storage_usage.py) |

```python
usage = client.usage.machine_storage()
```
