# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import event_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.event_create_response import EventCreateResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        actor_id: str | NotGiven = NOT_GIVEN,
        audit_log: bool | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        document_id: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventCreateResponse:
        """
        Events are an audit trail of important events that happen in the knowledge base.

        Args:
          actor_id: Filter to events performed by the selected user

          audit_log: Whether to return detailed events suitable for an audit log. Without this flag
              less detailed event types will be returned.

          collection_id: Filter to events performed in the selected collection

          document_id: Filter to events performed in the selected document

          name: Filter to a specific event, e.g. "collections.create". Event names are in the
              format "objects.verb"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/events.list",
            body=maybe_transform(
                {
                    "actor_id": actor_id,
                    "audit_log": audit_log,
                    "collection_id": collection_id,
                    "direction": direction,
                    "document_id": document_id,
                    "limit": limit,
                    "name": name,
                    "offset": offset,
                    "sort": sort,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventCreateResponse,
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        actor_id: str | NotGiven = NOT_GIVEN,
        audit_log: bool | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        document_id: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventCreateResponse:
        """
        Events are an audit trail of important events that happen in the knowledge base.

        Args:
          actor_id: Filter to events performed by the selected user

          audit_log: Whether to return detailed events suitable for an audit log. Without this flag
              less detailed event types will be returned.

          collection_id: Filter to events performed in the selected collection

          document_id: Filter to events performed in the selected document

          name: Filter to a specific event, e.g. "collections.create". Event names are in the
              format "objects.verb"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/events.list",
            body=await async_maybe_transform(
                {
                    "actor_id": actor_id,
                    "audit_log": audit_log,
                    "collection_id": collection_id,
                    "direction": direction,
                    "document_id": document_id,
                    "limit": limit,
                    "name": name,
                    "offset": offset,
                    "sort": sort,
                },
                event_create_params.EventCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventCreateResponse,
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_raw_response_wrapper(
            events.create,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_raw_response_wrapper(
            events.create,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.create = to_streamed_response_wrapper(
            events.create,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.create = async_to_streamed_response_wrapper(
            events.create,
        )
