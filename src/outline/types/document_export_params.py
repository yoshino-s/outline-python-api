# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentExportParams"]


class DocumentExportParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""

    include_child_documents: Annotated[bool, PropertyInfo(alias="includeChildDocuments")]
    """Whether to include child documents in the export.

    Using this option will always return a zip file.
    """

    paper_size: Annotated[str, PropertyInfo(alias="paperSize")]
    """Paper size for PDF export (e.g., "A4", "Letter")"""

    signed_urls: Annotated[float, PropertyInfo(alias="signedUrls")]
    """How long signed URLs should remain valid for attachment links (in seconds)"""
