# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    group_info_params,
    group_list_params,
    group_create_params,
    group_delete_params,
    group_update_params,
)
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
from ..types.group_info_response import GroupInfoResponse
from ..types.group_list_response import GroupListResponse
from ..types.group_create_response import GroupCreateResponse
from ..types.group_delete_response import GroupDeleteResponse
from ..types.group_update_response import GroupUpdateResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupCreateResponse:
        """
        Create a group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups.create",
            body=maybe_transform({"name": name}, group_create_params.GroupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """
        Update a group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups.update",
            body=maybe_transform(
                {
                    "id": id,
                    "name": name,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    def list(
        self,
        *,
        direction: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupListResponse:
        """
        List all groups

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups.list",
            body=maybe_transform(
                {
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                group_list_params.GroupListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupListResponse,
        )

    def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupDeleteResponse:
        """
        Deleting a group will cause all of its members to lose access to any collections
        the group has previously been added to. This action can’t be undone so please be
        careful.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups.delete",
            body=maybe_transform({"id": id}, group_delete_params.GroupDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupDeleteResponse,
        )

    def info(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupInfoResponse:
        """
        Retrieve a group

        Args:
          id: Unique identifier for the group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/groups.info",
            body=maybe_transform({"id": id}, group_info_params.GroupInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupInfoResponse,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupCreateResponse:
        """
        Create a group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups.create",
            body=await async_maybe_transform({"name": name}, group_create_params.GroupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupUpdateResponse:
        """
        Update a group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups.update",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "name": name,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    async def list(
        self,
        *,
        direction: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupListResponse:
        """
        List all groups

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups.list",
            body=await async_maybe_transform(
                {
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                group_list_params.GroupListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupListResponse,
        )

    async def delete(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupDeleteResponse:
        """
        Deleting a group will cause all of its members to lose access to any collections
        the group has previously been added to. This action can’t be undone so please be
        careful.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups.delete",
            body=await async_maybe_transform({"id": id}, group_delete_params.GroupDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupDeleteResponse,
        )

    async def info(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GroupInfoResponse:
        """
        Retrieve a group

        Args:
          id: Unique identifier for the group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/groups.info",
            body=await async_maybe_transform({"id": id}, group_info_params.GroupInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupInfoResponse,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )
        self.info = to_raw_response_wrapper(
            groups.info,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )
        self.info = async_to_raw_response_wrapper(
            groups.info,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )
        self.info = to_streamed_response_wrapper(
            groups.info,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )
        self.info = async_to_streamed_response_wrapper(
            groups.info,
        )
