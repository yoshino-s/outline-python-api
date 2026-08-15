# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentSearchParams", "Filter", "FilterUnionMember0", "FilterUnionMember1"]


class DocumentSearchParams(TypedDict, total=False):
    collection_id: Annotated[str, PropertyInfo(alias="collectionId")]
    """A collection to search within. Deprecated – prefer the `filters` parameter."""

    date_filter: Annotated[Literal["day", "week", "month", "year"], PropertyInfo(alias="dateFilter")]
    """
    Any documents that have not been updated within the specified period will be
    filtered out. Deprecated – prefer the `filters` parameter with a date field and
    an ISO 8601 duration value.
    """

    direction: Literal["ASC", "DESC"]
    """Specifies the sort order with respect to sort field"""

    document_id: Annotated[str, PropertyInfo(alias="documentId")]
    """A document to search within. Deprecated – prefer the `filters` parameter."""

    filters: Iterable[Filter]
    """Structured filter expression, evaluated as an AND of top-level entries.

    Cannot be combined with the deprecated `collectionId`, `userId`, `documentId`,
    `dateFilter` or `statusFilter` parameters.
    """

    limit: float

    offset: float

    query: str

    share_id: Annotated[str, PropertyInfo(alias="shareId")]
    """Filter results to the collection or document referenced by the shareId"""

    snippet_max_words: Annotated[float, PropertyInfo(alias="snippetMaxWords")]
    """Maximum number of words to show in search result snippets"""

    snippet_min_words: Annotated[float, PropertyInfo(alias="snippetMinWords")]
    """Minimum number of words to show in search result snippets"""

    sort: Literal["relevance", "createdAt", "updatedAt", "title"]
    """Specifies the attributes by which search results will be sorted"""

    status_filter: Annotated[List[Literal["draft", "archived", "published"]], PropertyInfo(alias="statusFilter")]
    """Document statuses to include in results.

    Deprecated – prefer the `filters` parameter.
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    Any documents that have not been edited by the user identifier will be filtered
    out. Deprecated – prefer the `filters` parameter.
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
