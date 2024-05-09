# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentDraftsParams"]


class DocumentDraftsParams(TypedDict, total=False):
    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """A collection to search within"""

    date_filter: Annotated[Literal["day", "week", "month", "year"], PropertyInfo(alias="dateFilter")]
    """
    Any documents that have not been updated within the specified period will be
    filtered out
    """

    direction: Literal["ASC", "DESC"]

    limit: float

    offset: float

    sort: str
