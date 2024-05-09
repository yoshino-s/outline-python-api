# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AttachmentCreateResponse", "Data", "DataAttachment"]


class DataAttachment(BaseModel):
    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the associated document, if any."""

    name: Optional[str] = None

    size: Optional[float] = None

    url: Optional[str] = None


class Data(BaseModel):
    attachment: Optional[DataAttachment] = None

    form: Optional[object] = None

    max_upload_size: Optional[float] = FieldInfo(alias="maxUploadSize", default=None)

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)


class AttachmentCreateResponse(BaseModel):
    data: Optional[Data] = None
