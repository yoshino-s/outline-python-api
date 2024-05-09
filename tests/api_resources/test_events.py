# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import EventCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Outline) -> None:
        event = client.events.create()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Outline) -> None:
        event = client.events.create(
            actor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audit_log=True,
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="DESC",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            name="string",
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Outline) -> None:
        response = client.events.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Outline) -> None:
        with client.events.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(EventCreateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOutline) -> None:
        event = await async_client.events.create()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOutline) -> None:
        event = await async_client.events.create(
            actor_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            audit_log=True,
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="DESC",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            name="string",
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOutline) -> None:
        response = await async_client.events.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(EventCreateResponse, event, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOutline) -> None:
        async with async_client.events.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(EventCreateResponse, event, path=["response"])

        assert cast(Any, response.is_closed) is True
