# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccessKeyRotateParams"]


class AccessKeyRotateParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    port_id: Required[str]

    access_key_id: Required[str]

    expires_in: Required[int]
    """Lifetime in integer seconds."""
