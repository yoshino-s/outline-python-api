# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import OutlineError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import auth, events, groups, comments, documents, attachments, collections, file_operations
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.events import EventsResource, AsyncEventsResource
    from .resources.groups import GroupsResource, AsyncGroupsResource
    from .resources.comments import CommentsResource, AsyncCommentsResource
    from .resources.documents import DocumentsResource, AsyncDocumentsResource
    from .resources.attachments import AttachmentsResource, AsyncAttachmentsResource
    from .resources.file_operations import FileOperationsResource, AsyncFileOperationsResource
    from .resources.collections.collections import CollectionsResource, AsyncCollectionsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Outline", "AsyncOutline", "Client", "AsyncClient"]


class Outline(SyncAPIClient):
    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Outline client instance.

        This automatically infers the `bearer_token` argument from the `OUTLINE_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("OUTLINE_BEARER_TOKEN")
        if bearer_token is None:
            raise OutlineError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the OUTLINE_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("OUTLINE_BASE_URL")
        if base_url is None:
            base_url = f"https://app.getoutline.com/api"

        custom_headers_env = os.environ.get("OUTLINE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def attachments(self) -> AttachmentsResource:
        """`Attachments` represent a file uploaded to cloud storage.

        They are created
        before the upload happens from the client and store all the meta information
        such as file type, size, and location.
        """
        from .resources.attachments import AttachmentsResource

        return AttachmentsResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        """`Auth` represents the current API Keys authentication details.

        It can be
        used to check that a token is still valid and load the IDs for the current
        user and workspace.
        """
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def collections(self) -> CollectionsResource:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        from .resources.collections import CollectionsResource

        return CollectionsResource(self)

    @cached_property
    def comments(self) -> CommentsResource:
        """
        `Comments` represent a comment either on a selection of text in a document
        or on the document itself.
        """
        from .resources.comments import CommentsResource

        return CommentsResource(self)

    @cached_property
    def documents(self) -> DocumentsResource:
        """`Documents` are what everything else revolves around.

        A document represents
        a single page of information and always returns the latest version of the
        content. Documents are stored in [Markdown](https://spec.commonmark.org/)
        formatting.
        """
        from .resources.documents import DocumentsResource

        return DocumentsResource(self)

    @cached_property
    def events(self) -> EventsResource:
        """`Events` represent an artifact of an action.

        Whether it is creating a user,
        editing a document, changing permissions, or any other action – an event
        is created that can be used as an audit trail or activity stream.
        """
        from .resources.events import EventsResource

        return EventsResource(self)

    @cached_property
    def file_operations(self) -> FileOperationsResource:
        """
        `FileOperations` represent background jobs for importing or exporting files.
        You can query the file operation to find the state of progress and any
        resulting output.
        """
        from .resources.file_operations import FileOperationsResource

        return FileOperationsResource(self)

    @cached_property
    def groups(self) -> GroupsResource:
        """
        `Groups` represent a list of users that logically belong together, for
        example there might be groups for each department in your organization.
        Groups can be granted access to collections with read or write permissions.
        """
        from .resources.groups import GroupsResource

        return GroupsResource(self)

    @cached_property
    def with_raw_response(self) -> OutlineWithRawResponse:
        return OutlineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OutlineWithStreamedResponse:
        return OutlineWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOutline(AsyncAPIClient):
    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOutline client instance.

        This automatically infers the `bearer_token` argument from the `OUTLINE_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("OUTLINE_BEARER_TOKEN")
        if bearer_token is None:
            raise OutlineError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the OUTLINE_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("OUTLINE_BASE_URL")
        if base_url is None:
            base_url = f"https://app.getoutline.com/api"

        custom_headers_env = os.environ.get("OUTLINE_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def attachments(self) -> AsyncAttachmentsResource:
        """`Attachments` represent a file uploaded to cloud storage.

        They are created
        before the upload happens from the client and store all the meta information
        such as file type, size, and location.
        """
        from .resources.attachments import AsyncAttachmentsResource

        return AsyncAttachmentsResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """`Auth` represents the current API Keys authentication details.

        It can be
        used to check that a token is still valid and load the IDs for the current
        user and workspace.
        """
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def collections(self) -> AsyncCollectionsResource:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        from .resources.collections import AsyncCollectionsResource

        return AsyncCollectionsResource(self)

    @cached_property
    def comments(self) -> AsyncCommentsResource:
        """
        `Comments` represent a comment either on a selection of text in a document
        or on the document itself.
        """
        from .resources.comments import AsyncCommentsResource

        return AsyncCommentsResource(self)

    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        """`Documents` are what everything else revolves around.

        A document represents
        a single page of information and always returns the latest version of the
        content. Documents are stored in [Markdown](https://spec.commonmark.org/)
        formatting.
        """
        from .resources.documents import AsyncDocumentsResource

        return AsyncDocumentsResource(self)

    @cached_property
    def events(self) -> AsyncEventsResource:
        """`Events` represent an artifact of an action.

        Whether it is creating a user,
        editing a document, changing permissions, or any other action – an event
        is created that can be used as an audit trail or activity stream.
        """
        from .resources.events import AsyncEventsResource

        return AsyncEventsResource(self)

    @cached_property
    def file_operations(self) -> AsyncFileOperationsResource:
        """
        `FileOperations` represent background jobs for importing or exporting files.
        You can query the file operation to find the state of progress and any
        resulting output.
        """
        from .resources.file_operations import AsyncFileOperationsResource

        return AsyncFileOperationsResource(self)

    @cached_property
    def groups(self) -> AsyncGroupsResource:
        """
        `Groups` represent a list of users that logically belong together, for
        example there might be groups for each department in your organization.
        Groups can be granted access to collections with read or write permissions.
        """
        from .resources.groups import AsyncGroupsResource

        return AsyncGroupsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOutlineWithRawResponse:
        return AsyncOutlineWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOutlineWithStreamedResponse:
        return AsyncOutlineWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OutlineWithRawResponse:
    _client: Outline

    def __init__(self, client: Outline) -> None:
        self._client = client

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithRawResponse:
        """`Attachments` represent a file uploaded to cloud storage.

        They are created
        before the upload happens from the client and store all the meta information
        such as file type, size, and location.
        """
        from .resources.attachments import AttachmentsResourceWithRawResponse

        return AttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        """`Auth` represents the current API Keys authentication details.

        It can be
        used to check that a token is still valid and load the IDs for the current
        user and workspace.
        """
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithRawResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        from .resources.collections import CollectionsResourceWithRawResponse

        return CollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def comments(self) -> comments.CommentsResourceWithRawResponse:
        """
        `Comments` represent a comment either on a selection of text in a document
        or on the document itself.
        """
        from .resources.comments import CommentsResourceWithRawResponse

        return CommentsResourceWithRawResponse(self._client.comments)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithRawResponse:
        """`Documents` are what everything else revolves around.

        A document represents
        a single page of information and always returns the latest version of the
        content. Documents are stored in [Markdown](https://spec.commonmark.org/)
        formatting.
        """
        from .resources.documents import DocumentsResourceWithRawResponse

        return DocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def events(self) -> events.EventsResourceWithRawResponse:
        """`Events` represent an artifact of an action.

        Whether it is creating a user,
        editing a document, changing permissions, or any other action – an event
        is created that can be used as an audit trail or activity stream.
        """
        from .resources.events import EventsResourceWithRawResponse

        return EventsResourceWithRawResponse(self._client.events)

    @cached_property
    def file_operations(self) -> file_operations.FileOperationsResourceWithRawResponse:
        """
        `FileOperations` represent background jobs for importing or exporting files.
        You can query the file operation to find the state of progress and any
        resulting output.
        """
        from .resources.file_operations import FileOperationsResourceWithRawResponse

        return FileOperationsResourceWithRawResponse(self._client.file_operations)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithRawResponse:
        """
        `Groups` represent a list of users that logically belong together, for
        example there might be groups for each department in your organization.
        Groups can be granted access to collections with read or write permissions.
        """
        from .resources.groups import GroupsResourceWithRawResponse

        return GroupsResourceWithRawResponse(self._client.groups)


class AsyncOutlineWithRawResponse:
    _client: AsyncOutline

    def __init__(self, client: AsyncOutline) -> None:
        self._client = client

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithRawResponse:
        """`Attachments` represent a file uploaded to cloud storage.

        They are created
        before the upload happens from the client and store all the meta information
        such as file type, size, and location.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithRawResponse

        return AsyncAttachmentsResourceWithRawResponse(self._client.attachments)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        """`Auth` represents the current API Keys authentication details.

        It can be
        used to check that a token is still valid and load the IDs for the current
        user and workspace.
        """
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithRawResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        from .resources.collections import AsyncCollectionsResourceWithRawResponse

        return AsyncCollectionsResourceWithRawResponse(self._client.collections)

    @cached_property
    def comments(self) -> comments.AsyncCommentsResourceWithRawResponse:
        """
        `Comments` represent a comment either on a selection of text in a document
        or on the document itself.
        """
        from .resources.comments import AsyncCommentsResourceWithRawResponse

        return AsyncCommentsResourceWithRawResponse(self._client.comments)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithRawResponse:
        """`Documents` are what everything else revolves around.

        A document represents
        a single page of information and always returns the latest version of the
        content. Documents are stored in [Markdown](https://spec.commonmark.org/)
        formatting.
        """
        from .resources.documents import AsyncDocumentsResourceWithRawResponse

        return AsyncDocumentsResourceWithRawResponse(self._client.documents)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithRawResponse:
        """`Events` represent an artifact of an action.

        Whether it is creating a user,
        editing a document, changing permissions, or any other action – an event
        is created that can be used as an audit trail or activity stream.
        """
        from .resources.events import AsyncEventsResourceWithRawResponse

        return AsyncEventsResourceWithRawResponse(self._client.events)

    @cached_property
    def file_operations(self) -> file_operations.AsyncFileOperationsResourceWithRawResponse:
        """
        `FileOperations` represent background jobs for importing or exporting files.
        You can query the file operation to find the state of progress and any
        resulting output.
        """
        from .resources.file_operations import AsyncFileOperationsResourceWithRawResponse

        return AsyncFileOperationsResourceWithRawResponse(self._client.file_operations)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithRawResponse:
        """
        `Groups` represent a list of users that logically belong together, for
        example there might be groups for each department in your organization.
        Groups can be granted access to collections with read or write permissions.
        """
        from .resources.groups import AsyncGroupsResourceWithRawResponse

        return AsyncGroupsResourceWithRawResponse(self._client.groups)


class OutlineWithStreamedResponse:
    _client: Outline

    def __init__(self, client: Outline) -> None:
        self._client = client

    @cached_property
    def attachments(self) -> attachments.AttachmentsResourceWithStreamingResponse:
        """`Attachments` represent a file uploaded to cloud storage.

        They are created
        before the upload happens from the client and store all the meta information
        such as file type, size, and location.
        """
        from .resources.attachments import AttachmentsResourceWithStreamingResponse

        return AttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        """`Auth` represents the current API Keys authentication details.

        It can be
        used to check that a token is still valid and load the IDs for the current
        user and workspace.
        """
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def collections(self) -> collections.CollectionsResourceWithStreamingResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        from .resources.collections import CollectionsResourceWithStreamingResponse

        return CollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def comments(self) -> comments.CommentsResourceWithStreamingResponse:
        """
        `Comments` represent a comment either on a selection of text in a document
        or on the document itself.
        """
        from .resources.comments import CommentsResourceWithStreamingResponse

        return CommentsResourceWithStreamingResponse(self._client.comments)

    @cached_property
    def documents(self) -> documents.DocumentsResourceWithStreamingResponse:
        """`Documents` are what everything else revolves around.

        A document represents
        a single page of information and always returns the latest version of the
        content. Documents are stored in [Markdown](https://spec.commonmark.org/)
        formatting.
        """
        from .resources.documents import DocumentsResourceWithStreamingResponse

        return DocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def events(self) -> events.EventsResourceWithStreamingResponse:
        """`Events` represent an artifact of an action.

        Whether it is creating a user,
        editing a document, changing permissions, or any other action – an event
        is created that can be used as an audit trail or activity stream.
        """
        from .resources.events import EventsResourceWithStreamingResponse

        return EventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def file_operations(self) -> file_operations.FileOperationsResourceWithStreamingResponse:
        """
        `FileOperations` represent background jobs for importing or exporting files.
        You can query the file operation to find the state of progress and any
        resulting output.
        """
        from .resources.file_operations import FileOperationsResourceWithStreamingResponse

        return FileOperationsResourceWithStreamingResponse(self._client.file_operations)

    @cached_property
    def groups(self) -> groups.GroupsResourceWithStreamingResponse:
        """
        `Groups` represent a list of users that logically belong together, for
        example there might be groups for each department in your organization.
        Groups can be granted access to collections with read or write permissions.
        """
        from .resources.groups import GroupsResourceWithStreamingResponse

        return GroupsResourceWithStreamingResponse(self._client.groups)


class AsyncOutlineWithStreamedResponse:
    _client: AsyncOutline

    def __init__(self, client: AsyncOutline) -> None:
        self._client = client

    @cached_property
    def attachments(self) -> attachments.AsyncAttachmentsResourceWithStreamingResponse:
        """`Attachments` represent a file uploaded to cloud storage.

        They are created
        before the upload happens from the client and store all the meta information
        such as file type, size, and location.
        """
        from .resources.attachments import AsyncAttachmentsResourceWithStreamingResponse

        return AsyncAttachmentsResourceWithStreamingResponse(self._client.attachments)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        """`Auth` represents the current API Keys authentication details.

        It can be
        used to check that a token is still valid and load the IDs for the current
        user and workspace.
        """
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def collections(self) -> collections.AsyncCollectionsResourceWithStreamingResponse:
        """
        `Collections` represent grouping of documents in the knowledge base, they
        offer a way to structure information in a nested hierarchy and a level
        at which read and write permissions can be granted to individual users or
        groups of users.
        """
        from .resources.collections import AsyncCollectionsResourceWithStreamingResponse

        return AsyncCollectionsResourceWithStreamingResponse(self._client.collections)

    @cached_property
    def comments(self) -> comments.AsyncCommentsResourceWithStreamingResponse:
        """
        `Comments` represent a comment either on a selection of text in a document
        or on the document itself.
        """
        from .resources.comments import AsyncCommentsResourceWithStreamingResponse

        return AsyncCommentsResourceWithStreamingResponse(self._client.comments)

    @cached_property
    def documents(self) -> documents.AsyncDocumentsResourceWithStreamingResponse:
        """`Documents` are what everything else revolves around.

        A document represents
        a single page of information and always returns the latest version of the
        content. Documents are stored in [Markdown](https://spec.commonmark.org/)
        formatting.
        """
        from .resources.documents import AsyncDocumentsResourceWithStreamingResponse

        return AsyncDocumentsResourceWithStreamingResponse(self._client.documents)

    @cached_property
    def events(self) -> events.AsyncEventsResourceWithStreamingResponse:
        """`Events` represent an artifact of an action.

        Whether it is creating a user,
        editing a document, changing permissions, or any other action – an event
        is created that can be used as an audit trail or activity stream.
        """
        from .resources.events import AsyncEventsResourceWithStreamingResponse

        return AsyncEventsResourceWithStreamingResponse(self._client.events)

    @cached_property
    def file_operations(self) -> file_operations.AsyncFileOperationsResourceWithStreamingResponse:
        """
        `FileOperations` represent background jobs for importing or exporting files.
        You can query the file operation to find the state of progress and any
        resulting output.
        """
        from .resources.file_operations import AsyncFileOperationsResourceWithStreamingResponse

        return AsyncFileOperationsResourceWithStreamingResponse(self._client.file_operations)

    @cached_property
    def groups(self) -> groups.AsyncGroupsResourceWithStreamingResponse:
        """
        `Groups` represent a list of users that logically belong together, for
        example there might be groups for each department in your organization.
        Groups can be granted access to collections with read or write permissions.
        """
        from .resources.groups import AsyncGroupsResourceWithStreamingResponse

        return AsyncGroupsResourceWithStreamingResponse(self._client.groups)


Client = Outline

AsyncClient = AsyncOutline
