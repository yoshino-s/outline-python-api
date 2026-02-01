# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentUpdateParams", "DataAttribute"]


class DocumentUpdateParams(TypedDict, total=False):
    id: Required[str]
    """Unique identifier for the document. Either the UUID or the urlId is acceptable."""

    data_attributes: Annotated[Optional[Iterable[DataAttribute]], PropertyInfo(alias="dataAttributes")]
    """Data attributes to be updated.

    Attributes not included will be removed from the document.
    """

    edit_mode: Annotated[object, PropertyInfo(alias="editMode")]
    """
    The editing mode of the request - append will add content to the end of the
    document, prepend will add content to the start of the document, and replace
    will overwrite the existing content.
    """

    publish: bool
    """
    Whether this document should be published and made visible to other team
    members, if a draft
    """

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
