# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .document import Document
from .shared.pagination import Pagination

__all__ = ["DocumentDraftsResponse", "Policy", "PolicyAbilities"]


class PolicyAbilities(BaseModel):
    archive: Optional[bool] = None

    create: Optional[bool] = None

    create_child_document: Optional[bool] = FieldInfo(alias="createChildDocument", default=None)

    delete: Optional[bool] = None

    download: Optional[bool] = None

    move: Optional[bool] = None

    pin: Optional[bool] = None

    read: Optional[bool] = None

    restore: Optional[bool] = None

    share: Optional[bool] = None

    star: Optional[bool] = None

    unarchive: Optional[bool] = None

    unpin: Optional[bool] = None

    unstar: Optional[bool] = None

    update: Optional[bool] = None


class Policy(BaseModel):
    id: Optional[str] = None
    """Unique identifier for the object this policy references."""

    abilities: Optional[PolicyAbilities] = None


class DocumentDraftsResponse(BaseModel):
    data: Optional[List[Document]] = None

    pagination: Optional[Pagination] = None

    policies: Optional[List[Policy]] = None
