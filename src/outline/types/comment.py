# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Comment", "CreatedBy", "ResolvedBy"]


class CreatedBy(BaseModel):
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


class ResolvedBy(BaseModel):
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


class Comment(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    anchor_text: Optional[str] = FieldInfo(alias="anchorText", default=None)
    """
    The document text that the comment is anchored to, only included if
    includeAnchorText=true.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    created_by: Optional[CreatedBy] = FieldInfo(alias="createdBy", default=None)

    created_by_id: Optional[str] = FieldInfo(alias="createdById", default=None)
    """Identifier for the user who created this comment."""

    data: Optional[object] = None
    """The editor data representing this comment."""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the document this is related to."""

    parent_comment_id: Optional[str] = FieldInfo(alias="parentCommentId", default=None)
    """Identifier for the comment this is a child of, if any."""

    reactions: Optional[List[object]] = None
    """List of emoji reactions on this comment."""

    resolved_at: Optional[datetime] = FieldInfo(alias="resolvedAt", default=None)
    """The date and time that this comment was resolved, if it has been."""

    resolved_by: Optional[ResolvedBy] = FieldInfo(alias="resolvedBy", default=None)

    resolved_by_id: Optional[str] = FieldInfo(alias="resolvedById", default=None)
    """Identifier for the user who resolved this comment, if any."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""
