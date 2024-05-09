# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import (
    CollectionListResponse,
    CollectionCreateResponse,
    CollectionDeleteResponse,
    CollectionExportResponse,
    CollectionUpdateResponse,
    CollectionAddUserResponse,
    CollectionAddGroupResponse,
    CollectionRetrieveResponse,
    CollectionDocumentsResponse,
    CollectionExportAllResponse,
    CollectionRemoveUserResponse,
    CollectionRemoveGroupResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Outline) -> None:
        collection = client.collections.create(
            name="Human Resources",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Outline) -> None:
        collection = client.collections.create(
            name="Human Resources",
            color="#123123",
            description="",
            permission="read",
            private=False,
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Outline) -> None:
        response = client.collections.with_raw_response.create(
            name="Human Resources",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Outline) -> None:
        with client.collections.with_streaming_response.create(
            name="Human Resources",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionCreateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Outline) -> None:
        collection = client.collections.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Outline) -> None:
        response = client.collections.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Outline) -> None:
        with client.collections.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Outline) -> None:
        collection = client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Outline) -> None:
        collection = client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            color="#123123",
            description="",
            name="Human Resources",
            permission="read",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Outline) -> None:
        response = client.collections.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Outline) -> None:
        with client.collections.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Outline) -> None:
        collection = client.collections.list()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Outline) -> None:
        collection = client.collections.list(
            limit=25,
            offset=0,
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Outline) -> None:
        response = client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Outline) -> None:
        with client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Outline) -> None:
        collection = client.collections.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Outline) -> None:
        response = client.collections.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Outline) -> None:
        with client.collections.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_group(self, client: Outline) -> None:
        collection = client.collections.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

    @parametrize
    def test_method_add_group_with_all_params(self, client: Outline) -> None:
        collection = client.collections.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            permission="read",
        )
        assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_add_group(self, client: Outline) -> None:
        response = client.collections.with_raw_response.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_add_group(self, client: Outline) -> None:
        with client.collections.with_streaming_response.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_user(self, client: Outline) -> None:
        collection = client.collections.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

    @parametrize
    def test_method_add_user_with_all_params(self, client: Outline) -> None:
        collection = client.collections.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            permission="read",
        )
        assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_add_user(self, client: Outline) -> None:
        response = client.collections.with_raw_response.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_add_user(self, client: Outline) -> None:
        with client.collections.with_streaming_response.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_documents(self, client: Outline) -> None:
        collection = client.collections.documents(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionDocumentsResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_documents(self, client: Outline) -> None:
        response = client.collections.with_raw_response.documents(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionDocumentsResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_documents(self, client: Outline) -> None:
        with client.collections.with_streaming_response.documents(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionDocumentsResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export(self, client: Outline) -> None:
        collection = client.collections.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionExportResponse, collection, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Outline) -> None:
        collection = client.collections.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            format="outline-markdown",
        )
        assert_matches_type(CollectionExportResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Outline) -> None:
        response = client.collections.with_raw_response.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionExportResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Outline) -> None:
        with client.collections.with_streaming_response.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionExportResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export_all(self, client: Outline) -> None:
        collection = client.collections.export_all()
        assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

    @parametrize
    def test_method_export_all_with_all_params(self, client: Outline) -> None:
        collection = client.collections.export_all(
            format="outline-markdown",
        )
        assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_export_all(self, client: Outline) -> None:
        response = client.collections.with_raw_response.export_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_export_all(self, client: Outline) -> None:
        with client.collections.with_streaming_response.export_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_group(self, client: Outline) -> None:
        collection = client.collections.remove_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRemoveGroupResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_remove_group(self, client: Outline) -> None:
        response = client.collections.with_raw_response.remove_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRemoveGroupResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_remove_group(self, client: Outline) -> None:
        with client.collections.with_streaming_response.remove_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRemoveGroupResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_user(self, client: Outline) -> None:
        collection = client.collections.remove_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRemoveUserResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_remove_user(self, client: Outline) -> None:
        response = client.collections.with_raw_response.remove_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionRemoveUserResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_remove_user(self, client: Outline) -> None:
        with client.collections.with_streaming_response.remove_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionRemoveUserResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.create(
            name="Human Resources",
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.create(
            name="Human Resources",
            color="#123123",
            description="",
            permission="read",
            private=False,
        )
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.create(
            name="Human Resources",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionCreateResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.create(
            name="Human Resources",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionCreateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRetrieveResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            color="#123123",
            description="",
            name="Human Resources",
            permission="read",
        )
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionUpdateResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.list()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.list(
            limit=25,
            offset=0,
        )
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionListResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_group(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

    @parametrize
    async def test_method_add_group_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            permission="read",
        )
        assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_add_group(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_add_group(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.add_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionAddGroupResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_user(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

    @parametrize
    async def test_method_add_user_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            permission="read",
        )
        assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_add_user(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_add_user(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.add_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionAddUserResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_documents(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.documents(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionDocumentsResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_documents(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.documents(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionDocumentsResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_documents(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.documents(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionDocumentsResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionExportResponse, collection, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            format="outline-markdown",
        )
        assert_matches_type(CollectionExportResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionExportResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.export(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionExportResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export_all(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.export_all()
        assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

    @parametrize
    async def test_method_export_all_with_all_params(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.export_all(
            format="outline-markdown",
        )
        assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_export_all(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.export_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_export_all(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.export_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionExportAllResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_group(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.remove_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRemoveGroupResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_remove_group(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.remove_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRemoveGroupResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_remove_group(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.remove_group(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRemoveGroupResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_user(self, async_client: AsyncOutline) -> None:
        collection = await async_client.collections.remove_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CollectionRemoveUserResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_remove_user(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.with_raw_response.remove_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionRemoveUserResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_remove_user(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.with_streaming_response.remove_user(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionRemoveUserResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True
