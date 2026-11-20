# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PortUpdateParams"]


class PortUpdateParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    port_id: Required[str]

    visibility: Required[Literal["public", "key_required", "private"]]
    """Who may reach the port. private requires a Dedalus API key from the owning organization in the X-Dedalus-API-Key header. key_required requires a port access key in the X-Dedalus-Port-Key header. public accepts anonymous requests, which can wake the machine and incur compute charges."""
