# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    collection_id: Required[Annotated[str, PropertyInfo(alias="collectionId")]]

    title: Required[str]

    parent_document_id: Annotated[str, PropertyInfo(alias="parentDocumentId")]

    publish: bool
    """
    Whether this document should be immediately published and made visible to other
    team members.
    """

    template: bool
    """Whether this document should be considered to be a template."""

    template_id: Annotated[str, PropertyInfo(alias="templateId")]

    text: str
    """The body of the document, may contain markdown formatting."""
