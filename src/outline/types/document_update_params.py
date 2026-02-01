# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentUpdateParams", "DataAttribute"]


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

    edit_mode: Annotated[Literal["append", "prepend", "replace"], PropertyInfo(alias="editMode")]
    """The editing mode for text updates to a document."""

    full_width: Annotated[bool, PropertyInfo(alias="fullWidth")]
    """Whether the document should be displayed in full width"""

    icon: Optional[str]
    """Icon displayed alongside the document title"""

    insights_enabled: Annotated[bool, PropertyInfo(alias="insightsEnabled")]
    """Whether insights should be visible on the document"""

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
