# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import (
    GroupInfoResponse,
    GroupListResponse,
    GroupCreateResponse,
    GroupDeleteResponse,
    GroupUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Outline) -> None:
        group = client.groups.create(
            name="Designers",
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Outline) -> None:
        response = client.groups.with_raw_response.create(
            name="Designers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Outline) -> None:
        with client.groups.with_streaming_response.create(
            name="Designers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Outline) -> None:
        group = client.groups.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Designers",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Outline) -> None:
        response = client.groups.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Designers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Outline) -> None:
        with client.groups.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Designers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Outline) -> None:
        group = client.groups.list()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Outline) -> None:
        group = client.groups.list(
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Outline) -> None:
        response = client.groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Outline) -> None:
        with client.groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupListResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Outline) -> None:
        group = client.groups.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Outline) -> None:
        response = client.groups.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Outline) -> None:
        with client.groups.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Outline) -> None:
        group = client.groups.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupInfoResponse, group, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Outline) -> None:
        response = client.groups.with_raw_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupInfoResponse, group, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Outline) -> None:
        with client.groups.with_streaming_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupInfoResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOutline) -> None:
        group = await async_client.groups.create(
            name="Designers",
        )
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOutline) -> None:
        response = await async_client.groups.with_raw_response.create(
            name="Designers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupCreateResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOutline) -> None:
        async with async_client.groups.with_streaming_response.create(
            name="Designers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupCreateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOutline) -> None:
        group = await async_client.groups.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Designers",
        )
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOutline) -> None:
        response = await async_client.groups.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Designers",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupUpdateResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOutline) -> None:
        async with async_client.groups.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="Designers",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupUpdateResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOutline) -> None:
        group = await async_client.groups.list()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOutline) -> None:
        group = await async_client.groups.list(
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(GroupListResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOutline) -> None:
        response = await async_client.groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupListResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOutline) -> None:
        async with async_client.groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupListResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOutline) -> None:
        group = await async_client.groups.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOutline) -> None:
        response = await async_client.groups.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupDeleteResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOutline) -> None:
        async with async_client.groups.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupDeleteResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncOutline) -> None:
        group = await async_client.groups.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupInfoResponse, group, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncOutline) -> None:
        response = await async_client.groups.with_raw_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupInfoResponse, group, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncOutline) -> None:
        async with async_client.groups.with_streaming_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupInfoResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True
