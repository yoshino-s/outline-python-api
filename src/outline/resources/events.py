# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import event_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.event_create_response import EventCreateResponse

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    """`Events` represent an artifact of an action.

    Whether it is creating a user,
    editing a document, changing permissions, or any other action – an event
    is created that can be used as an audit trail or activity stream.
    """

    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        actor_id: str | Omit = omit,
        audit_log: bool | Omit = omit,
        collection_id: str | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        document_id: str | Omit = omit,
        limit: float | Omit = omit,
        name: str | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    """`Events` represent an artifact of an action.

    Whether it is creating a user,
    editing a document, changing permissions, or any other action – an event
    is created that can be used as an audit trail or activity stream.
    """

    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        actor_id: str | Omit = omit,
        audit_log: bool | Omit = omit,
        collection_id: str | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        document_id: str | Omit = omit,
        limit: float | Omit = omit,
        name: str | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
