# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import comment_list_params, comment_create_params, comment_delete_params, comment_update_params
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
from ..types.comment_list_response import CommentListResponse
from ..types.comment_create_response import CommentCreateResponse
from ..types.comment_delete_response import CommentDeleteResponse
from ..types.comment_update_response import CommentUpdateResponse

__all__ = ["CommentsResource", "AsyncCommentsResource"]


class CommentsResource(SyncAPIResource):
    """
    `Comments` represent a comment either on a selection of text in a document
    or on the document itself.
    """

    @cached_property
    def with_raw_response(self) -> CommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return CommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return CommentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        document_id: str,
        id: str | Omit = omit,
        anchor_prefix: str | Omit = omit,
        anchor_suffix: str | Omit = omit,
        anchor_text: str | Omit = omit,
        data: object | Omit = omit,
        parent_comment_id: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateResponse:
        """
        Add a comment or reply to a document, either `data` or `text` is required.
        Provide `anchorText` to create an inline comment attached to a specific text
        range in the document.

        Args:
          anchor_prefix: Text immediately preceding `anchorText`, used to disambiguate between multiple
              occurrences. Requires `anchorText`.

          anchor_suffix: Text immediately following `anchorText`, used to disambiguate between multiple
              occurrences. Requires `anchorText`.

          anchor_text: Plain text substring to anchor the comment to as an inline comment. The first
              occurrence in the document's plain text is used unless disambiguated by
              `anchorPrefix` and/or `anchorSuffix`.

          data: The body of the comment.

          text: The body of the comment in markdown.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/comments.create",
            body=maybe_transform(
                {
                    "document_id": document_id,
                    "id": id,
                    "anchor_prefix": anchor_prefix,
                    "anchor_suffix": anchor_suffix,
                    "anchor_text": anchor_text,
                    "data": data,
                    "parent_comment_id": parent_comment_id,
                    "text": text,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        data: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentUpdateResponse:
        """
        Update a comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/comments.update",
            body=maybe_transform(
                {
                    "id": id,
                    "data": data,
                },
                comment_update_params.CommentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentUpdateResponse,
        )

    def list(
        self,
        *,
        collection_id: str | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        document_id: str | Omit = omit,
        include_anchor_text: bool | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentListResponse:
        """
        This method will list all comments matching the given properties.

        Args:
          collection_id: Filter to a specific collection

          document_id: Filter to a specific document

          include_anchor_text: Include the document text that the comment is anchored to, if any, in the
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/comments.list",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "direction": direction,
                    "document_id": document_id,
                    "include_anchor_text": include_anchor_text,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                comment_list_params.CommentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentListResponse,
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
    ) -> CommentDeleteResponse:
        """Deletes a comment.

        If the comment is a top-level comment, all its children will
        be deleted as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/comments.delete",
            body=maybe_transform({"id": id}, comment_delete_params.CommentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentDeleteResponse,
        )


class AsyncCommentsResource(AsyncAPIResource):
    """
    `Comments` represent a comment either on a selection of text in a document
    or on the document itself.
    """

    @cached_property
    def with_raw_response(self) -> AsyncCommentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return AsyncCommentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        document_id: str,
        id: str | Omit = omit,
        anchor_prefix: str | Omit = omit,
        anchor_suffix: str | Omit = omit,
        anchor_text: str | Omit = omit,
        data: object | Omit = omit,
        parent_comment_id: str | Omit = omit,
        text: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentCreateResponse:
        """
        Add a comment or reply to a document, either `data` or `text` is required.
        Provide `anchorText` to create an inline comment attached to a specific text
        range in the document.

        Args:
          anchor_prefix: Text immediately preceding `anchorText`, used to disambiguate between multiple
              occurrences. Requires `anchorText`.

          anchor_suffix: Text immediately following `anchorText`, used to disambiguate between multiple
              occurrences. Requires `anchorText`.

          anchor_text: Plain text substring to anchor the comment to as an inline comment. The first
              occurrence in the document's plain text is used unless disambiguated by
              `anchorPrefix` and/or `anchorSuffix`.

          data: The body of the comment.

          text: The body of the comment in markdown.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/comments.create",
            body=await async_maybe_transform(
                {
                    "document_id": document_id,
                    "id": id,
                    "anchor_prefix": anchor_prefix,
                    "anchor_suffix": anchor_suffix,
                    "anchor_text": anchor_text,
                    "data": data,
                    "parent_comment_id": parent_comment_id,
                    "text": text,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        data: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentUpdateResponse:
        """
        Update a comment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/comments.update",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "data": data,
                },
                comment_update_params.CommentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentUpdateResponse,
        )

    async def list(
        self,
        *,
        collection_id: str | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        document_id: str | Omit = omit,
        include_anchor_text: bool | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommentListResponse:
        """
        This method will list all comments matching the given properties.

        Args:
          collection_id: Filter to a specific collection

          document_id: Filter to a specific document

          include_anchor_text: Include the document text that the comment is anchored to, if any, in the
              response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/comments.list",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "direction": direction,
                    "document_id": document_id,
                    "include_anchor_text": include_anchor_text,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                comment_list_params.CommentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentListResponse,
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
    ) -> CommentDeleteResponse:
        """Deletes a comment.

        If the comment is a top-level comment, all its children will
        be deleted as well.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/comments.delete",
            body=await async_maybe_transform({"id": id}, comment_delete_params.CommentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommentDeleteResponse,
        )


class CommentsResourceWithRawResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_raw_response_wrapper(
            comments.create,
        )
        self.update = to_raw_response_wrapper(
            comments.update,
        )
        self.list = to_raw_response_wrapper(
            comments.list,
        )
        self.delete = to_raw_response_wrapper(
            comments.delete,
        )


class AsyncCommentsResourceWithRawResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_raw_response_wrapper(
            comments.create,
        )
        self.update = async_to_raw_response_wrapper(
            comments.update,
        )
        self.list = async_to_raw_response_wrapper(
            comments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            comments.delete,
        )


class CommentsResourceWithStreamingResponse:
    def __init__(self, comments: CommentsResource) -> None:
        self._comments = comments

        self.create = to_streamed_response_wrapper(
            comments.create,
        )
        self.update = to_streamed_response_wrapper(
            comments.update,
        )
        self.list = to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = to_streamed_response_wrapper(
            comments.delete,
        )


class AsyncCommentsResourceWithStreamingResponse:
    def __init__(self, comments: AsyncCommentsResource) -> None:
        self._comments = comments

        self.create = async_to_streamed_response_wrapper(
            comments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            comments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            comments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            comments.delete,
        )
