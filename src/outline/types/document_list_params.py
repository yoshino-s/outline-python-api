# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentListParams", "Filter", "FilterUnionMember0", "FilterUnionMember1"]


class DocumentListParams(TypedDict, total=False):
    backlink_document_id: Annotated[str, PropertyInfo(alias="backlinkDocumentId")]

    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """Optionally filter to a specific collection.

    Deprecated – prefer the `filters` parameter.
    """

    direction: Literal["ASC", "DESC"]

    filters: Iterable[Filter]
    """Structured filter expression, evaluated as an AND of top-level entries.

    Cannot be combined with the deprecated `collectionId`, `userId`,
    `parentDocumentId` or `statusFilter` parameters.
    """

    limit: float

    offset: float

    parent_document_id: Annotated[str, PropertyInfo(alias="parentDocumentId")]
    """Optionally filter to child documents of a specific parent.

    Deprecated – prefer the `filters` parameter.
    """

    sort: str

    status_filter: Annotated[List[Literal["draft", "archived", "published"]], PropertyInfo(alias="statusFilter")]
    """Document statuses to include in results.

    Deprecated – prefer the `filters` parameter.
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """Optionally filter to documents created by a specific user.

    Deprecated – prefer the `filters` parameter.
    """


class FilterUnionMember0(TypedDict, total=False):
    """A condition that compares a document field against a value."""

    field: Required[
        Literal[
            "createdAt",
            "updatedAt",
            "publishedAt",
            "archivedAt",
            "title",
            "templateId",
            "collectionId",
            "userId",
            "documentId",
            "parentDocumentId",
        ]
    ]
    """Name of the document field to filter on."""

    operator: Required[
        Literal[
            "eq",
            "neq",
            "lt",
            "lte",
            "gt",
            "gte",
            "contains",
            "startsWith",
            "endsWith",
            "containsStrict",
            "startsWithStrict",
            "endsWithStrict",
            "in",
            "notIn",
            "isNull",
            "isNotNull",
        ]
    ]
    """Comparison operator to apply.

    Note that some fields only accept a subset of operators – for example `userId`
    and `documentId` only support `eq` and `in`.
    """

    value: object
    """Value to compare against.

    May be a string, number, boolean or array of these depending on the field and
    operator. Date fields accept an ISO 8601 date or an ISO 8601 duration (relative
    to now). Omit for `isNull` and `isNotNull`.
    """


class FilterUnionMember1(TypedDict, total=False):
    """A logical group that combines nested filters with an `AND` or `OR` operator.

    Groups may themselves contain further groups.
    """

    filters: Required[Iterable[object]]

    operator: Required[Literal["AND", "OR"]]


Filter: TypeAlias = Union[FilterUnionMember0, FilterUnionMember1]
