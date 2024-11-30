# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CollectionDocumentsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the document."""

    children: Optional[List[object]] = None

    title: Optional[str] = None

    url: Optional[str] = None


class CollectionDocumentsResponse(BaseModel):
    data: Optional[List[Data]] = None
