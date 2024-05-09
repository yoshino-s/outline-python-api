# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionAddUserParams"]


class CollectionAddUserParams(TypedDict, total=False):
    id: Required[str]

    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]

    permission: Literal["read", "read_write"]
