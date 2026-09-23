# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MachineRebootParams"]


class MachineRebootParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    force: bool
    """Recover from the last committed filesystem checkpoint without guest cooperation. Unpublished file writes are lost. The default checkpoints files before rebooting."""
