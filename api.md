# Workspaces

Types:

```python
from dedalus_sdk.types import CreateParams, LifecycleStatus, UpdateParams, Workspace, WorkspaceList
```

Methods:

- <code title="post /v1/workspaces">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces/workspaces.py">create</a>(\*\*<a href="src/dedalus_sdk/types/workspace_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
- <code title="get /v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
- <code title="patch /v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces/workspaces.py">update</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspace_update_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
- <code title="get /v1/workspaces">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces/workspaces.py">list</a>(\*\*<a href="src/dedalus_sdk/types/workspace_list_params.py">params</a>) -> SyncCursorPage[Item]</code>
- <code title="delete /v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces/workspaces.py">delete</a>(workspace_id) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>

## Artifacts

Types:

```python
from dedalus_sdk.types.workspaces import Artifact, ArtifactList
```

Methods:

- <code title="get /v1/workspaces/{workspace_id}/artifacts/{artifact_id}">client.workspaces.artifacts.<a href="./src/dedalus_sdk/resources/workspaces/artifacts.py">retrieve</a>(artifact_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/artifact.py">Artifact</a></code>
- <code title="get /v1/workspaces/{workspace_id}/artifacts">client.workspaces.artifacts.<a href="./src/dedalus_sdk/resources/workspaces/artifacts.py">list</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/artifact_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/artifact.py">SyncCursorPage[Artifact]</a></code>
- <code title="delete /v1/workspaces/{workspace_id}/artifacts/{artifact_id}">client.workspaces.artifacts.<a href="./src/dedalus_sdk/resources/workspaces/artifacts.py">delete</a>(artifact_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/artifact.py">Artifact</a></code>

## Previews

Types:

```python
from dedalus_sdk.types.workspaces import Preview, PreviewCreateParams, PreviewList
```

Methods:

- <code title="post /v1/workspaces/{workspace_id}/previews">client.workspaces.previews.<a href="./src/dedalus_sdk/resources/workspaces/previews.py">create</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/preview_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/preview.py">Preview</a></code>
- <code title="get /v1/workspaces/{workspace_id}/previews/{preview_id}">client.workspaces.previews.<a href="./src/dedalus_sdk/resources/workspaces/previews.py">retrieve</a>(preview_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/preview.py">Preview</a></code>
- <code title="get /v1/workspaces/{workspace_id}/previews">client.workspaces.previews.<a href="./src/dedalus_sdk/resources/workspaces/previews.py">list</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/preview_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/preview.py">SyncCursorPage[Preview]</a></code>
- <code title="delete /v1/workspaces/{workspace_id}/previews/{preview_id}">client.workspaces.previews.<a href="./src/dedalus_sdk/resources/workspaces/previews.py">delete</a>(preview_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/preview.py">Preview</a></code>

## SSH

Types:

```python
from dedalus_sdk.types.workspaces import (
    SSHConnection,
    SSHHostTrust,
    SSHSession,
    SSHSessionCreateParams,
    SSHSessionList,
)
```

Methods:

- <code title="post /v1/workspaces/{workspace_id}/ssh">client.workspaces.ssh.<a href="./src/dedalus_sdk/resources/workspaces/ssh.py">create</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/ssh_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/ssh_session.py">SSHSession</a></code>
- <code title="get /v1/workspaces/{workspace_id}/ssh/{session_id}">client.workspaces.ssh.<a href="./src/dedalus_sdk/resources/workspaces/ssh.py">retrieve</a>(session_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/ssh_session.py">SSHSession</a></code>
- <code title="get /v1/workspaces/{workspace_id}/ssh">client.workspaces.ssh.<a href="./src/dedalus_sdk/resources/workspaces/ssh.py">list</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/ssh_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/ssh_session.py">SyncCursorPage[SSHSession]</a></code>
- <code title="delete /v1/workspaces/{workspace_id}/ssh/{session_id}">client.workspaces.ssh.<a href="./src/dedalus_sdk/resources/workspaces/ssh.py">delete</a>(session_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/ssh_session.py">SSHSession</a></code>

## Executions

Types:

```python
from dedalus_sdk.types.workspaces import (
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

- <code title="post /v1/workspaces/{workspace_id}/executions">client.workspaces.executions.<a href="./src/dedalus_sdk/resources/workspaces/executions.py">create</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/execution_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/execution.py">Execution</a></code>
- <code title="get /v1/workspaces/{workspace_id}/executions/{execution_id}">client.workspaces.executions.<a href="./src/dedalus_sdk/resources/workspaces/executions.py">retrieve</a>(execution_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/execution.py">Execution</a></code>
- <code title="get /v1/workspaces/{workspace_id}/executions">client.workspaces.executions.<a href="./src/dedalus_sdk/resources/workspaces/executions.py">list</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/execution_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/execution.py">SyncCursorPage[Execution]</a></code>
- <code title="delete /v1/workspaces/{workspace_id}/executions/{execution_id}">client.workspaces.executions.<a href="./src/dedalus_sdk/resources/workspaces/executions.py">delete</a>(execution_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/execution.py">Execution</a></code>
- <code title="get /v1/workspaces/{workspace_id}/executions/{execution_id}/events">client.workspaces.executions.<a href="./src/dedalus_sdk/resources/workspaces/executions.py">events</a>(execution_id, \*, workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/execution_events_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/execution_event.py">SyncCursorPage[ExecutionEvent]</a></code>
- <code title="get /v1/workspaces/{workspace_id}/executions/{execution_id}/output">client.workspaces.executions.<a href="./src/dedalus_sdk/resources/workspaces/executions.py">output</a>(execution_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/execution_output.py">ExecutionOutput</a></code>

## Terminals

Types:

```python
from dedalus_sdk.types.workspaces import (
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

- <code title="post /v1/workspaces/{workspace_id}/terminals">client.workspaces.terminals.<a href="./src/dedalus_sdk/resources/workspaces/terminals.py">create</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/terminal_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/terminal.py">Terminal</a></code>
- <code title="get /v1/workspaces/{workspace_id}/terminals/{terminal_id}">client.workspaces.terminals.<a href="./src/dedalus_sdk/resources/workspaces/terminals.py">retrieve</a>(terminal_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/terminal.py">Terminal</a></code>
- <code title="get /v1/workspaces/{workspace_id}/terminals">client.workspaces.terminals.<a href="./src/dedalus_sdk/resources/workspaces/terminals.py">list</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspaces/terminal_list_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspaces/terminal.py">SyncCursorPage[Terminal]</a></code>
- <code title="delete /v1/workspaces/{workspace_id}/terminals/{terminal_id}">client.workspaces.terminals.<a href="./src/dedalus_sdk/resources/workspaces/terminals.py">delete</a>(terminal_id, \*, workspace_id) -> <a href="./src/dedalus_sdk/types/workspaces/terminal.py">Terminal</a></code>
