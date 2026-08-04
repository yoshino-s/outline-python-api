# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentImportParams"]


class DocumentImportParams(TypedDict, total=False):
    file: Required[object]
    """
    Plain text, markdown, docx, csv, tsv, html, mhtml (or mht) web pages, eml email
    messages, and textbundle/textpack bundles are supported.
    """

    collection_id: Annotated[Optional[str], PropertyInfo(alias="collectionId")]
    """Identifier for the collection to import into.

    One of collectionId or parentDocumentId is required.
    """

    parent_document_id: Annotated[Optional[str], PropertyInfo(alias="parentDocumentId")]
    """Identifier for the parent document to import under.

    One of collectionId or parentDocumentId is required.
    """

    publish: bool
    """Whether to publish the imported document"""
