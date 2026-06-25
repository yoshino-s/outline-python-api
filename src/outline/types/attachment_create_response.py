# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AttachmentCreateResponse", "Data", "DataAttachment"]


class DataAttachment(BaseModel):
    content_type: Optional[str] = FieldInfo(alias="contentType", default=None)

    document_id: Optional[str] = FieldInfo(alias="documentId", default=None)
    """Identifier for the associated document, if any."""

    name: Optional[str] = None

    size: Optional[str] = None
    """The size of the attachment in bytes.

    Returned as a string as the value may exceed the safe integer range.
    """

    url: Optional[str] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Identifier for the user that created the attachment."""


class Data(BaseModel):
    attachment: Optional[DataAttachment] = None

    form: Optional[object] = None
    """Present when `mode` is `post`.

    The form fields to include in the multipart upload, including signed
    credentials.
    """

    headers: Optional[object] = None
    """Present when `mode` is `put`.

    The HTTP headers that must be sent with the PUT request.
    """

    max_upload_size: Optional[float] = FieldInfo(alias="maxUploadSize", default=None)

    mode: Optional[Literal["post", "put"]] = None
    """Indicates which presigned upload method the server is configured to use.

    When `post`, the client should perform a multipart form POST using `uploadUrl`
    and `form`. When `put`, the client should perform a PUT request to `url` with
    the supplied `headers`.
    """

    upload_url: Optional[str] = FieldInfo(alias="uploadUrl", default=None)
    """Present when `mode` is `post`. The endpoint to POST a multipart form upload to."""

    url: Optional[str] = None
    """Present when `mode` is `put`. The presigned URL to PUT the file contents to."""


class AttachmentCreateResponse(BaseModel):
    data: Optional[Data] = None
