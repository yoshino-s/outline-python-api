# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .collection import Collection

__all__ = ["CollectionRetrieveResponse"]


class CollectionRetrieveResponse(BaseModel):
    data: Optional[Collection] = None
