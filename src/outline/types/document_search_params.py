# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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

    direction: Literal["ASC", "DESC"]
    """Specifies the sort order with respect to sort field"""

    document_id: Annotated[str, PropertyInfo(alias="documentId")]
    """A document to search within"""

    limit: float

    offset: float

    query: str

    share_id: Annotated[str, PropertyInfo(alias="shareId")]
    """Filter results to the collection or document referenced by the shareId"""

    snippet_max_words: Annotated[float, PropertyInfo(alias="snippetMaxWords")]
    """Maximum number of words to show in search result snippets"""

    snippet_min_words: Annotated[float, PropertyInfo(alias="snippetMinWords")]
    """Minimum number of words to show in search result snippets"""

    sort: Literal["relevance", "createdAt", "updatedAt", "title"]
    """Specifies the attributes by which search results will be sorted"""

    status_filter: Annotated[List[Literal["draft", "archived", "published"]], PropertyInfo(alias="statusFilter")]
    """Document statuses to include in results"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    Any documents that have not been edited by the user identifier will be filtered
    out
    """
