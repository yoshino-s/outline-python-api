# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types.collections import GroupMembershipListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroupMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Outline) -> None:
        group_membership = client.collections.group_memberships.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Outline) -> None:
        group_membership = client.collections.group_memberships.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            offset=0,
            permission="read",
            query="developers",
        )
        assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Outline) -> None:
        response = client.collections.group_memberships.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group_membership = response.parse()
        assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Outline) -> None:
        with client.collections.group_memberships.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group_membership = response.parse()
            assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGroupMemberships:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOutline) -> None:
        group_membership = await async_client.collections.group_memberships.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOutline) -> None:
        group_membership = await async_client.collections.group_memberships.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            offset=0,
            permission="read",
            query="developers",
        )
        assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOutline) -> None:
        response = await async_client.collections.group_memberships.with_raw_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group_membership = await response.parse()
        assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOutline) -> None:
        async with async_client.collections.group_memberships.with_streaming_response.list(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group_membership = await response.parse()
            assert_matches_type(GroupMembershipListResponse, group_membership, path=["response"])

        assert cast(Any, response.is_closed) is True
