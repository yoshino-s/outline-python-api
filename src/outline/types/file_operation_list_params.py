# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FileOperationListParams"]


class FileOperationListParams(TypedDict, total=False):
    type: Required[Literal["export", "import"]]
    """The type of fileOperation"""

    direction: Literal["ASC", "DESC"]

    limit: float

    offset: float

    sort: str
