# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import attachment_create_params, attachment_delete_params, attachment_redirect_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.attachment_create_response import AttachmentCreateResponse
from ..types.attachment_delete_response import AttachmentDeleteResponse

__all__ = ["AttachmentsResource", "AsyncAttachmentsResource"]


class AttachmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttachmentsResourceWithRawResponse:
        return AttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttachmentsResourceWithStreamingResponse:
        return AttachmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content_type: str,
        name: str,
        size: float,
        document_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttachmentCreateResponse:
        """
        Creating an attachment object creates a database record and returns the inputs
        needed to generate a signed url and upload the file from the client to cloud
        storage.

        Args:
          size: Size of the file attachment in bytes.

          document_id: Identifier for the associated document, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/attachments.create",
            body=maybe_transform(
                {
                    "content_type": content_type,
                    "name": name,
                    "size": size,
                    "document_id": document_id,
                },
                attachment_create_params.AttachmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentCreateResponse,
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
    ) -> AttachmentDeleteResponse:
        """Deleting an attachment is permanant.

        It will not delete references or links to
        the attachment that may exist in your documents.

        Args:
          id: Unique identifier for the attachment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/attachments.delete",
            body=maybe_transform({"id": id}, attachment_delete_params.AttachmentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentDeleteResponse,
        )

    def redirect(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Load an attachment from where it is stored based on the id.

        If the attachment is
        private then a temporary, signed url with embedded credentials is generated on
        demand.

        Args:
          id: Unique identifier for the attachment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/attachments.redirect",
            body=maybe_transform({"id": id}, attachment_redirect_params.AttachmentRedirectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAttachmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttachmentsResourceWithRawResponse:
        return AsyncAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttachmentsResourceWithStreamingResponse:
        return AsyncAttachmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content_type: str,
        name: str,
        size: float,
        document_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttachmentCreateResponse:
        """
        Creating an attachment object creates a database record and returns the inputs
        needed to generate a signed url and upload the file from the client to cloud
        storage.

        Args:
          size: Size of the file attachment in bytes.

          document_id: Identifier for the associated document, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/attachments.create",
            body=await async_maybe_transform(
                {
                    "content_type": content_type,
                    "name": name,
                    "size": size,
                    "document_id": document_id,
                },
                attachment_create_params.AttachmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentCreateResponse,
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
    ) -> AttachmentDeleteResponse:
        """Deleting an attachment is permanant.

        It will not delete references or links to
        the attachment that may exist in your documents.

        Args:
          id: Unique identifier for the attachment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/attachments.delete",
            body=await async_maybe_transform({"id": id}, attachment_delete_params.AttachmentDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttachmentDeleteResponse,
        )

    async def redirect(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Load an attachment from where it is stored based on the id.

        If the attachment is
        private then a temporary, signed url with embedded credentials is generated on
        demand.

        Args:
          id: Unique identifier for the attachment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/attachments.redirect",
            body=await async_maybe_transform({"id": id}, attachment_redirect_params.AttachmentRedirectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.create = to_raw_response_wrapper(
            attachments.create,
        )
        self.delete = to_raw_response_wrapper(
            attachments.delete,
        )
        self.redirect = to_raw_response_wrapper(
            attachments.redirect,
        )


class AsyncAttachmentsResourceWithRawResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.create = async_to_raw_response_wrapper(
            attachments.create,
        )
        self.delete = async_to_raw_response_wrapper(
            attachments.delete,
        )
        self.redirect = async_to_raw_response_wrapper(
            attachments.redirect,
        )


class AttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AttachmentsResource) -> None:
        self._attachments = attachments

        self.create = to_streamed_response_wrapper(
            attachments.create,
        )
        self.delete = to_streamed_response_wrapper(
            attachments.delete,
        )
        self.redirect = to_streamed_response_wrapper(
            attachments.redirect,
        )


class AsyncAttachmentsResourceWithStreamingResponse:
    def __init__(self, attachments: AsyncAttachmentsResource) -> None:
        self._attachments = attachments

        self.create = async_to_streamed_response_wrapper(
            attachments.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            attachments.delete,
        )
        self.redirect = async_to_streamed_response_wrapper(
            attachments.redirect,
        )
