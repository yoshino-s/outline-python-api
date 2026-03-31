# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.collections import group_membership_list_params
from ...types.collections.group_membership_list_response import GroupMembershipListResponse

__all__ = ["GroupMembershipsResource", "AsyncGroupMembershipsResource"]


class GroupMembershipsResource(SyncAPIResource):
    """
    `Collections` represent grouping of documents in the knowledge base, they
    offer a way to structure information in a nested hierarchy and a level
    at which read and write permissions can be granted to individual users or
    groups of users.
    """

    @cached_property
    def with_raw_response(self) -> GroupMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return GroupMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return GroupMembershipsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        id: str,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        permission: Literal["read", "read_write"] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupMembershipListResponse:
        """This method allows you to list a collections group memberships.

        This is the list
        of groups that have been given access to the collection.

        Args:
          id: Identifier for the collection

          query: Filter memberships by group names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.group_memberships",
            body=maybe_transform(
                {
                    "id": id,
                    "limit": limit,
                    "offset": offset,
                    "permission": permission,
                    "query": query,
                },
                group_membership_list_params.GroupMembershipListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupMembershipListResponse,
        )


class AsyncGroupMembershipsResource(AsyncAPIResource):
    """
    `Collections` represent grouping of documents in the knowledge base, they
    offer a way to structure information in a nested hierarchy and a level
    at which read and write permissions can be granted to individual users or
    groups of users.
    """

    @cached_property
    def with_raw_response(self) -> AsyncGroupMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return AsyncGroupMembershipsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        id: str,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        permission: Literal["read", "read_write"] | Omit = omit,
        query: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupMembershipListResponse:
        """This method allows you to list a collections group memberships.

        This is the list
        of groups that have been given access to the collection.

        Args:
          id: Identifier for the collection

          query: Filter memberships by group names

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.group_memberships",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "limit": limit,
                    "offset": offset,
                    "permission": permission,
                    "query": query,
                },
                group_membership_list_params.GroupMembershipListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupMembershipListResponse,
        )


class GroupMembershipsResourceWithRawResponse:
    def __init__(self, group_memberships: GroupMembershipsResource) -> None:
        self._group_memberships = group_memberships

        self.list = to_raw_response_wrapper(
            group_memberships.list,
        )


class AsyncGroupMembershipsResourceWithRawResponse:
    def __init__(self, group_memberships: AsyncGroupMembershipsResource) -> None:
        self._group_memberships = group_memberships

        self.list = async_to_raw_response_wrapper(
            group_memberships.list,
        )


class GroupMembershipsResourceWithStreamingResponse:
    def __init__(self, group_memberships: GroupMembershipsResource) -> None:
        self._group_memberships = group_memberships

        self.list = to_streamed_response_wrapper(
            group_memberships.list,
        )


class AsyncGroupMembershipsResourceWithStreamingResponse:
    def __init__(self, group_memberships: AsyncGroupMembershipsResource) -> None:
        self._group_memberships = group_memberships

        self.list = async_to_streamed_response_wrapper(
            group_memberships.list,
        )
