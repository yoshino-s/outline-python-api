# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .document import Document

__all__ = ["DocumentInfoResponse"]


class DocumentInfoResponse(BaseModel):
    data: Optional[Document] = None
