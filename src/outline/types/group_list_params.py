# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GroupListParams"]


class GroupListParams(TypedDict, total=False):
    direction: Literal["ASC", "DESC"]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]
    """Filter to groups matching an external ID"""

    limit: float

    offset: float

    query: str
    """Filter to groups matching a search query"""

    sort: str

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Filter to groups including a specific user"""
