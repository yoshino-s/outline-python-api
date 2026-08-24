# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentCreateParams", "DataAttribute", "Preferences"]


class DocumentCreateParams(TypedDict, total=False):
    id: str
    """Optional identifier for the document"""

    collection_id: Annotated[Optional[str], PropertyInfo(alias="collectionId")]
    """Identifier for the collection.

    Required to publish unless parentDocumentId is provided
    """

    color: Optional[str]
    """Color for the document icon (hex format)"""

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Optionally set the created date in the past"""

    data_attributes: Annotated[Iterable[DataAttribute], PropertyInfo(alias="dataAttributes")]
    """Data attributes to be included on the document."""

    full_width: Annotated[bool, PropertyInfo(alias="fullWidth")]
    """Whether the document should be displayed in full width"""

    icon: str
    """Icon displayed alongside the document title"""

    parent_document_id: Annotated[Optional[str], PropertyInfo(alias="parentDocumentId")]
    """Identifier for the parent document.

    Required to publish unless collectionId is provided
    """

    preferences: Optional[Preferences]
    """Document-level display preferences.

    Only the fields supplied are updated; existing values for other preferences are
    preserved. Pass `null` to clear all preferences.
    """

    publish: bool
    """
    Whether this document should be immediately published and made visible to other
    workspace members.
    """

    template_id: Annotated[str, PropertyInfo(alias="templateId")]

    text: str
    """The body of the document in markdown"""

    title: str


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
