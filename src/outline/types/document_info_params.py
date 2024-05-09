# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentInfoParams"]


class DocumentInfoParams(TypedDict, total=False):
    id: str
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""

    share_id: Annotated[str, PropertyInfo(alias="shareId")]
    """
    Unique identifier for a document share, a shareId may be used in place of a
    document UUID
    """
