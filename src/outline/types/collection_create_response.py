# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .collection import Collection

__all__ = ["CollectionCreateResponse", "Policy"]


class Policy(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object this policy references."""

    abilities: Optional[Dict[str, Union[List[str], bool]]] = None
    """
    The abilities that are allowed by this policy, if an array is returned then the
    individual ID's in the array represent the memberships that grant the ability.
    """


class CollectionCreateResponse(BaseModel):
    data: Optional[Collection] = None

    policies: Optional[List[Policy]] = None
