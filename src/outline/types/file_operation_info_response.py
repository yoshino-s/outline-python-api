# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .file_operation import FileOperation

__all__ = ["FileOperationInfoResponse"]


class FileOperationInfoResponse(BaseModel):
    data: Optional[FileOperation] = None
