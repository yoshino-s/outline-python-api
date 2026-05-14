# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CommentCreateParams"]


class CommentCreateParams(TypedDict, total=False):
    document_id: Required[Annotated[str, PropertyInfo(alias="documentId")]]

    id: str

    anchor_prefix: Annotated[str, PropertyInfo(alias="anchorPrefix")]
    """
    Text immediately preceding `anchorText`, used to disambiguate between multiple
    occurrences. Requires `anchorText`.
    """

    anchor_suffix: Annotated[str, PropertyInfo(alias="anchorSuffix")]
    """
    Text immediately following `anchorText`, used to disambiguate between multiple
    occurrences. Requires `anchorText`.
    """

    anchor_text: Annotated[str, PropertyInfo(alias="anchorText")]
    """Plain text substring to anchor the comment to as an inline comment.

    The first occurrence in the document's plain text is used unless disambiguated
    by `anchorPrefix` and/or `anchorSuffix`.
    """

    data: object
    """The body of the comment."""

    parent_comment_id: Annotated[str, PropertyInfo(alias="parentCommentId")]

    text: str
    """The body of the comment in markdown."""
