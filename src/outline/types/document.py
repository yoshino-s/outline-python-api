# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Document", "CreatedBy", "DataAttribute", "Tasks", "UpdatedBy"]


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


class DataAttribute(BaseModel):
    data_attribute_id: Optional[str] = FieldInfo(alias="dataAttributeId", default=None)
    """Unique identifier for the associated data attribute."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object attribute was last changed"""

    value: Union[str, bool, float, None] = None
    """The value of the data attribute for this document."""


class Tasks(BaseModel):
    """Task completion counts for the document."""

    completed: Optional[float] = None

    total: Optional[float] = None


class UpdatedBy(BaseModel):
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


class Document(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    archived_at: Optional[datetime] = FieldInfo(alias="archivedAt", default=None)
    """The date and time that this object was archived"""

    collaborator_ids: Optional[List[str]] = FieldInfo(alias="collaboratorIds", default=None)
    """Identifiers of users who have edited the document."""

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Identifier for the associated collection."""

    color: Optional[str] = None
    """The color of the document icon in hex format."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    created_by: Optional[CreatedBy] = FieldInfo(alias="createdBy", default=None)

    data: Optional[object] = None
    """
    The body of the document as a Prosemirror document, returned in place of text
    when requested.
    """

    data_attributes: Optional[List[DataAttribute]] = FieldInfo(alias="dataAttributes", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)
    """The date and time that this object was deleted"""

    full_width: Optional[bool] = FieldInfo(alias="fullWidth", default=None)
    """Whether this document should be displayed in a full-width view."""

    icon: Optional[str] = None
    """An emoji or icon associated with the document."""

    parent_document_id: Optional[str] = FieldInfo(alias="parentDocumentId", default=None)
    """Identifier for the document this is a child of, if any."""

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)
    """The date and time that this object was published"""

    revision: Optional[float] = None
    """
    A number that is auto incrementing with every revision of the document that is
    saved
    """

    tasks: Optional[Tasks] = None
    """Task completion counts for the document."""

    template_id: Optional[str] = FieldInfo(alias="templateId", default=None)
    """Unique identifier for the template this document was created from, if any"""

    text: Optional[str] = None
    """The text content of the document, contains markdown formatting"""

    title: Optional[str] = None
    """The title of the document."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""

    updated_by: Optional[UpdatedBy] = FieldInfo(alias="updatedBy", default=None)

    url: Optional[str] = None
    """A URL path to access the document."""

    url_id: Optional[str] = FieldInfo(alias="urlId", default=None)
    """
    A short unique ID that can be used to identify the document as an alternative to
    the UUID
    """
