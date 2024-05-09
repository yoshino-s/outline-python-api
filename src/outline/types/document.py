# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Document", "Collaborator", "CreatedBy", "UpdatedBy"]


class Collaborator(BaseModel):
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


class Document(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """The date and time that this object was archived"""

    collaborators: Optional[List[Collaborator]] = None

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Identifier for the associated collection."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    created_by: Optional[CreatedBy] = FieldInfo(alias="createdBy", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The date and time that this object was deleted"""

    emoji: Optional[str] = None
    """An emoji associated with the document."""

    full_width: Optional[bool] = FieldInfo(alias="fullWidth", default=None)
    """Whether this document should be displayed in a full-width view."""

    parent_document_id: Optional[str] = FieldInfo(alias="parentDocumentId", default=None)
    """Identifier for the document this is a child of, if any."""

    pinned: Optional[bool] = None
    """Whether this document is pinned in the collection"""

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)
    """The date and time that this object was published"""

    revision: Optional[float] = None
    """
    A number that is auto incrementing with every revision of the document that is
    saved
    """

    template: Optional[bool] = None
    """Whether this document is a template"""

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """Unique identifier for the template this document was created from, if any"""

    text: Optional[str] = None
    """The text content of the document, contains markdown formatting"""

    title: Optional[str] = None
    """The title of the document."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""

    updated_by: Optional[UpdatedBy] = FieldInfo(alias="updatedBy", default=None)

    url_id: Optional[str] = FieldInfo(alias="urlId", default=None)
    """
    A short unique ID that can be used to identify the document as an alternative to
    the UUID
    """
