# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..group import Group
from ..._models import BaseModel
from ..shared.pagination import Pagination

__all__ = ["GroupMembershipListResponse", "Data", "DataCollectionGroupMembership"]


class DataCollectionGroupMembership(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Identifier for the associated collection."""

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)
    """Identifier for the associated group."""

    permission: Optional[Literal["read", "read_write"]] = None


class Data(BaseModel):
    collection_group_memberships: Optional[List[DataCollectionGroupMembership]] = FieldInfo(
        alias="collectionGroupMemberships", default=None
    )

    groups: Optional[List[Group]] = None


class GroupMembershipListResponse(BaseModel):
    data: Optional[Data] = None

    pagination: Optional[Pagination] = None
