# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PortCreateParams"]


class PortCreateParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    expires: int
    """Port lifetime in integer seconds. Omit for no expiry."""

    port: Required[int]

    protocol: Literal["http"]

    visibility: Literal["public", "key_required", "private"]
    """Who may reach the port. private, the default, requires a Dedalus API key from the owning organization in the X-Dedalus-API-Key header. key_required requires a port access key in the X-Dedalus-Port-Key header, and creating the port returns its first key once. public accepts anonymous requests, which can wake the machine and incur compute charges."""
