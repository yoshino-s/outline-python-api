# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionRemoveUserParams"]


class CollectionRemoveUserParams(TypedDict, total=False):
    id: Required[str]
    """Identifier for the collection"""

    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]
