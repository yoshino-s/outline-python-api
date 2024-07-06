# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    document_info_params,
    document_list_params,
    document_move_params,
    document_star_params,
    document_create_params,
    document_delete_params,
    document_drafts_params,
    document_export_params,
    document_import_params,
    document_search_params,
    document_unstar_params,
    document_update_params,
    document_viewed_params,
    document_archive_params,
    document_restore_params,
    document_unpublish_params,
    document_templatize_params,
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
from ..types.document_info_response import DocumentInfoResponse
from ..types.document_list_response import DocumentListResponse
from ..types.document_move_response import DocumentMoveResponse
from ..types.document_star_response import DocumentStarResponse
from ..types.document_create_response import DocumentCreateResponse
from ..types.document_delete_response import DocumentDeleteResponse
from ..types.document_drafts_response import DocumentDraftsResponse
from ..types.document_export_response import DocumentExportResponse
from ..types.document_import_response import DocumentImportResponse
from ..types.document_search_response import DocumentSearchResponse
from ..types.document_unstar_response import DocumentUnstarResponse
from ..types.document_update_response import DocumentUpdateResponse
from ..types.document_viewed_response import DocumentViewedResponse
from ..types.document_archive_response import DocumentArchiveResponse
from ..types.document_restore_response import DocumentRestoreResponse
from ..types.document_unpublish_response import DocumentUnpublishResponse
from ..types.document_templatize_response import DocumentTemplatizeResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        collection_id: str,
        title: str,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        template_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentCreateResponse:
        """This method allows you to create or publish a new document.

        By default a
        document is set to the collection root. If you want to create a nested/child
        document, you should pass parentDocumentId to set the parent document.

        Args:
          publish: Whether this document should be immediately published and made visible to other
              team members.

          template: Whether this document should be considered to be a template.

          text: The body of the document, may contain markdown formatting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.create",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "title": title,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
                    "template": template,
                    "template_id": template_id,
                    "text": text,
                },
                document_create_params.DocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )

    def update(
        self,
        *,
        id: str,
        append: bool | NotGiven = NOT_GIVEN,
        done: bool | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUpdateResponse:
        """
        This method allows you to modify an already created document

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          append: If true the text field will be appended to the end of the existing document,
              rather than the default behavior of replacing it. This is potentially useful for
              things like logging into a document.

          done: Whether the editing session has finished, this will trigger any notifications.
              This property will soon be deprecated.

          publish: Whether this document should be published and made visible to other team
              members, if a draft

          text: The body of the document, may contain markdown formatting.

          title: The title of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.update",
            body=maybe_transform(
                {
                    "id": id,
                    "append": append,
                    "done": done,
                    "publish": publish,
                    "text": text,
                    "title": title,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    def list(
        self,
        *,
        backlink_document_id: str | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentListResponse:
        """
        This method will list all published documents and draft documents belonging to
        the current user.

        Args:
          collection_id: Optionally filter to a specific collection

          template: Optionally filter to only templates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.list",
            body=maybe_transform(
                {
                    "backlink_document_id": backlink_document_id,
                    "collection_id": collection_id,
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "parent_document_id": parent_document_id,
                    "sort": sort,
                    "template": template,
                    "user_id": user_id,
                },
                document_list_params.DocumentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentListResponse,
        )

    def delete(
        self,
        *,
        id: str,
        permanent: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentDeleteResponse:
        """Deleting a document moves it to the trash.

        If not restored within 30 days it is
        permenantly deleted.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          permanent: If set to true the document will be destroyed with no way to recover rather than
              moved to the trash.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.delete",
            body=maybe_transform(
                {
                    "id": id,
                    "permanent": permanent,
                },
                document_delete_params.DocumentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    def archive(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentArchiveResponse:
        """
        Archiving a document allows outdated information to be moved out of sight whilst
        retaining the ability to optionally search and restore it later.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.archive",
            body=maybe_transform({"id": id}, document_archive_params.DocumentArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentArchiveResponse,
        )

    def drafts(
        self,
        *,
        collection_id: str | NotGiven = NOT_GIVEN,
        date_filter: Literal["day", "week", "month", "year"] | NotGiven = NOT_GIVEN,
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
    ) -> DocumentDraftsResponse:
        """
        This method will list all draft documents belonging to the current user.

        Args:
          collection_id: A collection to search within

          date_filter: Any documents that have not been updated within the specified period will be
              filtered out

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.drafts",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "date_filter": date_filter,
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                document_drafts_params.DocumentDraftsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDraftsResponse,
        )

    def export(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentExportResponse:
        """Export a document as markdown

        Args:
          id: Unique identifier for the document.

        Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.export",
            body=maybe_transform({"id": id}, document_export_params.DocumentExportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentExportResponse,
        )

    def import_(
        self,
        *,
        collection_id: str | NotGiven = NOT_GIVEN,
        file: object | NotGiven = NOT_GIVEN,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentImportResponse:
        """
        This method allows you to create a new document by importing an existing file.
        By default a document is set to the collection root. If you want to create a
        nested/child document, you should pass parentDocumentId to set the parent
        document.

        Args:
          file: Only plain text, markdown, docx, and html format are supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/documents.import",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "file": file,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
                    "template": template,
                },
                document_import_params.DocumentImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentImportResponse,
        )

    def info(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        share_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentInfoResponse:
        """Retrieve a document

        Args:
          id: Unique identifier for the document.

        Either the UUID or the urlId is acceptable.

          share_id: Unique identifier for a document share, a shareId may be used in place of a
              document UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.info",
            body=maybe_transform(
                {
                    "id": id,
                    "share_id": share_id,
                },
                document_info_params.DocumentInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentInfoResponse,
        )

    def move(
        self,
        *,
        id: str,
        collection_id: str | NotGiven = NOT_GIVEN,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentMoveResponse:
        """Move a document to a new location or collection.

        If no parent document is
        provided, the document will be moved to the collection root.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.move",
            body=maybe_transform(
                {
                    "id": id,
                    "collection_id": collection_id,
                    "parent_document_id": parent_document_id,
                },
                document_move_params.DocumentMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentMoveResponse,
        )

    def restore(
        self,
        *,
        id: str,
        revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentRestoreResponse:
        """If a document has been archived or deleted, it can be restored.

        Optionally a
        revision can be passed to restore the document to a previous point in time.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          revision_id: Identifier for the revision to restore to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.restore",
            body=maybe_transform(
                {
                    "id": id,
                    "revision_id": revision_id,
                },
                document_restore_params.DocumentRestoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentRestoreResponse,
        )

    def search(
        self,
        *,
        collection_id: str | NotGiven = NOT_GIVEN,
        date_filter: Literal["day", "week", "month", "year"] | NotGiven = NOT_GIVEN,
        document_id: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        status_filter: Literal["draft", "archived", "published"] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentSearchResponse:
        """This methods allows you to search your teams documents with keywords.

        Note that
        search results will be restricted to those accessible by the current access
        token.

        Args:
          collection_id: A collection to search within

          date_filter: Any documents that have not been updated within the specified period will be
              filtered out

          document_id: A document to search within

          status_filter: Any documents that are not in the specified status will be filtered out

          user_id: Any documents that have not been edited by the user identifier will be filtered
              out

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.search",
            body=maybe_transform(
                {
                    "collection_id": collection_id,
                    "date_filter": date_filter,
                    "document_id": document_id,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "status_filter": status_filter,
                    "user_id": user_id,
                },
                document_search_params.DocumentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentSearchResponse,
        )

    def star(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStarResponse:
        """
        Starring a document gives it extra priority in the UI and makes it easier to
        find important information later.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.star",
            body=maybe_transform({"id": id}, document_star_params.DocumentStarParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStarResponse,
        )

    def templatize(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentTemplatizeResponse:
        """
        This method allows you to createa new template using an existing document as the
        basis

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.templatize",
            body=maybe_transform({"id": id}, document_templatize_params.DocumentTemplatizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentTemplatizeResponse,
        )

    def unpublish(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUnpublishResponse:
        """
        Unpublishing a document moves it back to a draft status and out of the
        collection.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.unpublish",
            body=maybe_transform({"id": id}, document_unpublish_params.DocumentUnpublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUnpublishResponse,
        )

    def unstar(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUnstarResponse:
        """
        Starring a document gives it extra priority in the UI and makes it easier to
        find important information later.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.unstar",
            body=maybe_transform({"id": id}, document_unstar_params.DocumentUnstarParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUnstarResponse,
        )

    def viewed(
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
    ) -> DocumentViewedResponse:
        """
        This method will list all documents recently viewed by the current user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.viewed",
            body=maybe_transform(
                {
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                document_viewed_params.DocumentViewedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentViewedResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        collection_id: str,
        title: str,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        template_id: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentCreateResponse:
        """This method allows you to create or publish a new document.

        By default a
        document is set to the collection root. If you want to create a nested/child
        document, you should pass parentDocumentId to set the parent document.

        Args:
          publish: Whether this document should be immediately published and made visible to other
              team members.

          template: Whether this document should be considered to be a template.

          text: The body of the document, may contain markdown formatting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.create",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "title": title,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
                    "template": template,
                    "template_id": template_id,
                    "text": text,
                },
                document_create_params.DocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )

    async def update(
        self,
        *,
        id: str,
        append: bool | NotGiven = NOT_GIVEN,
        done: bool | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUpdateResponse:
        """
        This method allows you to modify an already created document

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          append: If true the text field will be appended to the end of the existing document,
              rather than the default behavior of replacing it. This is potentially useful for
              things like logging into a document.

          done: Whether the editing session has finished, this will trigger any notifications.
              This property will soon be deprecated.

          publish: Whether this document should be published and made visible to other team
              members, if a draft

          text: The body of the document, may contain markdown formatting.

          title: The title of the document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.update",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "append": append,
                    "done": done,
                    "publish": publish,
                    "text": text,
                    "title": title,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    async def list(
        self,
        *,
        backlink_document_id: str | NotGiven = NOT_GIVEN,
        collection_id: str | NotGiven = NOT_GIVEN,
        direction: Literal["ASC", "DESC"] | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentListResponse:
        """
        This method will list all published documents and draft documents belonging to
        the current user.

        Args:
          collection_id: Optionally filter to a specific collection

          template: Optionally filter to only templates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.list",
            body=await async_maybe_transform(
                {
                    "backlink_document_id": backlink_document_id,
                    "collection_id": collection_id,
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "parent_document_id": parent_document_id,
                    "sort": sort,
                    "template": template,
                    "user_id": user_id,
                },
                document_list_params.DocumentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentListResponse,
        )

    async def delete(
        self,
        *,
        id: str,
        permanent: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentDeleteResponse:
        """Deleting a document moves it to the trash.

        If not restored within 30 days it is
        permenantly deleted.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          permanent: If set to true the document will be destroyed with no way to recover rather than
              moved to the trash.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.delete",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "permanent": permanent,
                },
                document_delete_params.DocumentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    async def archive(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentArchiveResponse:
        """
        Archiving a document allows outdated information to be moved out of sight whilst
        retaining the ability to optionally search and restore it later.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.archive",
            body=await async_maybe_transform({"id": id}, document_archive_params.DocumentArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentArchiveResponse,
        )

    async def drafts(
        self,
        *,
        collection_id: str | NotGiven = NOT_GIVEN,
        date_filter: Literal["day", "week", "month", "year"] | NotGiven = NOT_GIVEN,
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
    ) -> DocumentDraftsResponse:
        """
        This method will list all draft documents belonging to the current user.

        Args:
          collection_id: A collection to search within

          date_filter: Any documents that have not been updated within the specified period will be
              filtered out

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.drafts",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "date_filter": date_filter,
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                document_drafts_params.DocumentDraftsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDraftsResponse,
        )

    async def export(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentExportResponse:
        """Export a document as markdown

        Args:
          id: Unique identifier for the document.

        Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.export",
            body=await async_maybe_transform({"id": id}, document_export_params.DocumentExportParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentExportResponse,
        )

    async def import_(
        self,
        *,
        collection_id: str | NotGiven = NOT_GIVEN,
        file: object | NotGiven = NOT_GIVEN,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        template: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentImportResponse:
        """
        This method allows you to create a new document by importing an existing file.
        By default a document is set to the collection root. If you want to create a
        nested/child document, you should pass parentDocumentId to set the parent
        document.

        Args:
          file: Only plain text, markdown, docx, and html format are supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/documents.import",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "file": file,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
                    "template": template,
                },
                document_import_params.DocumentImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentImportResponse,
        )

    async def info(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        share_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentInfoResponse:
        """Retrieve a document

        Args:
          id: Unique identifier for the document.

        Either the UUID or the urlId is acceptable.

          share_id: Unique identifier for a document share, a shareId may be used in place of a
              document UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.info",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "share_id": share_id,
                },
                document_info_params.DocumentInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentInfoResponse,
        )

    async def move(
        self,
        *,
        id: str,
        collection_id: str | NotGiven = NOT_GIVEN,
        parent_document_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentMoveResponse:
        """Move a document to a new location or collection.

        If no parent document is
        provided, the document will be moved to the collection root.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.move",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "collection_id": collection_id,
                    "parent_document_id": parent_document_id,
                },
                document_move_params.DocumentMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentMoveResponse,
        )

    async def restore(
        self,
        *,
        id: str,
        revision_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentRestoreResponse:
        """If a document has been archived or deleted, it can be restored.

        Optionally a
        revision can be passed to restore the document to a previous point in time.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          revision_id: Identifier for the revision to restore to.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.restore",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "revision_id": revision_id,
                },
                document_restore_params.DocumentRestoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentRestoreResponse,
        )

    async def search(
        self,
        *,
        collection_id: str | NotGiven = NOT_GIVEN,
        date_filter: Literal["day", "week", "month", "year"] | NotGiven = NOT_GIVEN,
        document_id: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        offset: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        status_filter: Literal["draft", "archived", "published"] | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentSearchResponse:
        """This methods allows you to search your teams documents with keywords.

        Note that
        search results will be restricted to those accessible by the current access
        token.

        Args:
          collection_id: A collection to search within

          date_filter: Any documents that have not been updated within the specified period will be
              filtered out

          document_id: A document to search within

          status_filter: Any documents that are not in the specified status will be filtered out

          user_id: Any documents that have not been edited by the user identifier will be filtered
              out

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.search",
            body=await async_maybe_transform(
                {
                    "collection_id": collection_id,
                    "date_filter": date_filter,
                    "document_id": document_id,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "status_filter": status_filter,
                    "user_id": user_id,
                },
                document_search_params.DocumentSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentSearchResponse,
        )

    async def star(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentStarResponse:
        """
        Starring a document gives it extra priority in the UI and makes it easier to
        find important information later.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.star",
            body=await async_maybe_transform({"id": id}, document_star_params.DocumentStarParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentStarResponse,
        )

    async def templatize(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentTemplatizeResponse:
        """
        This method allows you to createa new template using an existing document as the
        basis

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.templatize",
            body=await async_maybe_transform({"id": id}, document_templatize_params.DocumentTemplatizeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentTemplatizeResponse,
        )

    async def unpublish(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUnpublishResponse:
        """
        Unpublishing a document moves it back to a draft status and out of the
        collection.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.unpublish",
            body=await async_maybe_transform({"id": id}, document_unpublish_params.DocumentUnpublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUnpublishResponse,
        )

    async def unstar(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUnstarResponse:
        """
        Starring a document gives it extra priority in the UI and makes it easier to
        find important information later.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.unstar",
            body=await async_maybe_transform({"id": id}, document_unstar_params.DocumentUnstarParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUnstarResponse,
        )

    async def viewed(
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
    ) -> DocumentViewedResponse:
        """
        This method will list all documents recently viewed by the current user.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.viewed",
            body=await async_maybe_transform(
                {
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                document_viewed_params.DocumentViewedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentViewedResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_raw_response_wrapper(
            documents.create,
        )
        self.update = to_raw_response_wrapper(
            documents.update,
        )
        self.list = to_raw_response_wrapper(
            documents.list,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )
        self.archive = to_raw_response_wrapper(
            documents.archive,
        )
        self.drafts = to_raw_response_wrapper(
            documents.drafts,
        )
        self.export = to_raw_response_wrapper(
            documents.export,
        )
        self.import_ = to_raw_response_wrapper(
            documents.import_,
        )
        self.info = to_raw_response_wrapper(
            documents.info,
        )
        self.move = to_raw_response_wrapper(
            documents.move,
        )
        self.restore = to_raw_response_wrapper(
            documents.restore,
        )
        self.search = to_raw_response_wrapper(
            documents.search,
        )
        self.star = to_raw_response_wrapper(
            documents.star,
        )
        self.templatize = to_raw_response_wrapper(
            documents.templatize,
        )
        self.unpublish = to_raw_response_wrapper(
            documents.unpublish,
        )
        self.unstar = to_raw_response_wrapper(
            documents.unstar,
        )
        self.viewed = to_raw_response_wrapper(
            documents.viewed,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_raw_response_wrapper(
            documents.create,
        )
        self.update = async_to_raw_response_wrapper(
            documents.update,
        )
        self.list = async_to_raw_response_wrapper(
            documents.list,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )
        self.archive = async_to_raw_response_wrapper(
            documents.archive,
        )
        self.drafts = async_to_raw_response_wrapper(
            documents.drafts,
        )
        self.export = async_to_raw_response_wrapper(
            documents.export,
        )
        self.import_ = async_to_raw_response_wrapper(
            documents.import_,
        )
        self.info = async_to_raw_response_wrapper(
            documents.info,
        )
        self.move = async_to_raw_response_wrapper(
            documents.move,
        )
        self.restore = async_to_raw_response_wrapper(
            documents.restore,
        )
        self.search = async_to_raw_response_wrapper(
            documents.search,
        )
        self.star = async_to_raw_response_wrapper(
            documents.star,
        )
        self.templatize = async_to_raw_response_wrapper(
            documents.templatize,
        )
        self.unpublish = async_to_raw_response_wrapper(
            documents.unpublish,
        )
        self.unstar = async_to_raw_response_wrapper(
            documents.unstar,
        )
        self.viewed = async_to_raw_response_wrapper(
            documents.viewed,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = to_streamed_response_wrapper(
            documents.create,
        )
        self.update = to_streamed_response_wrapper(
            documents.update,
        )
        self.list = to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )
        self.archive = to_streamed_response_wrapper(
            documents.archive,
        )
        self.drafts = to_streamed_response_wrapper(
            documents.drafts,
        )
        self.export = to_streamed_response_wrapper(
            documents.export,
        )
        self.import_ = to_streamed_response_wrapper(
            documents.import_,
        )
        self.info = to_streamed_response_wrapper(
            documents.info,
        )
        self.move = to_streamed_response_wrapper(
            documents.move,
        )
        self.restore = to_streamed_response_wrapper(
            documents.restore,
        )
        self.search = to_streamed_response_wrapper(
            documents.search,
        )
        self.star = to_streamed_response_wrapper(
            documents.star,
        )
        self.templatize = to_streamed_response_wrapper(
            documents.templatize,
        )
        self.unpublish = to_streamed_response_wrapper(
            documents.unpublish,
        )
        self.unstar = to_streamed_response_wrapper(
            documents.unstar,
        )
        self.viewed = to_streamed_response_wrapper(
            documents.viewed,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = async_to_streamed_response_wrapper(
            documents.create,
        )
        self.update = async_to_streamed_response_wrapper(
            documents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            documents.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )
        self.archive = async_to_streamed_response_wrapper(
            documents.archive,
        )
        self.drafts = async_to_streamed_response_wrapper(
            documents.drafts,
        )
        self.export = async_to_streamed_response_wrapper(
            documents.export,
        )
        self.import_ = async_to_streamed_response_wrapper(
            documents.import_,
        )
        self.info = async_to_streamed_response_wrapper(
            documents.info,
        )
        self.move = async_to_streamed_response_wrapper(
            documents.move,
        )
        self.restore = async_to_streamed_response_wrapper(
            documents.restore,
        )
        self.search = async_to_streamed_response_wrapper(
            documents.search,
        )
        self.star = async_to_streamed_response_wrapper(
            documents.star,
        )
        self.templatize = async_to_streamed_response_wrapper(
            documents.templatize,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            documents.unpublish,
        )
        self.unstar = async_to_streamed_response_wrapper(
            documents.unstar,
        )
        self.viewed = async_to_streamed_response_wrapper(
            documents.viewed,
        )
