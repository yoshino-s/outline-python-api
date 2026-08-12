# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CollectionAddUserResponse", "Data", "DataMembership", "DataUser"]


class DataMembership(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Identifier for the associated collection, if any."""

    created_by_id: Optional[str] = FieldInfo(alias="createdById", default=None)
    """Identifier for the user who created this membership."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the associated document, if any."""

    index: Optional[str] = None
    """The position of the collection in the user's sidebar."""

    permission: Optional[Literal["read", "read_write"]] = None

    source_id: Optional[str] = FieldInfo(alias="sourceId", default=None)
    """Identifier for the membership this one was inherited from, if any."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Identifier for the associated user."""


class DataUser(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)
    """
    The URL for the image associated with this user, it will be displayed in the
    application UI and email notifications.
    """

    color: Optional[str] = None
    """A color representing the user, used in the UI for avatars without an image."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this user first signed in or was invited as a guest."""

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The date and time that this user was deleted, if applicable."""

    email: Optional[str] = None
    """
    The email associated with this user, it is migrated from Slack or Google
    Workspace when the SSO connection is made but can be changed if necessary.
    """

    invited_by: Optional[object] = FieldInfo(alias="invitedBy", default=None)
    """The user that invited this user, if they were invited.

    Only included in responses to admin users.
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
    SSO connection is made but can be changed if necessary.
    """

    role: Optional[Literal["admin", "member", "viewer", "guest"]] = None

    timezone: Optional[str] = None
    """The timezone this user has registered."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this user was last updated."""


class Data(BaseModel):
    memberships: Optional[List[DataMembership]] = None

    users: Optional[List[DataUser]] = None


class CollectionAddUserResponse(BaseModel):
    data: Optional[Data] = None
