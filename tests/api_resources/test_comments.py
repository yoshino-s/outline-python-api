# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import (
    CommentListResponse,
    CommentCreateResponse,
    CommentDeleteResponse,
    CommentUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Outline) -> None:
        comment = client.comments.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Outline) -> None:
        comment = client.comments.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Outline) -> None:
        response = client.comments.with_raw_response.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Outline) -> None:
        with client.comments.with_streaming_response.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Outline) -> None:
        comment = client.comments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Outline) -> None:
        response = client.comments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Outline) -> None:
        with client.comments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentUpdateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Outline) -> None:
        comment = client.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Outline) -> None:
        comment = client.comments.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="DESC",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Outline) -> None:
        response = client.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Outline) -> None:
        with client.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Outline) -> None:
        comment = client.comments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Outline) -> None:
        response = client.comments.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Outline) -> None:
        with client.comments.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncComments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOutline) -> None:
        comment = await async_client.comments.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOutline) -> None:
        comment = await async_client.comments.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_comment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOutline) -> None:
        response = await async_client.comments.with_raw_response.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentCreateResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOutline) -> None:
        async with async_client.comments.with_streaming_response.create(
            data={},
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentCreateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOutline) -> None:
        comment = await async_client.comments.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
        )
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOutline) -> None:
        response = await async_client.comments.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentUpdateResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOutline) -> None:
        async with async_client.comments.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentUpdateResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOutline) -> None:
        comment = await async_client.comments.list()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOutline) -> None:
        comment = await async_client.comments.list(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="DESC",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOutline) -> None:
        response = await async_client.comments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentListResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOutline) -> None:
        async with async_client.comments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentListResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOutline) -> None:
        comment = await async_client.comments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOutline) -> None:
        response = await async_client.comments.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = await response.parse()
        assert_matches_type(CommentDeleteResponse, comment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOutline) -> None:
        async with async_client.comments.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CommentDeleteResponse, comment, path=["response"])

        assert cast(Any, response.is_closed) is True
