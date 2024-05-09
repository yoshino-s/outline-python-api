# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GroupMembershipListParams"]


class GroupMembershipListParams(TypedDict, total=False):
    id: Required[str]
    """Identifier for the collection"""

    limit: float

    offset: float

    permission: Literal["read", "read_write"]

    query: str
    """Filter memberships by group names"""
