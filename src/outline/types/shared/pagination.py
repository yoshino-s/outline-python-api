# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    limit: Optional[float] = None

    offset: Optional[float] = None
