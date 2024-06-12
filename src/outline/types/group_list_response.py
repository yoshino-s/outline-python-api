# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .group import Group
from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["GroupListResponse", "Data", "DataGroupMembership", "DataGroupMembershipUser"]


class DataGroupMembershipUser(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)
    """
    The URL for the image associated with this user, it will be displayed in the
    application UI and email notifications.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this user first signed in or was invited as a guest."""

    email: Optional[str] = None
    """
    The email associated with this user, it is migrated from Slack or Google
    Workspace when the SSO connection is made but can be changed if neccessary.
    """

    is_suspended: Optional[bool] = FieldInfo(alias="isSuspended", default=None)
    """Whether this user has been suspended."""

    last_active_at: Optional[datetime] = FieldInfo(alias="lastActiveAt", default=None)
    """
    The last time this user made an API request, this value is updated at most every
    5 minutes.
    """

    name: Optional[str] = None
    """
    The name of this user, it is migrated from Slack or Google Workspace when the
    SSO connection is made but can be changed if neccessary.
    """

    role: Optional[Literal["admin", "member", "viewer", "guest"]] = None


class DataGroupMembership(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)
    """Identifier for the associated group."""

    user: Optional[DataGroupMembershipUser] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Identifier for the associated user."""


class Data(BaseModel):
    group_memberships: Optional[List[DataGroupMembership]] = FieldInfo(alias="groupMemberships", default=None)
    """
    A preview of memberships in the group, note that this is not all memberships
    which can be queried from `groups.memberships`.
    """

    groups: Optional[List[Group]] = None


class GroupListResponse(BaseModel):
    data: Optional[Data] = None

    pagination: Optional[Pagination] = None
