# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionListParams"]


class CollectionListParams(TypedDict, total=False):
    direction: Literal["ASC", "DESC"]

    limit: float

    offset: float

    query: str
    """If set, will filter the results by collection name."""

    sort: str

    status_filter: Annotated[List[Literal["archived"]], PropertyInfo(alias="statusFilter")]
    """An optional array of statuses to filter by."""
