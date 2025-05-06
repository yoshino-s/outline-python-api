# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import (
    FileOperationInfoResponse,
    FileOperationListResponse,
    FileOperationDeleteResponse,
)
from outline._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFileOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Outline) -> None:
        file_operation = client.file_operations.list(
            type="export",
        )
        assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Outline) -> None:
        file_operation = client.file_operations.list(
            type="export",
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Outline) -> None:
        response = client.file_operations.with_raw_response.list(
            type="export",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_operation = response.parse()
        assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Outline) -> None:
        with client.file_operations.with_streaming_response.list(
            type="export",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_operation = response.parse()
            assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Outline) -> None:
        file_operation = client.file_operations.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileOperationDeleteResponse, file_operation, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Outline) -> None:
        response = client.file_operations.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_operation = response.parse()
        assert_matches_type(FileOperationDeleteResponse, file_operation, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Outline) -> None:
        with client.file_operations.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_operation = response.parse()
            assert_matches_type(FileOperationDeleteResponse, file_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Outline) -> None:
        file_operation = client.file_operations.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileOperationInfoResponse, file_operation, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Outline) -> None:
        response = client.file_operations.with_raw_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_operation = response.parse()
        assert_matches_type(FileOperationInfoResponse, file_operation, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Outline) -> None:
        with client.file_operations.with_streaming_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_operation = response.parse()
            assert_matches_type(FileOperationInfoResponse, file_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_redirect(self, client: Outline, respx_mock: MockRouter) -> None:
        respx_mock.post("/fileOperations.redirect").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file_operation = client.file_operations.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file_operation.is_closed
        assert file_operation.json() == {"foo": "bar"}
        assert cast(Any, file_operation.is_closed) is True
        assert isinstance(file_operation, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_redirect(self, client: Outline, respx_mock: MockRouter) -> None:
        respx_mock.post("/fileOperations.redirect").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        file_operation = client.file_operations.with_raw_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert file_operation.is_closed is True
        assert file_operation.http_request.headers.get("X-Stainless-Lang") == "python"
        assert file_operation.json() == {"foo": "bar"}
        assert isinstance(file_operation, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_redirect(self, client: Outline, respx_mock: MockRouter) -> None:
        respx_mock.post("/fileOperations.redirect").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.file_operations.with_streaming_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as file_operation:
            assert not file_operation.is_closed
            assert file_operation.http_request.headers.get("X-Stainless-Lang") == "python"

            assert file_operation.json() == {"foo": "bar"}
            assert cast(Any, file_operation.is_closed) is True
            assert isinstance(file_operation, StreamedBinaryAPIResponse)

        assert cast(Any, file_operation.is_closed) is True


class TestAsyncFileOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOutline) -> None:
        file_operation = await async_client.file_operations.list(
            type="export",
        )
        assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOutline) -> None:
        file_operation = await async_client.file_operations.list(
            type="export",
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOutline) -> None:
        response = await async_client.file_operations.with_raw_response.list(
            type="export",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_operation = await response.parse()
        assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOutline) -> None:
        async with async_client.file_operations.with_streaming_response.list(
            type="export",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_operation = await response.parse()
            assert_matches_type(FileOperationListResponse, file_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOutline) -> None:
        file_operation = await async_client.file_operations.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileOperationDeleteResponse, file_operation, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOutline) -> None:
        response = await async_client.file_operations.with_raw_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_operation = await response.parse()
        assert_matches_type(FileOperationDeleteResponse, file_operation, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOutline) -> None:
        async with async_client.file_operations.with_streaming_response.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_operation = await response.parse()
            assert_matches_type(FileOperationDeleteResponse, file_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncOutline) -> None:
        file_operation = await async_client.file_operations.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileOperationInfoResponse, file_operation, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncOutline) -> None:
        response = await async_client.file_operations.with_raw_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file_operation = await response.parse()
        assert_matches_type(FileOperationInfoResponse, file_operation, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncOutline) -> None:
        async with async_client.file_operations.with_streaming_response.info(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file_operation = await response.parse()
            assert_matches_type(FileOperationInfoResponse, file_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_redirect(self, async_client: AsyncOutline, respx_mock: MockRouter) -> None:
        respx_mock.post("/fileOperations.redirect").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        file_operation = await async_client.file_operations.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file_operation.is_closed
        assert await file_operation.json() == {"foo": "bar"}
        assert cast(Any, file_operation.is_closed) is True
        assert isinstance(file_operation, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_redirect(self, async_client: AsyncOutline, respx_mock: MockRouter) -> None:
        respx_mock.post("/fileOperations.redirect").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        file_operation = await async_client.file_operations.with_raw_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert file_operation.is_closed is True
        assert file_operation.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await file_operation.json() == {"foo": "bar"}
        assert isinstance(file_operation, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_redirect(self, async_client: AsyncOutline, respx_mock: MockRouter) -> None:
        respx_mock.post("/fileOperations.redirect").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.file_operations.with_streaming_response.redirect(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as file_operation:
            assert not file_operation.is_closed
            assert file_operation.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await file_operation.json() == {"foo": "bar"}
            assert cast(Any, file_operation.is_closed) is True
            assert isinstance(file_operation, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, file_operation.is_closed) is True
