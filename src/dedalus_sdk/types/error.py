# File generated from our OpenAPI spec by Scalar. See README.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Error"]


class Error(BaseModel):
    details: Optional[Dict[str, str]] = None

    error_code: str

    message: str

    retry_after_ms: Optional[int] = None

    retryable: bool
