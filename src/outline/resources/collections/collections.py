# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
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
from .memberships import (
    MembershipsResource,
    AsyncMembershipsResource,
    MembershipsResourceWithRawResponse,
    AsyncMembershipsResourceWithRawResponse,
    MembershipsResourceWithStreamingResponse,
    AsyncMembershipsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
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
    """
    `Collections` represent grouping of documents in the knowledge base, they
    offer a way to structure information in a nested hierarchy and a level
    at which read and write permissions can be granted to individual users or
    groups of users.
    """

    @cached_property
    def memberships(self) -> MembershipsResource:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return MembershipsResource(self._client)

    @cached_property
    def group_memberships(self) -> GroupMembershipsResource:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return GroupMembershipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        color: str | Omit = omit,
        data: object | Omit = omit,
        description: str | Omit = omit,
        icon: str | Omit = omit,
        permission: Literal["read", "read_write"] | Omit = omit,
        sharing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionCreateResponse:
        """
        Create a new collection with the specified name, description, icon, color, and
        permission settings. Collections are used to organize documents.

        Args:
          color: A hex color code for the collection icon

          data: The collection description as a rich-text ProseMirror JSON document. Only one of
              `description` or `data` may be provided.

          description: A brief description of the collection, markdown supported. Only one of
              `description` or `data` may be provided.

          icon: A string that represents an icon in the outline-icons package or an emoji

          sharing: Whether public sharing of documents is allowed

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
                    "data": data,
                    "description": description,
                    "icon": icon,
                    "permission": permission,
                    "sharing": sharing,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRetrieveResponse:
        """
        Retrieve the details of a collection by its unique identifier.

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
        color: str | Omit = omit,
        data: object | Omit = omit,
        description: str | Omit = omit,
        icon: str | Omit = omit,
        name: str | Omit = omit,
        permission: Literal["read", "read_write"] | Omit = omit,
        sharing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionUpdateResponse:
        """
        Update an existing collection's properties such as name, description, icon,
        color, sharing settings, or permission level.

        Args:
          color: A hex color code for the collection icon

          data: The collection description as a rich-text ProseMirror JSON document. Only one of
              `description` or `data` may be provided.

          description: A brief description of the collection, markdown supported. Only one of
              `description` or `data` may be provided.

          icon: A string that represents an icon in the outline-icons package or an emoji

          sharing: Whether public sharing of documents is allowed

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
                    "data": data,
                    "description": description,
                    "icon": icon,
                    "name": name,
                    "permission": permission,
                    "sharing": sharing,
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
        direction: Literal["ASC", "DESC"] | Omit = omit,
        filters: Iterable[collection_list_params.Filter] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        query: str | Omit = omit,
        sort: str | Omit = omit,
        status_filter: List[Literal["archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        List all collections that the authenticated user has access to.

        Args:
          filters: Structured filter expression, evaluated as an AND of top-level entries. Cannot
              be combined with the deprecated `query` or `statusFilter` parameters.

          query: If set, will filter the results by collection name. Deprecated – prefer the
              `filters` parameter.

          status_filter: An optional array of statuses to filter by. Deprecated – prefer the `filters`
              parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.list",
            body=maybe_transform(
                {
                    "direction": direction,
                    "filters": filters,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort": sort,
                    "status_filter": status_filter,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        permission: Literal["read", "read_write"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        permission: Literal["read", "read_write"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionAddUserResponse:
        """
        This method allows you to add a user membership to the specified collection.

        Args:
          id: Identifier for the collection

          user_id: Identifier for the user to add to the collection

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionDocumentsResponse:
        """
        Returns the document structure of a collection as a tree of navigation nodes,
        representing the hierarchy of documents within the collection.

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
        format: Literal["outline-markdown", "json", "html"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        format: Literal["outline-markdown", "json", "html"] | Omit = omit,
        include_attachments: bool | Omit = omit,
        include_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionExportAllResponse:
        """Triggers a bulk export of multiple collections and their documents.

        The endpoint
        returns a `FileOperation` that can be queried through the fileOperations
        endpoint to track the progress of the export and get the url for the final file.

        Args:
          include_attachments: Whether to include attachments in the export.

          include_private: Whether to include private collections in the export.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections.export_all",
            body=maybe_transform(
                {
                    "format": format,
                    "include_attachments": include_attachments,
                    "include_private": include_private,
                },
                collection_export_all_params.CollectionExportAllParams,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRemoveUserResponse:
        """
        This method allows you to remove a user from the specified collection.

        Args:
          id: Identifier for the collection

          user_id: Identifier for the user to remove from the collection

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
    """
    `Collections` represent grouping of documents in the knowledge base, they
    offer a way to structure information in a nested hierarchy and a level
    at which read and write permissions can be granted to individual users or
    groups of users.
    """

    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return AsyncMembershipsResource(self._client)

    @cached_property
    def group_memberships(self) -> AsyncGroupMembershipsResource:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return AsyncGroupMembershipsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        color: str | Omit = omit,
        data: object | Omit = omit,
        description: str | Omit = omit,
        icon: str | Omit = omit,
        permission: Literal["read", "read_write"] | Omit = omit,
        sharing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionCreateResponse:
        """
        Create a new collection with the specified name, description, icon, color, and
        permission settings. Collections are used to organize documents.

        Args:
          color: A hex color code for the collection icon

          data: The collection description as a rich-text ProseMirror JSON document. Only one of
              `description` or `data` may be provided.

          description: A brief description of the collection, markdown supported. Only one of
              `description` or `data` may be provided.

          icon: A string that represents an icon in the outline-icons package or an emoji

          sharing: Whether public sharing of documents is allowed

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
                    "data": data,
                    "description": description,
                    "icon": icon,
                    "permission": permission,
                    "sharing": sharing,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRetrieveResponse:
        """
        Retrieve the details of a collection by its unique identifier.

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
        color: str | Omit = omit,
        data: object | Omit = omit,
        description: str | Omit = omit,
        icon: str | Omit = omit,
        name: str | Omit = omit,
        permission: Literal["read", "read_write"] | Omit = omit,
        sharing: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionUpdateResponse:
        """
        Update an existing collection's properties such as name, description, icon,
        color, sharing settings, or permission level.

        Args:
          color: A hex color code for the collection icon

          data: The collection description as a rich-text ProseMirror JSON document. Only one of
              `description` or `data` may be provided.

          description: A brief description of the collection, markdown supported. Only one of
              `description` or `data` may be provided.

          icon: A string that represents an icon in the outline-icons package or an emoji

          sharing: Whether public sharing of documents is allowed

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
                    "data": data,
                    "description": description,
                    "icon": icon,
                    "name": name,
                    "permission": permission,
                    "sharing": sharing,
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
        direction: Literal["ASC", "DESC"] | Omit = omit,
        filters: Iterable[collection_list_params.Filter] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        query: str | Omit = omit,
        sort: str | Omit = omit,
        status_filter: List[Literal["archived"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionListResponse:
        """
        List all collections that the authenticated user has access to.

        Args:
          filters: Structured filter expression, evaluated as an AND of top-level entries. Cannot
              be combined with the deprecated `query` or `statusFilter` parameters.

          query: If set, will filter the results by collection name. Deprecated – prefer the
              `filters` parameter.

          status_filter: An optional array of statuses to filter by. Deprecated – prefer the `filters`
              parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.list",
            body=await async_maybe_transform(
                {
                    "direction": direction,
                    "filters": filters,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "sort": sort,
                    "status_filter": status_filter,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        permission: Literal["read", "read_write"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        permission: Literal["read", "read_write"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionAddUserResponse:
        """
        This method allows you to add a user membership to the specified collection.

        Args:
          id: Identifier for the collection

          user_id: Identifier for the user to add to the collection

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionDocumentsResponse:
        """
        Returns the document structure of a collection as a tree of navigation nodes,
        representing the hierarchy of documents within the collection.

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
        format: Literal["outline-markdown", "json", "html"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        format: Literal["outline-markdown", "json", "html"] | Omit = omit,
        include_attachments: bool | Omit = omit,
        include_private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionExportAllResponse:
        """Triggers a bulk export of multiple collections and their documents.

        The endpoint
        returns a `FileOperation` that can be queried through the fileOperations
        endpoint to track the progress of the export and get the url for the final file.

        Args:
          include_attachments: Whether to include attachments in the export.

          include_private: Whether to include private collections in the export.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections.export_all",
            body=await async_maybe_transform(
                {
                    "format": format,
                    "include_attachments": include_attachments,
                    "include_private": include_private,
                },
                collection_export_all_params.CollectionExportAllParams,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionRemoveUserResponse:
        """
        This method allows you to remove a user from the specified collection.

        Args:
          id: Identifier for the collection

          user_id: Identifier for the user to remove from the collection

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
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return MembershipsResourceWithRawResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> GroupMembershipsResourceWithRawResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
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
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return AsyncMembershipsResourceWithRawResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> AsyncGroupMembershipsResourceWithRawResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
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
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return MembershipsResourceWithStreamingResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> GroupMembershipsResourceWithStreamingResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
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
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return AsyncMembershipsResourceWithStreamingResponse(self._collections.memberships)

    @cached_property
    def group_memberships(self) -> AsyncGroupMembershipsResourceWithStreamingResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        return AsyncGroupMembershipsResourceWithStreamingResponse(self._collections.group_memberships)
