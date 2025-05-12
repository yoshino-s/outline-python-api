# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    name: Required[str]

    color: str
    """A hex color code for the collection icon"""

    description: str
    """A brief description of the collection, markdown supported."""

    icon: str
    """A string that represents an icon in the outline-icons package or an emoji"""

    permission: Literal["read", "read_write"]

    sharing: bool
    """Whether public sharing of documents is allowed"""
