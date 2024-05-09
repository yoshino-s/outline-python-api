# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_operation import FileOperation

__all__ = ["CollectionExportResponse", "Data"]


class Data(BaseModel):
    file_operation: Optional[FileOperation] = FieldInfo(alias="fileOperation", default=None)


class CollectionExportResponse(BaseModel):
    data: Optional[Data] = None
