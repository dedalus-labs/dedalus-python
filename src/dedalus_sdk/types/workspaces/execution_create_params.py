# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ExecutionCreateParams"]


class ExecutionCreateParams(TypedDict, total=False):
    command: Required[Optional[SequenceNotStr[str]]]

    capture_paths: Optional[SequenceNotStr[str]]

    cwd: str

    env: Dict[str, str]

    stdin: str

    timeout_ms: int

    wake_if_needed: bool
