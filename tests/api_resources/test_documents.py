# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from outline import Outline, AsyncOutline
from tests.utils import assert_matches_type
from outline.types import (
    DocumentInfoResponse,
    DocumentListResponse,
    DocumentMoveResponse,
    DocumentStarResponse,
    DocumentCreateResponse,
    DocumentDeleteResponse,
    DocumentDraftsResponse,
    DocumentExportResponse,
    DocumentImportResponse,
    DocumentSearchResponse,
    DocumentUnstarResponse,
    DocumentUpdateResponse,
    DocumentViewedResponse,
    DocumentArchiveResponse,
    DocumentRestoreResponse,
    DocumentUnpublishResponse,
    DocumentTemplatizeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Outline) -> None:
        document = client.documents.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Outline) -> None:
        document = client.documents.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            publish=True,
            template=True,
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="…",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Outline) -> None:
        response = client.documents.with_raw_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Outline) -> None:
        with client.documents.with_streaming_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Outline) -> None:
        document = client.documents.update(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Outline) -> None:
        document = client.documents.update(
            id="hDYep1TPAM",
            append=True,
            done=True,
            publish=True,
            text="…",
            title="string",
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Outline) -> None:
        response = client.documents.with_raw_response.update(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Outline) -> None:
        with client.documents.with_streaming_response.update(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentUpdateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Outline) -> None:
        document = client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Outline) -> None:
        document = client.documents.list(
            backlink_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="DESC",
            limit=25,
            offset=0,
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="updatedAt",
            template=True,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Outline) -> None:
        response = client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Outline) -> None:
        with client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Outline) -> None:
        document = client.documents.delete(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Outline) -> None:
        document = client.documents.delete(
            id="hDYep1TPAM",
            permanent=False,
        )
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Outline) -> None:
        response = client.documents.with_raw_response.delete(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Outline) -> None:
        with client.documents.with_streaming_response.delete(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentDeleteResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_archive(self, client: Outline) -> None:
        document = client.documents.archive(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentArchiveResponse, document, path=["response"])

    @parametrize
    def test_raw_response_archive(self, client: Outline) -> None:
        response = client.documents.with_raw_response.archive(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentArchiveResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_archive(self, client: Outline) -> None:
        with client.documents.with_streaming_response.archive(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentArchiveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_drafts(self, client: Outline) -> None:
        document = client.documents.drafts()
        assert_matches_type(DocumentDraftsResponse, document, path=["response"])

    @parametrize
    def test_method_drafts_with_all_params(self, client: Outline) -> None:
        document = client.documents.drafts(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            date_filter="month",
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(DocumentDraftsResponse, document, path=["response"])

    @parametrize
    def test_raw_response_drafts(self, client: Outline) -> None:
        response = client.documents.with_raw_response.drafts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentDraftsResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_drafts(self, client: Outline) -> None:
        with client.documents.with_streaming_response.drafts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentDraftsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_export(self, client: Outline) -> None:
        document = client.documents.export()
        assert_matches_type(DocumentExportResponse, document, path=["response"])

    @parametrize
    def test_method_export_with_all_params(self, client: Outline) -> None:
        document = client.documents.export(
            id="string",
        )
        assert_matches_type(DocumentExportResponse, document, path=["response"])

    @parametrize
    def test_raw_response_export(self, client: Outline) -> None:
        response = client.documents.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentExportResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_export(self, client: Outline) -> None:
        with client.documents.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentExportResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_import(self, client: Outline) -> None:
        document = client.documents.import_()
        assert_matches_type(DocumentImportResponse, document, path=["response"])

    @parametrize
    def test_method_import_with_all_params(self, client: Outline) -> None:
        document = client.documents.import_(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file={},
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            publish=True,
            template=True,
        )
        assert_matches_type(DocumentImportResponse, document, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Outline) -> None:
        response = client.documents.with_raw_response.import_()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentImportResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Outline) -> None:
        with client.documents.with_streaming_response.import_() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentImportResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_info(self, client: Outline) -> None:
        document = client.documents.info()
        assert_matches_type(DocumentInfoResponse, document, path=["response"])

    @parametrize
    def test_method_info_with_all_params(self, client: Outline) -> None:
        document = client.documents.info(
            id="string",
            share_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentInfoResponse, document, path=["response"])

    @parametrize
    def test_raw_response_info(self, client: Outline) -> None:
        response = client.documents.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentInfoResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_info(self, client: Outline) -> None:
        with client.documents.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentInfoResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_move(self, client: Outline) -> None:
        document = client.documents.move(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentMoveResponse, document, path=["response"])

    @parametrize
    def test_method_move_with_all_params(self, client: Outline) -> None:
        document = client.documents.move(
            id="hDYep1TPAM",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentMoveResponse, document, path=["response"])

    @parametrize
    def test_raw_response_move(self, client: Outline) -> None:
        response = client.documents.with_raw_response.move(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentMoveResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_move(self, client: Outline) -> None:
        with client.documents.with_streaming_response.move(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentMoveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_restore(self, client: Outline) -> None:
        document = client.documents.restore(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @parametrize
    def test_method_restore_with_all_params(self, client: Outline) -> None:
        document = client.documents.restore(
            id="hDYep1TPAM",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @parametrize
    def test_raw_response_restore(self, client: Outline) -> None:
        response = client.documents.with_raw_response.restore(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_restore(self, client: Outline) -> None:
        with client.documents.with_streaming_response.restore(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentRestoreResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Outline) -> None:
        document = client.documents.search()
        assert_matches_type(DocumentSearchResponse, document, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Outline) -> None:
        document = client.documents.search(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            date_filter="month",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            offset=0,
            query="hiring",
            status_filter="published",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentSearchResponse, document, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Outline) -> None:
        response = client.documents.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentSearchResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Outline) -> None:
        with client.documents.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentSearchResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_star(self, client: Outline) -> None:
        document = client.documents.star(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentStarResponse, document, path=["response"])

    @parametrize
    def test_raw_response_star(self, client: Outline) -> None:
        response = client.documents.with_raw_response.star(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentStarResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_star(self, client: Outline) -> None:
        with client.documents.with_streaming_response.star(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentStarResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_templatize(self, client: Outline) -> None:
        document = client.documents.templatize(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentTemplatizeResponse, document, path=["response"])

    @parametrize
    def test_raw_response_templatize(self, client: Outline) -> None:
        response = client.documents.with_raw_response.templatize(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentTemplatizeResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_templatize(self, client: Outline) -> None:
        with client.documents.with_streaming_response.templatize(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentTemplatizeResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unpublish(self, client: Outline) -> None:
        document = client.documents.unpublish(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentUnpublishResponse, document, path=["response"])

    @parametrize
    def test_raw_response_unpublish(self, client: Outline) -> None:
        response = client.documents.with_raw_response.unpublish(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentUnpublishResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_unpublish(self, client: Outline) -> None:
        with client.documents.with_streaming_response.unpublish(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentUnpublishResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unstar(self, client: Outline) -> None:
        document = client.documents.unstar(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentUnstarResponse, document, path=["response"])

    @parametrize
    def test_raw_response_unstar(self, client: Outline) -> None:
        response = client.documents.with_raw_response.unstar(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentUnstarResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_unstar(self, client: Outline) -> None:
        with client.documents.with_streaming_response.unstar(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentUnstarResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_viewed(self, client: Outline) -> None:
        document = client.documents.viewed()
        assert_matches_type(DocumentViewedResponse, document, path=["response"])

    @parametrize
    def test_method_viewed_with_all_params(self, client: Outline) -> None:
        document = client.documents.viewed(
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(DocumentViewedResponse, document, path=["response"])

    @parametrize
    def test_raw_response_viewed(self, client: Outline) -> None:
        response = client.documents.with_raw_response.viewed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = response.parse()
        assert_matches_type(DocumentViewedResponse, document, path=["response"])

    @parametrize
    def test_streaming_response_viewed(self, client: Outline) -> None:
        with client.documents.with_streaming_response.viewed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = response.parse()
            assert_matches_type(DocumentViewedResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            publish=True,
            template=True,
            template_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            text="…",
        )
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentCreateResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.create(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            title="Welcome to Acme Inc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentCreateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.update(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.update(
            id="hDYep1TPAM",
            append=True,
            done=True,
            publish=True,
            text="…",
            title="string",
        )
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.update(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentUpdateResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.update(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentUpdateResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.list()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.list(
            backlink_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            direction="DESC",
            limit=25,
            offset=0,
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="updatedAt",
            template=True,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentListResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentListResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.delete(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.delete(
            id="hDYep1TPAM",
            permanent=False,
        )
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.delete(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentDeleteResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.delete(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentDeleteResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_archive(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.archive(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentArchiveResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.archive(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentArchiveResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.archive(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentArchiveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_drafts(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.drafts()
        assert_matches_type(DocumentDraftsResponse, document, path=["response"])

    @parametrize
    async def test_method_drafts_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.drafts(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            date_filter="month",
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(DocumentDraftsResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_drafts(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.drafts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentDraftsResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_drafts(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.drafts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentDraftsResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_export(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.export()
        assert_matches_type(DocumentExportResponse, document, path=["response"])

    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.export(
            id="string",
        )
        assert_matches_type(DocumentExportResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_export(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.export()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentExportResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.export() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentExportResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_import(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.import_()
        assert_matches_type(DocumentImportResponse, document, path=["response"])

    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.import_(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file={},
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            publish=True,
            template=True,
        )
        assert_matches_type(DocumentImportResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.import_()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentImportResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.import_() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentImportResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_info(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.info()
        assert_matches_type(DocumentInfoResponse, document, path=["response"])

    @parametrize
    async def test_method_info_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.info(
            id="string",
            share_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentInfoResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_info(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentInfoResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_info(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentInfoResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_move(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.move(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentMoveResponse, document, path=["response"])

    @parametrize
    async def test_method_move_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.move(
            id="hDYep1TPAM",
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parent_document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentMoveResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_move(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.move(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentMoveResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.move(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentMoveResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_restore(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.restore(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.restore(
            id="hDYep1TPAM",
            revision_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.restore(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentRestoreResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.restore(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentRestoreResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.search()
        assert_matches_type(DocumentSearchResponse, document, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.search(
            collection_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            date_filter="month",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=25,
            offset=0,
            query="hiring",
            status_filter="published",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentSearchResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentSearchResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentSearchResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_star(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.star(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentStarResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_star(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.star(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentStarResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_star(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.star(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentStarResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_templatize(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.templatize(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DocumentTemplatizeResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_templatize(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.templatize(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentTemplatizeResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_templatize(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.templatize(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentTemplatizeResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unpublish(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.unpublish(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentUnpublishResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_unpublish(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.unpublish(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentUnpublishResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_unpublish(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.unpublish(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentUnpublishResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unstar(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.unstar(
            id="hDYep1TPAM",
        )
        assert_matches_type(DocumentUnstarResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_unstar(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.unstar(
            id="hDYep1TPAM",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentUnstarResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_unstar(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.unstar(
            id="hDYep1TPAM",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentUnstarResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_viewed(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.viewed()
        assert_matches_type(DocumentViewedResponse, document, path=["response"])

    @parametrize
    async def test_method_viewed_with_all_params(self, async_client: AsyncOutline) -> None:
        document = await async_client.documents.viewed(
            direction="DESC",
            limit=25,
            offset=0,
            sort="updatedAt",
        )
        assert_matches_type(DocumentViewedResponse, document, path=["response"])

    @parametrize
    async def test_raw_response_viewed(self, async_client: AsyncOutline) -> None:
        response = await async_client.documents.with_raw_response.viewed()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        document = await response.parse()
        assert_matches_type(DocumentViewedResponse, document, path=["response"])

    @parametrize
    async def test_streaming_response_viewed(self, async_client: AsyncOutline) -> None:
        async with async_client.documents.with_streaming_response.viewed() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            document = await response.parse()
            assert_matches_type(DocumentViewedResponse, document, path=["response"])

        assert cast(Any, response.is_closed) is True
