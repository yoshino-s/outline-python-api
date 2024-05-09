# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""

    append: bool
    """
    If true the text field will be appended to the end of the existing document,
    rather than the default behavior of replacing it. This is potentially useful for
    things like logging into a document.
    """

    done: bool
    """Whether the editing session has finished, this will trigger any notifications.

    This property will soon be deprecated.
    """

    publish: bool
    """
    Whether this document should be published and made visible to other team
    members, if a draft
    """

    text: str
    """The body of the document, may contain markdown formatting."""

    title: str
    """The title of the document."""
