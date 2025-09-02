# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._oauth2 import OAuth2ClientCredentials
from ._version import __version__
from .resources import auth, events, groups, comments, documents, attachments, file_operations
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import OutlineError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.collections import collections

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Outline", "AsyncOutline", "Client", "AsyncClient"]


class Outline(SyncAPIClient):
    attachments: attachments.AttachmentsResource
    auth: auth.AuthResource
    collections: collections.CollectionsResource
    comments: comments.CommentsResource
    documents: documents.DocumentsResource
    events: events.EventsResource
    file_operations: file_operations.FileOperationsResource
    groups: groups.GroupsResource
    with_raw_response: OutlineWithRawResponse
    with_streaming_response: OutlineWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.attachments = attachments.AttachmentsResource(self)
        self.auth = auth.AuthResource(self)
        self.collections = collections.CollectionsResource(self)
        self.comments = comments.CommentsResource(self)
        self.documents = documents.DocumentsResource(self)
        self.events = events.EventsResource(self)
        self.file_operations = file_operations.FileOperationsResource(self)
        self.groups = groups.GroupsResource(self)
        self.with_raw_response = OutlineWithRawResponse(self)
        self.with_streaming_response = OutlineWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def custom_auth(self) -> httpx.Auth | None:
        raise NotImplementedError("This auth method has not been implemented yet.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    attachments: attachments.AsyncAttachmentsResource
    auth: auth.AsyncAuthResource
    collections: collections.AsyncCollectionsResource
    comments: comments.AsyncCommentsResource
    documents: documents.AsyncDocumentsResource
    events: events.AsyncEventsResource
    file_operations: file_operations.AsyncFileOperationsResource
    groups: groups.AsyncGroupsResource
    with_raw_response: AsyncOutlineWithRawResponse
    with_streaming_response: AsyncOutlineWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.attachments = attachments.AsyncAttachmentsResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.collections = collections.AsyncCollectionsResource(self)
        self.comments = comments.AsyncCommentsResource(self)
        self.documents = documents.AsyncDocumentsResource(self)
        self.events = events.AsyncEventsResource(self)
        self.file_operations = file_operations.AsyncFileOperationsResource(self)
        self.groups = groups.AsyncGroupsResource(self)
        self.with_raw_response = AsyncOutlineWithRawResponse(self)
        self.with_streaming_response = AsyncOutlineWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def custom_auth(self) -> httpx.Auth | None:
        raise NotImplementedError("This auth method has not been implemented yet.")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _should_retry(self, response: httpx.Response) -> bool:
        # Retry on 401 if we are using OAuth2 and the token might be expired
        if response.status_code == 401 and isinstance(self.custom_auth, OAuth2ClientCredentials):
            if self.custom_auth.token_is_expired():
                self.custom_auth.invalidate_token()
                return True
        return super()._should_retry(response)

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def __init__(self, client: Outline) -> None:
        self.attachments = attachments.AttachmentsResourceWithRawResponse(client.attachments)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.collections = collections.CollectionsResourceWithRawResponse(client.collections)
        self.comments = comments.CommentsResourceWithRawResponse(client.comments)
        self.documents = documents.DocumentsResourceWithRawResponse(client.documents)
        self.events = events.EventsResourceWithRawResponse(client.events)
        self.file_operations = file_operations.FileOperationsResourceWithRawResponse(client.file_operations)
        self.groups = groups.GroupsResourceWithRawResponse(client.groups)


class AsyncOutlineWithRawResponse:
    def __init__(self, client: AsyncOutline) -> None:
        self.attachments = attachments.AsyncAttachmentsResourceWithRawResponse(client.attachments)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.collections = collections.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.comments = comments.AsyncCommentsResourceWithRawResponse(client.comments)
        self.documents = documents.AsyncDocumentsResourceWithRawResponse(client.documents)
        self.events = events.AsyncEventsResourceWithRawResponse(client.events)
        self.file_operations = file_operations.AsyncFileOperationsResourceWithRawResponse(client.file_operations)
        self.groups = groups.AsyncGroupsResourceWithRawResponse(client.groups)


class OutlineWithStreamedResponse:
    def __init__(self, client: Outline) -> None:
        self.attachments = attachments.AttachmentsResourceWithStreamingResponse(client.attachments)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.collections = collections.CollectionsResourceWithStreamingResponse(client.collections)
        self.comments = comments.CommentsResourceWithStreamingResponse(client.comments)
        self.documents = documents.DocumentsResourceWithStreamingResponse(client.documents)
        self.events = events.EventsResourceWithStreamingResponse(client.events)
        self.file_operations = file_operations.FileOperationsResourceWithStreamingResponse(client.file_operations)
        self.groups = groups.GroupsResourceWithStreamingResponse(client.groups)


class AsyncOutlineWithStreamedResponse:
    def __init__(self, client: AsyncOutline) -> None:
        self.attachments = attachments.AsyncAttachmentsResourceWithStreamingResponse(client.attachments)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.collections = collections.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.comments = comments.AsyncCommentsResourceWithStreamingResponse(client.comments)
        self.documents = documents.AsyncDocumentsResourceWithStreamingResponse(client.documents)
        self.events = events.AsyncEventsResourceWithStreamingResponse(client.events)
        self.file_operations = file_operations.AsyncFileOperationsResourceWithStreamingResponse(client.file_operations)
        self.groups = groups.AsyncGroupsResourceWithStreamingResponse(client.groups)


Client = Outline

AsyncClient = AsyncOutline
