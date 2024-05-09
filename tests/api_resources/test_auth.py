# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import AuthInfoResponse, AuthConfigResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_config(self, client: Outline) -> None:
        auth = client.auth.config()
        assert_matches_type(AuthConfigResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_config(self, client: Outline) -> None:
        response = client.auth.with_raw_response.config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthConfigResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_config(self, client: Outline) -> None:
        with client.auth.with_streaming_response.config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthConfigResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Outline) -> None:
        auth = client.auth.info()
        assert_matches_type(AuthInfoResponse, auth, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Outline) -> None:
        response = client.auth.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthInfoResponse, auth, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Outline) -> None:
        with client.auth.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthInfoResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_config(self, async_client: AsyncOutline) -> None:
        auth = await async_client.auth.config()
        assert_matches_type(AuthConfigResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_config(self, async_client: AsyncOutline) -> None:
        response = await async_client.auth.with_raw_response.config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthConfigResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_config(self, async_client: AsyncOutline) -> None:
        async with async_client.auth.with_streaming_response.config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthConfigResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncOutline) -> None:
        auth = await async_client.auth.info()
        assert_matches_type(AuthInfoResponse, auth, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncOutline) -> None:
        response = await async_client.auth.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthInfoResponse, auth, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncOutline) -> None:
        async with async_client.auth.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthInfoResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True
