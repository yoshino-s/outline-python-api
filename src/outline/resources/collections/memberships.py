# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.collections import membership_list_params
from ...types.collections.membership_list_response import MembershipListResponse

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: str,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipListResponse:
        """This method allows you to list a collections individual memberships.

        It's
        important to note that memberships returned from this endpoint do not include
        group memberships.

        Args:
          id: Identifier for the collection

          query: Filter memberships by user names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.memberships",
            body=maybe_transform(
                {
                    "id": id,
                    "limit": limit,
                    "offset": offset,
                    "permission": permission,
                    "query": query,
                },
                membership_list_params.MembershipListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipListResponse,
        )


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        id: str,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MembershipListResponse:
        """This method allows you to list a collections individual memberships.

        It's
        important to note that memberships returned from this endpoint do not include
        group memberships.

        Args:
          id: Identifier for the collection

          query: Filter memberships by user names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.memberships",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "limit": limit,
                    "offset": offset,
                    "permission": permission,
                    "query": query,
                },
                membership_list_params.MembershipListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipListResponse,
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.list = to_raw_response_wrapper(
            memberships.list,
        )


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.list = async_to_raw_response_wrapper(
            memberships.list,
        )


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.list = to_streamed_response_wrapper(
            memberships.list,
        )


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.list = async_to_streamed_response_wrapper(
            memberships.list,
        )
