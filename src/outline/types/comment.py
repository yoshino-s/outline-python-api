# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Comment", "CreatedBy", "UpdatedBy"]


class CreatedBy(BaseModel):
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


class UpdatedBy(BaseModel):
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


class Comment(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    created_by: Optional[CreatedBy] = FieldInfo(alias="createdBy", default=None)

    data: Optional[object] = None
    """The editor data representing this comment."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the document this is related to."""

    parent_comment_id: Optional[str] = FieldInfo(alias="parentCommentId", default=None)
    """Identifier for the comment this is a child of, if any."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""

    updated_by: Optional[UpdatedBy] = FieldInfo(alias="updatedBy", default=None)
