# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    document_info_params,
    document_list_params,
    document_move_params,
    document_create_params,
    document_delete_params,
    document_drafts_params,
    document_export_params,
    document_import_params,
    document_search_params,
    document_update_params,
    document_viewed_params,
    document_archive_params,
    document_restore_params,
    document_unpublish_params,
    document_templatize_params,
)
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
from ..types.document_info_response import DocumentInfoResponse
from ..types.document_list_response import DocumentListResponse
from ..types.document_move_response import DocumentMoveResponse
from ..types.document_create_response import DocumentCreateResponse
from ..types.document_delete_response import DocumentDeleteResponse
from ..types.document_drafts_response import DocumentDraftsResponse
from ..types.document_export_response import DocumentExportResponse
from ..types.document_import_response import DocumentImportResponse
from ..types.document_search_response import DocumentSearchResponse
from ..types.document_update_response import DocumentUpdateResponse
from ..types.document_viewed_response import DocumentViewedResponse
from ..types.document_archive_response import DocumentArchiveResponse
from ..types.document_restore_response import DocumentRestoreResponse
from ..types.document_unpublish_response import DocumentUnpublishResponse
from ..types.document_templatize_response import DocumentTemplatizeResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    """`Documents` are what everything else revolves around.

    A document represents
    a single page of information and always returns the latest version of the
    content. Documents are stored in [Markdown](https://spec.commonmark.org/)
    formatting.
    """

    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str | Omit = omit,
        collection_id: Optional[str] | Omit = omit,
        color: Optional[str] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        data_attributes: Iterable[document_create_params.DataAttribute] | Omit = omit,
        full_width: bool | Omit = omit,
        icon: str | Omit = omit,
        parent_document_id: Optional[str] | Omit = omit,
        publish: bool | Omit = omit,
        template_id: str | Omit = omit,
        text: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """This method allows you to create or publish a new document.

        By default a
        document is set to the collection root. If you want to create a nested/child
        document, you should pass parentDocumentId to set the parent document.

        Args:
          id: Optional identifier for the document

          collection_id: Identifier for the collection. Required to publish unless parentDocumentId is
              provided

          color: Color for the document icon (hex format)

          created_at: Optionally set the created date in the past

          data_attributes: Data attributes to be included on the document.

          full_width: Whether the document should be displayed in full width

          icon: Icon displayed alongside the document title

          parent_document_id: Identifier for the parent document. Required to publish unless collectionId is
              provided

          publish: Whether this document should be immediately published and made visible to other
              workspace members.

          text: The body of the document in markdown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.create",
            body=maybe_transform(
                {
                    "id": id,
                    "collection_id": collection_id,
                    "color": color,
                    "created_at": created_at,
                    "data_attributes": data_attributes,
                    "full_width": full_width,
                    "icon": icon,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
                    "template_id": template_id,
                    "text": text,
                    "title": title,
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
        collection_id: Optional[str] | Omit = omit,
        color: Optional[str] | Omit = omit,
        data_attributes: Optional[Iterable[document_update_params.DataAttribute]] | Omit = omit,
        edit_mode: Literal["append", "prepend", "replace", "patch"] | Omit = omit,
        find_text: str | Omit = omit,
        full_width: bool | Omit = omit,
        icon: Optional[str] | Omit = omit,
        insights_enabled: bool | Omit = omit,
        publish: bool | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        text: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        This method allows you to modify an already created document

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          collection_id: Identifier for the collection to move the document to

          color: Color for the document icon (hex format)

          data_attributes: Data attributes to be updated. Attributes not included will be removed from the
              document.

          edit_mode: The editing mode for text updates to a document. When set to `patch`, the
              `findText` parameter is required and the existing occurrence of `findText` will
              be replaced with the value of `text`.

          find_text: The text to find within the document when using `patch` editMode. This text will
              be replaced with the value of `text`. Required when `editMode` is `patch`.

          full_width: Whether the document should be displayed in full width

          icon: Icon displayed alongside the document title

          insights_enabled: Whether insights should be visible on the document

          publish: Whether this document should be published and made visible to other workspace
              members, if a draft

          template_id: Identifier for the template this document is based on

          text: The body of the document in markdown.

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
                    "collection_id": collection_id,
                    "color": color,
                    "data_attributes": data_attributes,
                    "edit_mode": edit_mode,
                    "find_text": find_text,
                    "full_width": full_width,
                    "icon": icon,
                    "insights_enabled": insights_enabled,
                    "publish": publish,
                    "template_id": template_id,
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
        backlink_document_id: str | Omit = omit,
        collection_id: str | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        parent_document_id: str | Omit = omit,
        sort: str | Omit = omit,
        status_filter: List[Literal["draft", "archived", "published"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentListResponse:
        """
        This method will list all published documents and draft documents belonging to
        the current user.

        Args:
          collection_id: Optionally filter to a specific collection

          status_filter: Document statuses to include in results

          user_id: Optionally filter to documents created by a specific user

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
                    "status_filter": status_filter,
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
        permanent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentDeleteResponse:
        """Deleting a document moves it to the trash.

        If not restored within 30 days it is
        permanently deleted.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        collection_id: str | Omit = omit,
        date_filter: Literal["day", "week", "month", "year"] | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        id: str,
        include_child_documents: bool | Omit = omit,
        paper_size: str | Omit = omit,
        signed_urls: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentExportResponse:
        """Export a document in Markdown, HTML, PDF, or TextBundle format.

        The response
        format is determined by the Accept header (`text/markdown`, `text/html`,
        `application/pdf`, or `application/x-textbundle`). Optionally include child
        documents in the export as a zip file.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          include_child_documents: Whether to include child documents in the export. Using this option will always
              return a zip file.

          paper_size: Paper size for PDF export (e.g., "A4", "Letter")

          signed_urls: How long signed URLs should remain valid for attachment links (in seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.export",
            body=maybe_transform(
                {
                    "id": id,
                    "include_child_documents": include_child_documents,
                    "paper_size": paper_size,
                    "signed_urls": signed_urls,
                },
                document_export_params.DocumentExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentExportResponse,
        )

    def import_(
        self,
        *,
        file: object,
        collection_id: Optional[str] | Omit = omit,
        parent_document_id: Optional[str] | Omit = omit,
        publish: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentImportResponse:
        """
        This method allows you to create a new document by importing an existing file.
        By default a document is set to the collection root. If you want to create a
        nested/child document, you should pass parentDocumentId to set the parent
        document.

        Args:
          file: Plain text, markdown, docx, csv, tsv, html, mhtml (or mht) web pages, eml email
              messages, and textbundle/textpack bundles are supported.

          collection_id: Identifier for the collection to import into. One of collectionId or
              parentDocumentId is required.

          parent_document_id: Identifier for the parent document to import under. One of collectionId or
              parentDocumentId is required.

          publish: Whether to publish the imported document

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
                    "file": file,
                    "collection_id": collection_id,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
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
        id: str | Omit = omit,
        share_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentInfoResponse:
        """Retrieve a document by its `UUID`, `urlId`, or `shareId`.

        At least one of these
        parameters must be provided.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

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
        collection_id: str | Omit = omit,
        index: float | Omit = omit,
        parent_document_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentMoveResponse:
        """Move a document to a new location or collection.

        If no parent document is
        provided, the document will be moved to the collection root.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          index: The position index in the collection structure

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
                    "index": index,
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
        collection_id: str | Omit = omit,
        revision_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRestoreResponse:
        """If a document has been archived or deleted, it can be restored.

        Optionally a
        revision can be passed to restore the document to a previous point in time.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          collection_id: Identifier for the collection to restore the document to.

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
                    "collection_id": collection_id,
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
        collection_id: str | Omit = omit,
        date_filter: Literal["day", "week", "month", "year"] | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        document_id: str | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        query: str | Omit = omit,
        share_id: str | Omit = omit,
        snippet_max_words: float | Omit = omit,
        snippet_min_words: float | Omit = omit,
        sort: Literal["relevance", "createdAt", "updatedAt", "title"] | Omit = omit,
        status_filter: List[Literal["draft", "archived", "published"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentSearchResponse:
        """This methods allows you to search your workspace's documents with keywords.

        Note
        that search results will be restricted to those accessible by the current access
        token.

        Args:
          collection_id: A collection to search within

          date_filter: Any documents that have not been updated within the specified period will be
              filtered out

          direction: Specifies the sort order with respect to sort field

          document_id: A document to search within

          share_id: Filter results to the collection or document referenced by the shareId

          snippet_max_words: Maximum number of words to show in search result snippets

          snippet_min_words: Minimum number of words to show in search result snippets

          sort: Specifies the attributes by which search results will be sorted

          status_filter: Document statuses to include in results

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
                    "direction": direction,
                    "document_id": document_id,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "share_id": share_id,
                    "snippet_max_words": snippet_max_words,
                    "snippet_min_words": snippet_min_words,
                    "sort": sort,
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

    def templatize(
        self,
        *,
        id: str,
        publish: bool,
        collection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentTemplatizeResponse:
        """
        This method allows you to create a new template using an existing document as
        the basis

        Args:
          publish: Whether the new template should be published

          collection_id: Identifier for the collection where the template should be created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.templatize",
            body=maybe_transform(
                {
                    "id": id,
                    "publish": publish,
                    "collection_id": collection_id,
                },
                document_templatize_params.DocumentTemplatizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentTemplatizeResponse,
        )

    def unpublish(
        self,
        *,
        id: str,
        detach: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUnpublishResponse:
        """
        Unpublishing a document moves it back to a draft status and out of the
        collection.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          detach: Whether to detach the document from the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents.unpublish",
            body=maybe_transform(
                {
                    "id": id,
                    "detach": detach,
                },
                document_unpublish_params.DocumentUnpublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUnpublishResponse,
        )

    def viewed(
        self,
        *,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
    """`Documents` are what everything else revolves around.

    A document represents
    a single page of information and always returns the latest version of the
    content. Documents are stored in [Markdown](https://spec.commonmark.org/)
    formatting.
    """

    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Yoshino-s/outline-python-api#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str | Omit = omit,
        collection_id: Optional[str] | Omit = omit,
        color: Optional[str] | Omit = omit,
        created_at: Union[str, datetime] | Omit = omit,
        data_attributes: Iterable[document_create_params.DataAttribute] | Omit = omit,
        full_width: bool | Omit = omit,
        icon: str | Omit = omit,
        parent_document_id: Optional[str] | Omit = omit,
        publish: bool | Omit = omit,
        template_id: str | Omit = omit,
        text: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """This method allows you to create or publish a new document.

        By default a
        document is set to the collection root. If you want to create a nested/child
        document, you should pass parentDocumentId to set the parent document.

        Args:
          id: Optional identifier for the document

          collection_id: Identifier for the collection. Required to publish unless parentDocumentId is
              provided

          color: Color for the document icon (hex format)

          created_at: Optionally set the created date in the past

          data_attributes: Data attributes to be included on the document.

          full_width: Whether the document should be displayed in full width

          icon: Icon displayed alongside the document title

          parent_document_id: Identifier for the parent document. Required to publish unless collectionId is
              provided

          publish: Whether this document should be immediately published and made visible to other
              workspace members.

          text: The body of the document in markdown

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.create",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "collection_id": collection_id,
                    "color": color,
                    "created_at": created_at,
                    "data_attributes": data_attributes,
                    "full_width": full_width,
                    "icon": icon,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
                    "template_id": template_id,
                    "text": text,
                    "title": title,
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
        collection_id: Optional[str] | Omit = omit,
        color: Optional[str] | Omit = omit,
        data_attributes: Optional[Iterable[document_update_params.DataAttribute]] | Omit = omit,
        edit_mode: Literal["append", "prepend", "replace", "patch"] | Omit = omit,
        find_text: str | Omit = omit,
        full_width: bool | Omit = omit,
        icon: Optional[str] | Omit = omit,
        insights_enabled: bool | Omit = omit,
        publish: bool | Omit = omit,
        template_id: Optional[str] | Omit = omit,
        text: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        This method allows you to modify an already created document

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          collection_id: Identifier for the collection to move the document to

          color: Color for the document icon (hex format)

          data_attributes: Data attributes to be updated. Attributes not included will be removed from the
              document.

          edit_mode: The editing mode for text updates to a document. When set to `patch`, the
              `findText` parameter is required and the existing occurrence of `findText` will
              be replaced with the value of `text`.

          find_text: The text to find within the document when using `patch` editMode. This text will
              be replaced with the value of `text`. Required when `editMode` is `patch`.

          full_width: Whether the document should be displayed in full width

          icon: Icon displayed alongside the document title

          insights_enabled: Whether insights should be visible on the document

          publish: Whether this document should be published and made visible to other workspace
              members, if a draft

          template_id: Identifier for the template this document is based on

          text: The body of the document in markdown.

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
                    "collection_id": collection_id,
                    "color": color,
                    "data_attributes": data_attributes,
                    "edit_mode": edit_mode,
                    "find_text": find_text,
                    "full_width": full_width,
                    "icon": icon,
                    "insights_enabled": insights_enabled,
                    "publish": publish,
                    "template_id": template_id,
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
        backlink_document_id: str | Omit = omit,
        collection_id: str | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        parent_document_id: str | Omit = omit,
        sort: str | Omit = omit,
        status_filter: List[Literal["draft", "archived", "published"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentListResponse:
        """
        This method will list all published documents and draft documents belonging to
        the current user.

        Args:
          collection_id: Optionally filter to a specific collection

          status_filter: Document statuses to include in results

          user_id: Optionally filter to documents created by a specific user

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
                    "status_filter": status_filter,
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
        permanent: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentDeleteResponse:
        """Deleting a document moves it to the trash.

        If not restored within 30 days it is
        permanently deleted.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        collection_id: str | Omit = omit,
        date_filter: Literal["day", "week", "month", "year"] | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        id: str,
        include_child_documents: bool | Omit = omit,
        paper_size: str | Omit = omit,
        signed_urls: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentExportResponse:
        """Export a document in Markdown, HTML, PDF, or TextBundle format.

        The response
        format is determined by the Accept header (`text/markdown`, `text/html`,
        `application/pdf`, or `application/x-textbundle`). Optionally include child
        documents in the export as a zip file.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          include_child_documents: Whether to include child documents in the export. Using this option will always
              return a zip file.

          paper_size: Paper size for PDF export (e.g., "A4", "Letter")

          signed_urls: How long signed URLs should remain valid for attachment links (in seconds)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.export",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "include_child_documents": include_child_documents,
                    "paper_size": paper_size,
                    "signed_urls": signed_urls,
                },
                document_export_params.DocumentExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentExportResponse,
        )

    async def import_(
        self,
        *,
        file: object,
        collection_id: Optional[str] | Omit = omit,
        parent_document_id: Optional[str] | Omit = omit,
        publish: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentImportResponse:
        """
        This method allows you to create a new document by importing an existing file.
        By default a document is set to the collection root. If you want to create a
        nested/child document, you should pass parentDocumentId to set the parent
        document.

        Args:
          file: Plain text, markdown, docx, csv, tsv, html, mhtml (or mht) web pages, eml email
              messages, and textbundle/textpack bundles are supported.

          collection_id: Identifier for the collection to import into. One of collectionId or
              parentDocumentId is required.

          parent_document_id: Identifier for the parent document to import under. One of collectionId or
              parentDocumentId is required.

          publish: Whether to publish the imported document

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
                    "file": file,
                    "collection_id": collection_id,
                    "parent_document_id": parent_document_id,
                    "publish": publish,
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
        id: str | Omit = omit,
        share_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentInfoResponse:
        """Retrieve a document by its `UUID`, `urlId`, or `shareId`.

        At least one of these
        parameters must be provided.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

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
        collection_id: str | Omit = omit,
        index: float | Omit = omit,
        parent_document_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentMoveResponse:
        """Move a document to a new location or collection.

        If no parent document is
        provided, the document will be moved to the collection root.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          index: The position index in the collection structure

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
                    "index": index,
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
        collection_id: str | Omit = omit,
        revision_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRestoreResponse:
        """If a document has been archived or deleted, it can be restored.

        Optionally a
        revision can be passed to restore the document to a previous point in time.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          collection_id: Identifier for the collection to restore the document to.

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
                    "collection_id": collection_id,
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
        collection_id: str | Omit = omit,
        date_filter: Literal["day", "week", "month", "year"] | Omit = omit,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        document_id: str | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        query: str | Omit = omit,
        share_id: str | Omit = omit,
        snippet_max_words: float | Omit = omit,
        snippet_min_words: float | Omit = omit,
        sort: Literal["relevance", "createdAt", "updatedAt", "title"] | Omit = omit,
        status_filter: List[Literal["draft", "archived", "published"]] | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentSearchResponse:
        """This methods allows you to search your workspace's documents with keywords.

        Note
        that search results will be restricted to those accessible by the current access
        token.

        Args:
          collection_id: A collection to search within

          date_filter: Any documents that have not been updated within the specified period will be
              filtered out

          direction: Specifies the sort order with respect to sort field

          document_id: A document to search within

          share_id: Filter results to the collection or document referenced by the shareId

          snippet_max_words: Maximum number of words to show in search result snippets

          snippet_min_words: Minimum number of words to show in search result snippets

          sort: Specifies the attributes by which search results will be sorted

          status_filter: Document statuses to include in results

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
                    "direction": direction,
                    "document_id": document_id,
                    "limit": limit,
                    "offset": offset,
                    "query": query,
                    "share_id": share_id,
                    "snippet_max_words": snippet_max_words,
                    "snippet_min_words": snippet_min_words,
                    "sort": sort,
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

    async def templatize(
        self,
        *,
        id: str,
        publish: bool,
        collection_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentTemplatizeResponse:
        """
        This method allows you to create a new template using an existing document as
        the basis

        Args:
          publish: Whether the new template should be published

          collection_id: Identifier for the collection where the template should be created

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.templatize",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "publish": publish,
                    "collection_id": collection_id,
                },
                document_templatize_params.DocumentTemplatizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentTemplatizeResponse,
        )

    async def unpublish(
        self,
        *,
        id: str,
        detach: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUnpublishResponse:
        """
        Unpublishing a document moves it back to a draft status and out of the
        collection.

        Args:
          id: Unique identifier for the document. Either the UUID or the urlId is acceptable.

          detach: Whether to detach the document from the collection

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents.unpublish",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "detach": detach,
                },
                document_unpublish_params.DocumentUnpublishParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUnpublishResponse,
        )

    async def viewed(
        self,
        *,
        direction: Literal["ASC", "DESC"] | Omit = omit,
        limit: float | Omit = omit,
        offset: float | Omit = omit,
        sort: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        self.templatize = to_raw_response_wrapper(
            documents.templatize,
        )
        self.unpublish = to_raw_response_wrapper(
            documents.unpublish,
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
        self.templatize = async_to_raw_response_wrapper(
            documents.templatize,
        )
        self.unpublish = async_to_raw_response_wrapper(
            documents.unpublish,
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
        self.templatize = to_streamed_response_wrapper(
            documents.templatize,
        )
        self.unpublish = to_streamed_response_wrapper(
            documents.unpublish,
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
        self.templatize = async_to_streamed_response_wrapper(
            documents.templatize,
        )
        self.unpublish = async_to_streamed_response_wrapper(
            documents.unpublish,
        )
        self.viewed = async_to_streamed_response_wrapper(
            documents.viewed,
        )
