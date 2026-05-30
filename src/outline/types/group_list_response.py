# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .group import Group
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["GroupListResponse", "Data", "DataGroupMembership", "Policy"]


class DataGroupMembership(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Identifier for the associated collection, if any."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the associated document, if any."""

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)
    """Identifier for the associated group."""

    permission: Optional[Literal["read", "read_write"]] = None

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)
    """Identifier for the membership this one was inherited from, if any."""


class Data(BaseModel):
    group_memberships: Optional[List[DataGroupMembership]] = FieldInfo(alias="groupMemberships", default=None)
    """
    A preview of memberships in the group, note that this is not all memberships
    which can be queried from `groups.memberships`.
    """

    groups: Optional[List[Group]] = None


class Policy(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object this policy references."""

    abilities: Optional[Dict[str, Union[List[str], bool]]] = None
    """
    The abilities that are allowed by this policy, if an array is returned then the
    individual ID's in the array represent the memberships that grant the ability.
    """


class GroupListResponse(BaseModel):
    data: Optional[Data] = None

    pagination: Optional[Pagination] = None

    policies: Optional[List[Policy]] = None
