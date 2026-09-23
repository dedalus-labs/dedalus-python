# File generated from our OpenAPI spec by Scalar. See README.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHCreateParams"]


class SSHCreateParams(TypedDict, total=False):
    machine_id: Required[str]
    """Bare, lowercase, hyphenated Machine UUID. Pass the returned machine_id unchanged."""

    public_key: Required[str]
