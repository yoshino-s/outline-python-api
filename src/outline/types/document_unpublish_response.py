# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .document import Document

__all__ = ["DocumentUnpublishResponse", "Policy"]


class Policy(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object this policy references."""

    abilities: Optional[Dict[str, Union[List[str], bool]]] = None
    """
    The abilities that are allowed by this policy, if an array is returned then the
    individual ID's in the array represent the memberships that grant the ability.
    """


class DocumentUnpublishResponse(BaseModel):
    data: Optional[Document] = None

    policies: Optional[List[Policy]] = None
