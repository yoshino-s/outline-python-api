# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttachmentCreateParams"]


class AttachmentCreateParams(TypedDict, total=False):
    content_type: Required[Annotated[str, PropertyInfo(alias="contentType")]]

    name: Required[str]

    size: Required[float]
    """Size of the file attachment in bytes."""

    document_id: Annotated[str, PropertyInfo(alias="documentId")]
    """Identifier for the associated document, if any."""
