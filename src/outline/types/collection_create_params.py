# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    name: Required[str]

    color: str

    description: str

    permission: Literal["read", "read_write"]

    private: bool
