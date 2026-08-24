# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionListParams", "Filter", "FilterUnionMember0", "FilterUnionMember1"]


class CollectionListParams(TypedDict, total=False):
    direction: Literal["ASC", "DESC"]

    filters: Iterable[Filter]
    """Structured filter expression, evaluated as an AND of top-level entries.

    Cannot be combined with the deprecated `query` or `statusFilter` parameters.
    """

    limit: float

    offset: float

    query: str
    """If set, will filter the results by collection name.

    Deprecated – prefer the `filters` parameter.
    """

    sort: str

    status_filter: Annotated[List[Literal["archived"]], PropertyInfo(alias="statusFilter")]
    """An optional array of statuses to filter by.

    Deprecated – prefer the `filters` parameter.
    """


class FilterUnionMember0(TypedDict, total=False):
    """A condition that compares a collection field against a value."""

    field: Required[Literal["name", "createdAt", "updatedAt", "archivedAt", "createdById", "permission"]]
    """Name of the collection field to filter on."""

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

    Note that some fields only accept a subset of operators – for example
    `permission` only supports `eq`, `neq`, `in`, `notIn`, `isNull` and `isNotNull`.
    """

    value: object
    """Value to compare against.

    May be a string, boolean or array of these depending on the field and operator.
    Date fields accept an ISO 8601 date or an ISO 8601 duration (relative to now).
    `permission` accepts a `Permission` enum value (or an array with `in`/`notIn`).
    Omit for `isNull` and `isNotNull`.
    """


class FilterUnionMember1(TypedDict, total=False):
    """A logical group that combines nested filters with an `AND` or `OR` operator.

    Groups may themselves contain further groups.
    """

    filters: Required[Iterable[object]]

    operator: Required[Literal["AND", "OR"]]


Filter: TypeAlias = Union[FilterUnionMember0, FilterUnionMember1]
