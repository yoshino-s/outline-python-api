# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Group"]


class Group(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    member_count: Optional[float] = FieldInfo(alias="memberCount", default=None)
    """The number of users that are members of the group"""

    name: Optional[str] = None
    """The name of this group."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""
