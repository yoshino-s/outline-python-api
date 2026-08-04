# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.pagination import Pagination

__all__ = ["EventCreateResponse", "Data", "DataActor"]


class DataActor(BaseModel):
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


class Data(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    actor: Optional[DataActor] = None

    actor_id: Optional[str] = FieldInfo(alias="actorId", default=None)
    """The user that performed the action."""

    actor_ip_address: Optional[str] = FieldInfo(alias="actorIpAddress", default=None)
    """The ip address the action was performed from.

    This field is only returned when the `auditLog` boolean is true.
    """

    auth_type: Optional[Literal["api", "app", "mcp", "oauth"]] = FieldInfo(alias="authType", default=None)
    """The authentication method used to perform the action."""

    changes: Optional[object] = None
    """The set of changes made by this event.

    This field is only returned when the `auditLog` boolean is true.
    """

    collection_id: Optional[str] = FieldInfo(alias="collectionId", default=None)
    """Identifier for the associated collection, if any"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """The date and time that this event was created"""

    data: Optional[object] = None
    """Additional unstructured data associated with the event"""

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the associated document, if any"""

    api_model_id: Optional[str] = FieldInfo(alias="modelId", default=None)
    """
    Identifier for the object this event is associated with when it is not one of
    document, collection, or user.
    """

    name: Optional[str] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Identifier for the user associated with the event, if any."""


class EventCreateResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
