# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    file_operation_info_params,
    file_operation_list_params,
    file_operation_delete_params,
    file_operation_redirect_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.file_operation_info_response import FileOperationInfoResponse
from ..types.file_operation_list_response import FileOperationListResponse
from ..types.file_operation_delete_response import FileOperationDeleteResponse

__all__ = ["FileOperationsResource", "AsyncFileOperationsResource"]


class FileOperationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileOperationsResourceWithRawResponse:
        return FileOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileOperationsResourceWithStreamingResponse:
        return FileOperationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        type: Literal["export", "import"],
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
    ) -> FileOperationListResponse:
        """
        List all file operations

        Args:
          type: The type of fileOperation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fileOperations.list",
            body=maybe_transform(
                {
                    "type": type,
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                file_operation_list_params.FileOperationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOperationListResponse,
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
    ) -> FileOperationDeleteResponse:
        """
        Delete a file operation

        Args:
          id: Unique identifier for the file operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fileOperations.delete",
            body=maybe_transform({"id": id}, file_operation_delete_params.FileOperationDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOperationDeleteResponse,
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
    ) -> FileOperationInfoResponse:
        """
        Retrieve a file operation

        Args:
          id: Unique identifier for the file operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/fileOperations.info",
            body=maybe_transform({"id": id}, file_operation_info_params.FileOperationInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOperationInfoResponse,
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
    ) -> BinaryAPIResponse:
        """Load the resulting file from where it is stored based on the id.

        A temporary,
        signed url with embedded credentials is generated on demand.

        Args:
          id: Unique identifier for the file operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/fileOperations.redirect",
            body=maybe_transform({"id": id}, file_operation_redirect_params.FileOperationRedirectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncFileOperationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileOperationsResourceWithRawResponse:
        return AsyncFileOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileOperationsResourceWithStreamingResponse:
        return AsyncFileOperationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        type: Literal["export", "import"],
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
    ) -> FileOperationListResponse:
        """
        List all file operations

        Args:
          type: The type of fileOperation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fileOperations.list",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "direction": direction,
                    "limit": limit,
                    "offset": offset,
                    "sort": sort,
                },
                file_operation_list_params.FileOperationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOperationListResponse,
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
    ) -> FileOperationDeleteResponse:
        """
        Delete a file operation

        Args:
          id: Unique identifier for the file operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fileOperations.delete",
            body=await async_maybe_transform({"id": id}, file_operation_delete_params.FileOperationDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOperationDeleteResponse,
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
    ) -> FileOperationInfoResponse:
        """
        Retrieve a file operation

        Args:
          id: Unique identifier for the file operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/fileOperations.info",
            body=await async_maybe_transform({"id": id}, file_operation_info_params.FileOperationInfoParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileOperationInfoResponse,
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
    ) -> AsyncBinaryAPIResponse:
        """Load the resulting file from where it is stored based on the id.

        A temporary,
        signed url with embedded credentials is generated on demand.

        Args:
          id: Unique identifier for the file operation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/fileOperations.redirect",
            body=await async_maybe_transform({"id": id}, file_operation_redirect_params.FileOperationRedirectParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class FileOperationsResourceWithRawResponse:
    def __init__(self, file_operations: FileOperationsResource) -> None:
        self._file_operations = file_operations

        self.list = to_raw_response_wrapper(
            file_operations.list,
        )
        self.delete = to_raw_response_wrapper(
            file_operations.delete,
        )
        self.info = to_raw_response_wrapper(
            file_operations.info,
        )
        self.redirect = to_custom_raw_response_wrapper(
            file_operations.redirect,
            BinaryAPIResponse,
        )


class AsyncFileOperationsResourceWithRawResponse:
    def __init__(self, file_operations: AsyncFileOperationsResource) -> None:
        self._file_operations = file_operations

        self.list = async_to_raw_response_wrapper(
            file_operations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            file_operations.delete,
        )
        self.info = async_to_raw_response_wrapper(
            file_operations.info,
        )
        self.redirect = async_to_custom_raw_response_wrapper(
            file_operations.redirect,
            AsyncBinaryAPIResponse,
        )


class FileOperationsResourceWithStreamingResponse:
    def __init__(self, file_operations: FileOperationsResource) -> None:
        self._file_operations = file_operations

        self.list = to_streamed_response_wrapper(
            file_operations.list,
        )
        self.delete = to_streamed_response_wrapper(
            file_operations.delete,
        )
        self.info = to_streamed_response_wrapper(
            file_operations.info,
        )
        self.redirect = to_custom_streamed_response_wrapper(
            file_operations.redirect,
            StreamedBinaryAPIResponse,
        )


class AsyncFileOperationsResourceWithStreamingResponse:
    def __init__(self, file_operations: AsyncFileOperationsResource) -> None:
        self._file_operations = file_operations

        self.list = async_to_streamed_response_wrapper(
            file_operations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            file_operations.delete,
        )
        self.info = async_to_streamed_response_wrapper(
            file_operations.info,
        )
        self.redirect = async_to_custom_streamed_response_wrapper(
            file_operations.redirect,
            AsyncStreamedBinaryAPIResponse,
        )
