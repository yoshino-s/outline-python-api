# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .collection import Collection
from .shared.pagination import Pagination

__all__ = ["CollectionListResponse"]


class CollectionListResponse(BaseModel):
    data: Optional[List[Collection]] = None

    pagination: Optional[Pagination] = None
