# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentSearchParams"]


class DocumentSearchParams(TypedDict, total=False):
    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """A collection to search within"""

    date_filter: Annotated[Literal["day", "week", "month", "year"], PropertyInfo(alias="dateFilter")]
    """
    Any documents that have not been updated within the specified period will be
    filtered out
    """

    document_id: Annotated[str, PropertyInfo(alias="documentId")]
    """A document to search within"""

    limit: float

    offset: float

    query: str

    status_filter: Annotated[Literal["draft", "archived", "published"], PropertyInfo(alias="statusFilter")]
    """Any documents that are not in the specified status will be filtered out"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    Any documents that have not been edited by the user identifier will be filtered
    out
    """
