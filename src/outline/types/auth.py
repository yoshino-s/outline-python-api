# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Auth", "Team", "User"]


class Team(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object."""

    allowed_domains: Optional[List[str]] = FieldInfo(alias="allowedDomains", default=None)

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)
    """
    The URL for the image associated with this workspace, it will be displayed in
    the workspace switcher and in the top left of the knowledge base along with the
    name.
    """

    default_collection_id: Optional[str] = FieldInfo(alias="defaultCollectionId", default=None)
    """
    If set then the referenced collection is where users will be redirected to after
    signing in instead of the Home screen
    """

    default_user_role: Optional[Literal["admin", "member", "viewer", "guest"]] = FieldInfo(
        alias="defaultUserRole", default=None
    )

    description: Optional[str] = None
    """A short description of this workspace."""

    document_embeds: Optional[bool] = FieldInfo(alias="documentEmbeds", default=None)
    """Whether this workspace has embeds in documents globally enabled.

    It can be disabled to reduce potential data leakage to third parties.
    """

    domain: Optional[str] = None
    """The custom domain configured for this workspace, if any."""

    guest_signin: Optional[bool] = FieldInfo(alias="guestSignin", default=None)
    """Whether this workspace has guest signin enabled.

    Guests can signin with an email address and are not required to have a Google
    Workspace/Slack SSO account once invited.
    """

    guidance_mcp: Optional[str] = FieldInfo(alias="guidanceMCP", default=None)
    """Guidance text provided to MCP integrations."""

    invite_required: Optional[bool] = FieldInfo(alias="inviteRequired", default=None)
    """
    Whether an invite is required to join this workspace, if false users may join
    with a linked SSO provider.
    """

    member_collection_create: Optional[bool] = FieldInfo(alias="memberCollectionCreate", default=None)
    """Whether members are allowed to create new collections.

    If false then only admins can create collections.
    """

    member_team_create: Optional[bool] = FieldInfo(alias="memberTeamCreate", default=None)
    """Whether members are allowed to create new groups.

    If false then only admins can create groups.
    """

    name: Optional[str] = None
    """
    The name of this workspace, it is usually auto-generated when the first SSO
    connection is made but can be changed if necessary.
    """

    passkeys_enabled: Optional[bool] = FieldInfo(alias="passkeysEnabled", default=None)
    """Whether passkey authentication is enabled for this workspace."""

    preferences: Optional[object] = None
    """Workspace-level preference flags."""

    sharing: Optional[bool] = None
    """Whether this workspace has share links globally enabled.

    If this value is false then all sharing UI and APIs are disabled.
    """

    subdomain: Optional[str] = None
    """
    Represents the subdomain at which this workspace's knowledge base can be
    accessed.
    """

    url: Optional[str] = None
    """
    The fully qualified URL at which this workspace's knowledge base can be
    accessed.
    """


class User(BaseModel):
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


class Auth(BaseModel):
    team: Optional[Team] = None

    user: Optional[User] = None
