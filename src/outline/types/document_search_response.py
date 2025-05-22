# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .document import Document
from .shared.pagination import Pagination

__all__ = ["DocumentSearchResponse", "Data", "Policy"]


class Data(BaseModel):
    context: Optional[str] = None
    """A short snippet of context from the document that includes the search query."""

    document: Optional[Document] = None

    ranking: Optional[float] = None
    """The ranking used to order search results based on relevance."""


class Policy(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object this policy references."""

    abilities: Optional[Dict[str, Union[List[str], bool]]] = None
    """
    The abilities that are allowed by this policy, if an array is returned then the
    individual ID's in the array represent the memberships that grant the ability.
    """


class DocumentSearchResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None

    policies: Optional[List[Policy]] = None
