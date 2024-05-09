# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentUnpublishParams"]


class DocumentUnpublishParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""
