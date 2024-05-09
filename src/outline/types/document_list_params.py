# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentListParams"]


class DocumentListParams(TypedDict, total=False):
    backlink_document_id: Annotated[str, PropertyInfo(alias="backlinkDocumentId")]

    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """Optionally filter to a specific collection"""

    direction: Literal["ASC", "DESC"]

    limit: float

    offset: float

    parent_document_id: Annotated[str, PropertyInfo(alias="parentDocumentId")]

    sort: str

    template: bool
    """Optionally filter to only templates"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
