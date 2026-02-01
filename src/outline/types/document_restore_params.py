# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentRestoreParams"]


class DocumentRestoreParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""

    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """Identifier for the collection to restore the document to."""

    revision_id: Annotated[str, PropertyInfo(alias="revisionId")]
    """Identifier for the revision to restore to."""
