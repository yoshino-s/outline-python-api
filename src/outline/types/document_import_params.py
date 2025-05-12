# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentImportParams"]


class DocumentImportParams(TypedDict, total=False):
    file: Required[object]
    """Plain text, markdown, docx, csv, tsv, and html format are supported."""

    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]

    parent_document_id: Annotated[str, PropertyInfo(alias="parentDocumentId")]

    publish: bool

    template: bool
