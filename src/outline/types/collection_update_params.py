# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionUpdateParams"]


class CollectionUpdateParams(TypedDict, total=False):
    id: Required[str]

    color: str

    description: str

    name: str

    permission: Literal["read", "read_write"]
