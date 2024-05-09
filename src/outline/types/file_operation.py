# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .collection import Collection

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


class FileOperation(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    collection: Optional[Collection] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this object was created"""

    size: Optional[float] = None
    """The size of the resulting file in bytes"""

    state: Optional[Literal["creating", "uploading", "complete", "error", "expired"]] = None
    """The state of the file operation."""

    type: Optional[Literal["import", "export"]] = None
    """The type of file operation."""

    user: Optional[User] = None
