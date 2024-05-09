# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .file_operation import FileOperation
from .shared.pagination import Pagination

__all__ = ["FileOperationListResponse"]


class FileOperationListResponse(BaseModel):
    data: Optional[List[FileOperation]] = None

    pagination: Optional[Pagination] = None
