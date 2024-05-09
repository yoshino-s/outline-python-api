# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .auth import Auth
from .._models import BaseModel

__all__ = ["AuthInfoResponse"]


class AuthInfoResponse(BaseModel):
    data: Optional[Auth] = None
