# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentImportParams"]


class DocumentImportParams(TypedDict, total=False):
    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]

    file: object
    """Only plain text, markdown, docx, and html format are supported."""

    parent_document_id: Annotated[str, PropertyInfo(alias="parentDocumentId")]

    publish: bool

    template: bool
