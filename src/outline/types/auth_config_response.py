# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthConfigResponse", "Data", "DataService"]


class DataService(BaseModel):
    id: Optional[str] = None

    auth_url: Optional[str] = FieldInfo(alias="authUrl", default=None)

    name: Optional[str] = None


class Data(BaseModel):
    hostname: Optional[str] = None

    name: Optional[str] = None

    services: Optional[List[DataService]] = None


class AuthConfigResponse(BaseModel):
    data: Optional[Data] = None
