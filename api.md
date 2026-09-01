# Machines

Types:

```python
from dedalus_sdk.types import (
    CreateParams,
    LifecycleStatus,
    Machine,
    MachineList,
    MachineListItem,
    UpdateParams,
    MachineRetrieveResponse,
)
```

Methods:

- <code title="post /v1/machines">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">create</a>(\*\*<a href="src/dedalus_sdk/types/machine_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="get /v1/machines/{machine_id}">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">retrieve</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine_retrieve_response.py">MachineRetrieveResponse</a></code>
- <code title="patch /v1/machines/{machine_id}">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">update</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machine_update_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="get /v1/machines">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">list</a>(\*\*<a href="src/dedalus_sdk/types/machine_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machine_list_item.py">SyncCursorPage[MachineListItem]</a></code>
- <code title="delete /v1/machines/{machine_id}">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">delete</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="post /v1/machines/{machine_id}/sleep">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">sleep</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="post /v1/machines/{machine_id}/wake">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">wake</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>

## SSH

Types:

```python
from dedalus_sdk.types.machines import (
    SSHConnection,
    SSHHostTrust,
    SSHSession,
    SSHSessionCreateParams,
    SSHSessionList,
)
```

Methods:

- <code title="post /v1/machines/{machine_id}/ssh">client.machines.ssh.<a href="./src/dedalus_sdk/resources/machines/ssh.py">create</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/ssh_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/ssh_session.py">SSHSession</a></code>
- <code title="get /v1/machines/{machine_id}/ssh/{session_id}">client.machines.ssh.<a href="./src/dedalus_sdk/resources/machines/ssh.py">retrieve</a>(\*, machine_id, session_id) -> <a href="./src/dedalus_sdk/types/machines/ssh_session.py">SSHSession</a></code>
- <code title="get /v1/machines/{machine_id}/ssh">client.machines.ssh.<a href="./src/dedalus_sdk/resources/machines/ssh.py">list</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/ssh_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/ssh_session.py">SyncCursorPage[SSHSession]</a></code>
- <code title="delete /v1/machines/{machine_id}/ssh/{session_id}">client.machines.ssh.<a href="./src/dedalus_sdk/resources/machines/ssh.py">delete</a>(\*, machine_id, session_id) -> <a href="./src/dedalus_sdk/types/machines/ssh_session.py">SSHSession</a></code>

## Executions

Types:

```python
from dedalus_sdk.types.machines import (
    ArtifactRef,
    Execution,
    ExecutionCreateParams,
    ExecutionEvent,
    ExecutionEvents,
    ExecutionList,
    ExecutionOutput,
)
```

Methods:

- <code title="post /v1/machines/{machine_id}/executions">client.machines.executions.<a href="./src/dedalus_sdk/resources/machines/executions.py">create</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/execution_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/execution.py">Execution</a></code>
- <code title="get /v1/machines/{machine_id}/executions/{execution_id}">client.machines.executions.<a href="./src/dedalus_sdk/resources/machines/executions.py">retrieve</a>(\*, machine_id, execution_id) -> <a href="./src/dedalus_sdk/types/machines/execution.py">Execution</a></code>
- <code title="get /v1/machines/{machine_id}/executions">client.machines.executions.<a href="./src/dedalus_sdk/resources/machines/executions.py">list</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/execution_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/execution.py">SyncCursorPage[Execution]</a></code>
- <code title="delete /v1/machines/{machine_id}/executions/{execution_id}">client.machines.executions.<a href="./src/dedalus_sdk/resources/machines/executions.py">delete</a>(\*, machine_id, execution_id) -> <a href="./src/dedalus_sdk/types/machines/execution.py">Execution</a></code>
- <code title="get /v1/machines/{machine_id}/executions/{execution_id}/events">client.machines.executions.<a href="./src/dedalus_sdk/resources/machines/executions.py">events</a>(\*, machine_id, execution_id, \*\*<a href="src/dedalus_sdk/types/machines/execution_events_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/execution_event.py">SyncCursorPage[ExecutionEvent]</a></code>
- <code title="get /v1/machines/{machine_id}/executions/{execution_id}/output">client.machines.executions.<a href="./src/dedalus_sdk/resources/machines/executions.py">output</a>(\*, machine_id, execution_id) -> <a href="./src/dedalus_sdk/types/machines/execution_output.py">ExecutionOutput</a></code>
