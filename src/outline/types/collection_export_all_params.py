# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CollectionExportAllParams"]


class CollectionExportAllParams(TypedDict, total=False):
    format: Literal["outline-markdown", "json", "html"]
