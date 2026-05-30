# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileOperation", "User"]


class User(BaseModel):
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


class FileOperation(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """
    Identifier for the associated collection, if the file operation is scoped to a
    single collection.
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """
    Identifier for the associated document, if the file operation is scoped to a
    single document.
    """

    error: Optional[str] = None
    """An error message if the file operation failed."""

    format: Optional[str] = None
    """The file format of the resulting file."""

    name: Optional[str] = None
    """
    The name of the file operation, derived from the collection name, document
    title, or file name.
    """

    size: Optional[str] = None
    """The size of the resulting file in bytes.

    Returned as a string as the value may exceed the safe integer range.
    """

    state: Optional[Literal["creating", "uploading", "complete", "error", "expired"]] = None
    """The state of the file operation."""

    type: Optional[Literal["import", "export"]] = None
    """The type of file operation."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """The date and time that this object was last changed"""

    user: Optional[User] = None
