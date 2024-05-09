# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    actor_id: Annotated[str, PropertyInfo(alias="actorId")]
    """Filter to events performed by the selected user"""

    audit_log: Annotated[bool, PropertyInfo(alias="auditLog")]
    """Whether to return detailed events suitable for an audit log.

    Without this flag less detailed event types will be returned.
    """

    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """Filter to events performed in the selected collection"""

    direction: Literal["ASC", "DESC"]

    document_id: Annotated[str, PropertyInfo(alias="documentId")]
    """Filter to events performed in the selected document"""

    limit: float

    name: str
    """Filter to a specific event, e.g.

    "collections.create". Event names are in the format "objects.verb"
    """

    offset: float

    sort: str
