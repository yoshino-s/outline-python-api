# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    collection_list_params,
    collection_create_params,
    collection_delete_params,
    collection_export_params,
    collection_update_params,
    collection_add_user_params,
    collection_retrieve_params,
    collection_add_group_params,
    collection_documents_params,
    collection_export_all_params,
    collection_remove_user_params,
    collection_remove_group_params,
)
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
from .memberships import (
    MembershipsResource,
    AsyncMembershipsResource,
    MembershipsResourceWithRawResponse,
    AsyncMembershipsResourceWithRawResponse,
    MembershipsResourceWithStreamingResponse,
    AsyncMembershipsResourceWithStreamingResponse,
)
from ..._base_client import (
    make_request_options,
)
from .group_memberships import (
    GroupMembershipsResource,
    AsyncGroupMembershipsResource,
    GroupMembershipsResourceWithRawResponse,
    AsyncGroupMembershipsResourceWithRawResponse,
    GroupMembershipsResourceWithStreamingResponse,
    AsyncGroupMembershipsResourceWithStreamingResponse,
)
from ...types.collection_list_response import CollectionListResponse
from ...types.collection_create_response import CollectionCreateResponse
from ...types.collection_delete_response import CollectionDeleteResponse
from ...types.collection_export_response import CollectionExportResponse
from ...types.collection_update_response import CollectionUpdateResponse
from ...types.collection_add_user_response import CollectionAddUserResponse
from ...types.collection_retrieve_response import CollectionRetrieveResponse
from ...types.collection_add_group_response import CollectionAddGroupResponse
from ...types.collection_documents_response import CollectionDocumentsResponse
from ...types.collection_export_all_response import CollectionExportAllResponse
from ...types.collection_remove_user_response import CollectionRemoveUserResponse
from ...types.collection_remove_group_response import CollectionRemoveGroupResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

    @cached_property
    def group_memberships(self) -> GroupMembershipsResource:
        return GroupMembershipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        color: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionCreateResponse:
        """
        Create a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.create",
            body=maybe_transform(
                {
                    "name": name,
                    "color": color,
                    "description": description,
                    "permission": permission,
                    "private": private,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRetrieveResponse:
        """
        Retrieve a collection

        Args:
          id: Unique identifier for the collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.info",
            body=maybe_transform({"id": id}, collection_retrieve_params.CollectionRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    def update(
        self,
        *,
        id: str,
        color: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionUpdateResponse:
        """
        Update a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.update",
            body=maybe_transform(
                {
                    "id": id,
                    "color": color,
                    "description": description,
                    "name": name,
                    "permission": permission,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    def list(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        List all collections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.list",
            body=maybe_transform(
                {
                    "limit": limit,
                    "offset": offset,
                },
                collection_list_params.CollectionListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionListResponse,
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
    ) -> CollectionDeleteResponse:
        """Delete a collection and all of its documents.

        This action can’t be undone so
        please be careful.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.delete",
            body=maybe_transform({"id": id}, collection_delete_params.CollectionDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteResponse,
        )

    def add_group(
        self,
        *,
        id: str,
        group_id: str,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionAddGroupResponse:
        """
        This method allows you to give all members in a group access to a collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.add_group",
            body=maybe_transform(
                {
                    "id": id,
                    "group_id": group_id,
                    "permission": permission,
                },
                collection_add_group_params.CollectionAddGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddGroupResponse,
        )

    def add_user(
        self,
        *,
        id: str,
        user_id: str,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionAddUserResponse:
        """
        This method allows you to add a user membership to the specified collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.add_user",
            body=maybe_transform(
                {
                    "id": id,
                    "user_id": user_id,
                    "permission": permission,
                },
                collection_add_user_params.CollectionAddUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddUserResponse,
        )

    def documents(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDocumentsResponse:
        """
        Retrieve a collections document structure

        Args:
          id: Unique identifier for the collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.documents",
            body=maybe_transform({"id": id}, collection_documents_params.CollectionDocumentsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDocumentsResponse,
        )

    def export(
        self,
        *,
        id: str,
        format: Literal["outline-markdown", "json", "html"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionExportResponse:
        """
        Triggers a bulk export of the collection in markdown format and their
        attachments. If documents are nested then they will be nested in folders inside
        the zip file. The endpoint returns a `FileOperation` that can be queried to
        track the progress of the export and get the url for the final file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.export",
            body=maybe_transform(
                {
                    "id": id,
                    "format": format,
                },
                collection_export_params.CollectionExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionExportResponse,
        )

    def export_all(
        self,
        *,
        format: Literal["outline-markdown", "json", "html"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionExportAllResponse:
        """Triggers a bulk export of all documents in and their attachments.

        The endpoint
        returns a `FileOperation` that can be queried through the fileOperations
        endpoint to track the progress of the export and get the url for the final file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.export_all",
            body=maybe_transform({"format": format}, collection_export_all_params.CollectionExportAllParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionExportAllResponse,
        )

    def remove_group(
        self,
        *,
        id: str,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRemoveGroupResponse:
        """
        This method allows you to revoke all members in a group access to a collection.
        Note that members of the group may still retain access through other groups or
        individual memberships.

        Args:
          id: Identifier for the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.remove_group",
            body=maybe_transform(
                {
                    "id": id,
                    "group_id": group_id,
                },
                collection_remove_group_params.CollectionRemoveGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRemoveGroupResponse,
        )

    def remove_user(
        self,
        *,
        id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRemoveUserResponse:
        """
        This method allows you to remove a user from the specified collection.

        Args:
          id: Identifier for the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.remove_user",
            body=maybe_transform(
                {
                    "id": id,
                    "user_id": user_id,
                },
                collection_remove_user_params.CollectionRemoveUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRemoveUserResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

    @cached_property
    def group_memberships(self) -> AsyncGroupMembershipsResource:
        return AsyncGroupMembershipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        color: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionCreateResponse:
        """
        Create a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "color": color,
                    "description": description,
                    "permission": permission,
                    "private": private,
                },
                collection_create_params.CollectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRetrieveResponse:
        """
        Retrieve a collection

        Args:
          id: Unique identifier for the collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.info",
            body=await async_maybe_transform({"id": id}, collection_retrieve_params.CollectionRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRetrieveResponse,
        )

    async def update(
        self,
        *,
        id: str,
        color: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionUpdateResponse:
        """
        Update a collection

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.update",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "color": color,
                    "description": description,
                    "name": name,
                    "permission": permission,
                },
                collection_update_params.CollectionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionUpdateResponse,
        )

    async def list(
        self,
        *,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """
        List all collections

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.list",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "offset": offset,
                },
                collection_list_params.CollectionListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionListResponse,
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
    ) -> CollectionDeleteResponse:
        """Delete a collection and all of its documents.

        This action can’t be undone so
        please be careful.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.delete",
            body=await async_maybe_transform({"id": id}, collection_delete_params.CollectionDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteResponse,
        )

    async def add_group(
        self,
        *,
        id: str,
        group_id: str,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionAddGroupResponse:
        """
        This method allows you to give all members in a group access to a collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.add_group",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "group_id": group_id,
                    "permission": permission,
                },
                collection_add_group_params.CollectionAddGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddGroupResponse,
        )

    async def add_user(
        self,
        *,
        id: str,
        user_id: str,
        permission: Literal["read", "read_write"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionAddUserResponse:
        """
        This method allows you to add a user membership to the specified collection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.add_user",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "user_id": user_id,
                    "permission": permission,
                },
                collection_add_user_params.CollectionAddUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddUserResponse,
        )

    async def documents(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDocumentsResponse:
        """
        Retrieve a collections document structure

        Args:
          id: Unique identifier for the collection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.documents",
            body=await async_maybe_transform({"id": id}, collection_documents_params.CollectionDocumentsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDocumentsResponse,
        )

    async def export(
        self,
        *,
        id: str,
        format: Literal["outline-markdown", "json", "html"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionExportResponse:
        """
        Triggers a bulk export of the collection in markdown format and their
        attachments. If documents are nested then they will be nested in folders inside
        the zip file. The endpoint returns a `FileOperation` that can be queried to
        track the progress of the export and get the url for the final file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.export",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "format": format,
                },
                collection_export_params.CollectionExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionExportResponse,
        )

    async def export_all(
        self,
        *,
        format: Literal["outline-markdown", "json", "html"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionExportAllResponse:
        """Triggers a bulk export of all documents in and their attachments.

        The endpoint
        returns a `FileOperation` that can be queried through the fileOperations
        endpoint to track the progress of the export and get the url for the final file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.export_all",
            body=await async_maybe_transform(
                {"format": format}, collection_export_all_params.CollectionExportAllParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionExportAllResponse,
        )

    async def remove_group(
        self,
        *,
        id: str,
        group_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRemoveGroupResponse:
        """
        This method allows you to revoke all members in a group access to a collection.
        Note that members of the group may still retain access through other groups or
        individual memberships.

        Args:
          id: Identifier for the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.remove_group",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "group_id": group_id,
                },
                collection_remove_group_params.CollectionRemoveGroupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRemoveGroupResponse,
        )

    async def remove_user(
        self,
        *,
        id: str,
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRemoveUserResponse:
        """
        This method allows you to remove a user from the specified collection.

        Args:
          id: Identifier for the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.remove_user",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "user_id": user_id,
                },
                collection_remove_user_params.CollectionRemoveUserParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionRemoveUserResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = to_raw_response_wrapper(
            collections.update,
        )
        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.add_group = to_raw_response_wrapper(
            collections.add_group,
        )
        self.add_user = to_raw_response_wrapper(
            collections.add_user,
        )
        self.documents = to_raw_response_wrapper(
            collections.documents,
        )
        self.export = to_raw_response_wrapper(
            collections.export,
        )
        self.export_all = to_raw_response_wrapper(
            collections.export_all,
        )
        self.remove_group = to_raw_response_wrapper(
            collections.remove_group,
        )
        self.remove_user = to_raw_response_wrapper(
            collections.remove_user,
        )

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> GroupMembershipsResourceWithRawResponse:
        return GroupMembershipsResourceWithRawResponse(self._collections.group_memberships)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_raw_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            collections.update,
        )
        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.add_group = async_to_raw_response_wrapper(
            collections.add_group,
        )
        self.add_user = async_to_raw_response_wrapper(
            collections.add_user,
        )
        self.documents = async_to_raw_response_wrapper(
            collections.documents,
        )
        self.export = async_to_raw_response_wrapper(
            collections.export,
        )
        self.export_all = async_to_raw_response_wrapper(
            collections.export_all,
        )
        self.remove_group = async_to_raw_response_wrapper(
            collections.remove_group,
        )
        self.remove_user = async_to_raw_response_wrapper(
            collections.remove_user,
        )

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> AsyncGroupMembershipsResourceWithRawResponse:
        return AsyncGroupMembershipsResourceWithRawResponse(self._collections.group_memberships)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.create = to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            collections.update,
        )
        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.add_group = to_streamed_response_wrapper(
            collections.add_group,
        )
        self.add_user = to_streamed_response_wrapper(
            collections.add_user,
        )
        self.documents = to_streamed_response_wrapper(
            collections.documents,
        )
        self.export = to_streamed_response_wrapper(
            collections.export,
        )
        self.export_all = to_streamed_response_wrapper(
            collections.export_all,
        )
        self.remove_group = to_streamed_response_wrapper(
            collections.remove_group,
        )
        self.remove_user = to_streamed_response_wrapper(
            collections.remove_user,
        )

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> GroupMembershipsResourceWithStreamingResponse:
        return GroupMembershipsResourceWithStreamingResponse(self._collections.group_memberships)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.create = async_to_streamed_response_wrapper(
            collections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            collections.update,
        )
        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.add_group = async_to_streamed_response_wrapper(
            collections.add_group,
        )
        self.add_user = async_to_streamed_response_wrapper(
            collections.add_user,
        )
        self.documents = async_to_streamed_response_wrapper(
            collections.documents,
        )
        self.export = async_to_streamed_response_wrapper(
            collections.export,
        )
        self.export_all = async_to_streamed_response_wrapper(
            collections.export_all,
        )
        self.remove_group = async_to_streamed_response_wrapper(
            collections.remove_group,
        )
        self.remove_user = async_to_streamed_response_wrapper(
            collections.remove_user,
        )

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> AsyncGroupMembershipsResourceWithStreamingResponse:
        return AsyncGroupMembershipsResourceWithStreamingResponse(self._collections.group_memberships)
