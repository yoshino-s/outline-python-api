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


class EventCreateResponse(BaseModel):
    data: Optional[List[Data]] = None

    pagination: Optional[Pagination] = None
