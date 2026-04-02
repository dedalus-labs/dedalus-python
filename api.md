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
)
```

Methods:

- <code title="post /v1/machines">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">create</a>(\*\*<a href="src/dedalus_sdk/types/machine_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="get /v1/machines/{machine_id}">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">retrieve</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="patch /v1/machines/{machine_id}">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">update</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machine_update_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="get /v1/machines">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">list</a>(\*\*<a href="src/dedalus_sdk/types/machine_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machine_list_item.py">SyncCursorPage[MachineListItem]</a></code>
- <code title="delete /v1/machines/{machine_id}">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">delete</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="post /v1/machines/{machine_id}/sleep">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">sleep</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="post /v1/machines/{machine_id}/wake">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">wake</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>
- <code title="get /v1/machines/{machine_id}/status/stream">client.machines.<a href="./src/dedalus_sdk/resources/machines/machines.py">watch</a>(\*, machine_id) -> <a href="./src/dedalus_sdk/types/machine.py">Machine</a></code>

## Artifacts

Types:

```python
from dedalus_sdk.types.machines import Artifact, ArtifactList
```

Methods:

- <code title="get /v1/machines/{machine_id}/artifacts/{artifact_id}">client.machines.artifacts.<a href="./src/dedalus_sdk/resources/machines/artifacts.py">retrieve</a>(\*, machine_id, artifact_id) -> <a href="./src/dedalus_sdk/types/machines/artifact.py">Artifact</a></code>
- <code title="get /v1/machines/{machine_id}/artifacts">client.machines.artifacts.<a href="./src/dedalus_sdk/resources/machines/artifacts.py">list</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/artifact_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/artifact.py">SyncCursorPage[Artifact]</a></code>
- <code title="delete /v1/machines/{machine_id}/artifacts/{artifact_id}">client.machines.artifacts.<a href="./src/dedalus_sdk/resources/machines/artifacts.py">delete</a>(\*, machine_id, artifact_id) -> <a href="./src/dedalus_sdk/types/machines/artifact.py">Artifact</a></code>

## Previews

Types:

```python
from dedalus_sdk.types.machines import Preview, PreviewCreateParams, PreviewList
```

Methods:

- <code title="post /v1/machines/{machine_id}/previews">client.machines.previews.<a href="./src/dedalus_sdk/resources/machines/previews.py">create</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/preview_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/preview.py">Preview</a></code>
- <code title="get /v1/machines/{machine_id}/previews/{preview_id}">client.machines.previews.<a href="./src/dedalus_sdk/resources/machines/previews.py">retrieve</a>(\*, machine_id, preview_id) -> <a href="./src/dedalus_sdk/types/machines/preview.py">Preview</a></code>
- <code title="get /v1/machines/{machine_id}/previews">client.machines.previews.<a href="./src/dedalus_sdk/resources/machines/previews.py">list</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/preview_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/preview.py">SyncCursorPage[Preview]</a></code>
- <code title="delete /v1/machines/{machine_id}/previews/{preview_id}">client.machines.previews.<a href="./src/dedalus_sdk/resources/machines/previews.py">delete</a>(\*, machine_id, preview_id) -> <a href="./src/dedalus_sdk/types/machines/preview.py">Preview</a></code>

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

## Terminals

Types:

```python
from dedalus_sdk.types.machines import (
    Terminal,
    TerminalClientEvent,
    TerminalClosedEvent,
    TerminalCreateParams,
    TerminalErrorEvent,
    TerminalInputEvent,
    TerminalList,
    TerminalOutputEvent,
    TerminalResizeEvent,
    TerminalServerEvent,
)
```

Methods:

- <code title="post /v1/machines/{machine_id}/terminals">client.machines.terminals.<a href="./src/dedalus_sdk/resources/machines/terminals.py">create</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/terminal_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/terminal.py">Terminal</a></code>
- <code title="get /v1/machines/{machine_id}/terminals/{terminal_id}">client.machines.terminals.<a href="./src/dedalus_sdk/resources/machines/terminals.py">retrieve</a>(\*, machine_id, terminal_id) -> <a href="./src/dedalus_sdk/types/machines/terminal.py">Terminal</a></code>
- <code title="get /v1/machines/{machine_id}/terminals">client.machines.terminals.<a href="./src/dedalus_sdk/resources/machines/terminals.py">list</a>(\*, machine_id, \*\*<a href="src/dedalus_sdk/types/machines/terminal_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/machines/terminal.py">SyncCursorPage[Terminal]</a></code>
- <code title="delete /v1/machines/{machine_id}/terminals/{terminal_id}">client.machines.terminals.<a href="./src/dedalus_sdk/resources/machines/terminals.py">delete</a>(\*, machine_id, terminal_id) -> <a href="./src/dedalus_sdk/types/machines/terminal.py">Terminal</a></code>
