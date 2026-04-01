# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .machine_list_item import MachineListItem

__all__ = ["MachineList"]


class MachineList(BaseModel):
    items: Optional[List[MachineListItem]] = None

    next_cursor: Optional[str] = None
