# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["TerminalCreateParams"]


class TerminalCreateParams(TypedDict, total=False):
    height: Required[int]

    width: Required[int]

    cwd: str

    env: Dict[str, str]

    shell: str

    wake_if_needed: bool
