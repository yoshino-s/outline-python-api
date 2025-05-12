# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Collection", "ArchivedBy", "Sort"]


class ArchivedBy(BaseModel):
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


class Sort(BaseModel):
    direction: Optional[Literal["asc", "desc"]] = None

    field: Optional[str] = None


class Collection(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """The date and time that this object was archived"""

    archived_by: Optional[ArchivedBy] = FieldInfo(alias="archivedBy", default=None)

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
    """A string that represents an icon in the outline-icons package or an emoji"""

    index: Optional[str] = None
    """The position of the collection in the sidebar"""

    name: Optional[str] = None
    """The name of the collection."""

    permission: Optional[Literal["read", "read_write"]] = None

    sharing: Optional[bool] = None
    """Whether public document sharing is enabled in this collection"""

    sort: Optional[Sort] = None
    """The sort of documents in the collection.

    Note that not all API responses respect this and it is left as a frontend
    concern to implement.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""

    url_id: Optional[str] = FieldInfo(alias="urlId", default=None)
    """
    A short unique identifier that can be used to identify the collection instead of
    the UUID.
    """
