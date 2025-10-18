# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionExportAllParams"]


class CollectionExportAllParams(TypedDict, total=False):
    format: Literal["outline-markdown", "json", "html"]

    include_attachments: Annotated[bool, PropertyInfo(alias="includeAttachments")]
    """Whether to include attachments in the export."""

    include_private: Annotated[bool, PropertyInfo(alias="includePrivate")]
    """Whether to include private collections in the export."""
