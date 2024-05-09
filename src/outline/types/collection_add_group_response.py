# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CollectionAddGroupResponse", "Data", "DataCollectionGroupMembership"]


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


class CollectionAddGroupResponse(BaseModel):
    data: Optional[Data] = None
