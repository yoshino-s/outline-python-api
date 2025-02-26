# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    document_id: Required[Annotated[str, PropertyInfo(alias="documentId")]]

    id: str

    data: object
    """The body of the comment."""

    parent_comment_id: Annotated[str, PropertyInfo(alias="parentCommentId")]

    text: str
    """The body of the comment in markdown."""
