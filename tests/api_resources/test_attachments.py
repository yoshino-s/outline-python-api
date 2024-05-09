# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import (
    AttachmentCreateResponse,
    AttachmentDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttachments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Outline) -> None:
        attachment = client.attachments.create(
            content_type="image/png",
            name="image.png",
            size=0,
        )
        assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Outline) -> None:
        attachment = client.attachments.create(
            content_type="image/png",
            name="image.png",
            size=0,
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Outline) -> None:
        response = client.attachments.with_raw_response.create(
            content_type="image/png",
            name="image.png",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Outline) -> None:
        with client.attachments.with_streaming_response.create(
            content_type="image/png",
            name="image.png",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Outline) -> None:
        attachment = client.attachments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Outline) -> None:
        response = client.attachments.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Outline) -> None:
        with client.attachments.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_redirect(self, client: Outline) -> None:
        attachment = client.attachments.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert attachment is None

    @parametrize
    def test_raw_response_redirect(self, client: Outline) -> None:
        response = client.attachments.with_raw_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = response.parse()
        assert attachment is None

    @parametrize
    def test_streaming_response_redirect(self, client: Outline) -> None:
        with client.attachments.with_streaming_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = response.parse()
            assert attachment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAttachments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOutline) -> None:
        attachment = await async_client.attachments.create(
            content_type="image/png",
            name="image.png",
            size=0,
        )
        assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOutline) -> None:
        attachment = await async_client.attachments.create(
            content_type="image/png",
            name="image.png",
            size=0,
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOutline) -> None:
        response = await async_client.attachments.with_raw_response.create(
            content_type="image/png",
            name="image.png",
            size=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOutline) -> None:
        async with async_client.attachments.with_streaming_response.create(
            content_type="image/png",
            name="image.png",
            size=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentCreateResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOutline) -> None:
        attachment = await async_client.attachments.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOutline) -> None:
        response = await async_client.attachments.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOutline) -> None:
        async with async_client.attachments.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert_matches_type(AttachmentDeleteResponse, attachment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_redirect(self, async_client: AsyncOutline) -> None:
        attachment = await async_client.attachments.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert attachment is None

    @parametrize
    async def test_raw_response_redirect(self, async_client: AsyncOutline) -> None:
        response = await async_client.attachments.with_raw_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attachment = await response.parse()
        assert attachment is None

    @parametrize
    async def test_streaming_response_redirect(self, async_client: AsyncOutline) -> None:
        async with async_client.attachments.with_streaming_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attachment = await response.parse()
            assert attachment is None

        assert cast(Any, response.is_closed) is True
