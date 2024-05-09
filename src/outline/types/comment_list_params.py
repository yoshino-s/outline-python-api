# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CommentListParams"]


class CommentListParams(TypedDict, total=False):
    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """Filter to a specific collection"""

    direction: Literal["ASC", "DESC"]

    document_id: Annotated[str, PropertyInfo(alias="documentId")]
    """Filter to a specific document"""

    limit: float

    offset: float

    sort: str
