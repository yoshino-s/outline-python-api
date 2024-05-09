# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Collection", "Sort"]


class Sort(BaseModel):
    direction: Optional[Literal["asc", "desc"]] = None

    field: Optional[str] = None


class Collection(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    color: Optional[str] = None
    """
    A color representing the collection, this is used to help make collections more
    identifiable in the UI. It should be in HEX format including the #
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The date and time that this object was deleted"""

    description: Optional[str] = None
    """A description of the collection, may contain markdown formatting"""

    icon: Optional[str] = None
    """A string that represents an icon in the outline-icons package"""

    index: Optional[str] = None
    """The position of the collection in the sidebar"""

    name: Optional[str] = None
    """The name of the collection."""

    permission: Optional[Literal["read", "read_write"]] = None

    sort: Optional[Sort] = None
    """The sort of documents in the collection.

    Note that not all API responses respect this and it is left as a frontend
    concern to implement.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""
