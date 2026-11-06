# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MachineDeleteParams"]


class MachineDeleteParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    force: bool
    """Destroy from the last published filesystem checkpoint without publishing the Machine's remaining writes, whether the Machine is running or failed. Unpublished file writes are lost. The default publishes them first, and waits while it cannot."""
