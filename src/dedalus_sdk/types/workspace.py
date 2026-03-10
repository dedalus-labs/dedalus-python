# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .lifecycle_status import LifecycleStatus

__all__ = ["Workspace"]


class Workspace(BaseModel):
    desired_state: Literal["active", "inactive", "destroyed"]

    status: LifecycleStatus

    workspace_id: str

    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """A URL to the JSON Schema for this object."""
