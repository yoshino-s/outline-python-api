# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentUpdateParams", "DataAttribute", "Preferences"]


class DocumentUpdateParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""

    collection_id: Annotated[Optional[str], PropertyInfo(alias="collectionId")]
    """Identifier for the collection to move the document to"""

    color: Optional[str]
    """Color for the document icon (hex format)"""

    data_attributes: Annotated[Optional[Iterable[DataAttribute]], PropertyInfo(alias="dataAttributes")]
    """Data attributes to be updated.

    Attributes not included will be removed from the document.
    """

    edit_mode: Annotated[Literal["append", "prepend", "replace", "patch"], PropertyInfo(alias="editMode")]
    """The editing mode for text updates to a document.

    When set to `patch`, the `findText` parameter is required and the existing
    occurrence of `findText` will be replaced with the value of `text`.
    """

    find_text: Annotated[str, PropertyInfo(alias="findText")]
    """The text to find within the document when using `patch` editMode.

    This text will be replaced with the value of `text`. Required when `editMode` is
    `patch`.
    """

    full_width: Annotated[bool, PropertyInfo(alias="fullWidth")]
    """Whether the document should be displayed in full width"""

    icon: Optional[str]
    """Icon displayed alongside the document title"""

    insights_enabled: Annotated[bool, PropertyInfo(alias="insightsEnabled")]
    """Whether insights should be visible on the document"""

    last_revision: Annotated[int, PropertyInfo(alias="lastRevision")]
    """
    If set, the update is rejected with a 409 response when the document's current
    revision number does not match this value. Use this for optimistic concurrency
    control to avoid overwriting changes made since the client last loaded the
    document.
    """

    preferences: Optional[Preferences]
    """Document-level display preferences.

    Only the fields supplied are updated; existing values for other preferences are
    preserved. Pass `null` to clear all preferences.
    """

    publish: bool
    """
    Whether this document should be published and made visible to other workspace
    members, if a draft
    """

    template_id: Annotated[Optional[str], PropertyInfo(alias="templateId")]
    """Identifier for the template this document is based on"""

    text: str
    """The body of the document in markdown."""

    title: str
    """The title of the document."""


class DataAttribute(TypedDict, total=False):
    data_attribute_id: Required[Annotated[str, PropertyInfo(alias="dataAttributeId")]]
    """Unique identifier for the data attribute."""

    value: Required[Union[str, bool, float]]
    """The value of the data attribute.

    Can be a string, boolean, or number depending on the data attribute type.
    """


class Preferences(TypedDict, total=False):
    """Document-level display preferences.

    Only the fields supplied are updated; existing values for other preferences are preserved. Pass `null` to clear all preferences.
    """

    heading_prefix: Annotated[
        Literal["none", "numeric", "alphanumeric", "outline"], PropertyInfo(alias="headingPrefix")
    ]
    """Numbering style applied to the document's headings when rendered."""
