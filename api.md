# Workspaces

Types:

```python
from dedalus_sdk.types import CreateParams, LifecycleStatus, UpdateParams, Workspace, WorkspaceList
```

Methods:

- <code title="post /v1/workspaces">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces.py">create</a>(\*\*<a href="src/dedalus_sdk/types/workspace_create_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
- <code title="get /v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces.py">retrieve</a>(workspace_id) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
- <code title="patch /v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces.py">update</a>(workspace_id, \*\*<a href="src/dedalus_sdk/types/workspace_update_params.py">params</a>) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
- <code title="get /v1/workspaces">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces.py">list</a>(\*\*<a href="src/dedalus_sdk/types/workspace_list_params.py">params</a>) -> SyncWorkspaceList[Item]</code>
- <code title="delete /v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/dedalus_sdk/resources/workspaces.py">delete</a>(workspace_id) -> <a href="./src/dedalus_sdk/types/workspace.py">Workspace</a></code>
