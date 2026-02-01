# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentTemplatizeParams"]


class DocumentTemplatizeParams(TypedDict, total=False):
    id: Required[str]

    publish: Required[bool]
    """Whether the new template should be published"""

    collection_id: Annotated[Optional[str], PropertyInfo(alias="collectionId")]
    """Identifier for the collection where the template should be created"""
