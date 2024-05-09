# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DocumentExportParams"]


class DocumentExportParams(TypedDict, total=False):
    id: str
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""
