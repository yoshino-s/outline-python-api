# Shared Types

```python
from outline.types import Pagination
```

# Attachments

Types:

```python
from outline.types import AttachmentCreateResponse, AttachmentDeleteResponse
```

Methods:

- <code title="post /attachments.create">client.attachments.<a href="./src/outline/resources/attachments.py">create</a>(\*\*<a href="src/outline/types/attachment_create_params.py">params</a>) -> <a href="./src/outline/types/attachment_create_response.py">AttachmentCreateResponse</a></code>
- <code title="post /attachments.delete">client.attachments.<a href="./src/outline/resources/attachments.py">delete</a>(\*\*<a href="src/outline/types/attachment_delete_params.py">params</a>) -> <a href="./src/outline/types/attachment_delete_response.py">AttachmentDeleteResponse</a></code>
- <code title="post /attachments.redirect">client.attachments.<a href="./src/outline/resources/attachments.py">redirect</a>(\*\*<a href="src/outline/types/attachment_redirect_params.py">params</a>) -> None</code>

# Auth

Types:

```python
from outline.types import Auth, AuthConfigResponse, AuthInfoResponse
```

Methods:

- <code title="post /auth.config">client.auth.<a href="./src/outline/resources/auth.py">config</a>() -> <a href="./src/outline/types/auth_config_response.py">AuthConfigResponse</a></code>
- <code title="post /auth.info">client.auth.<a href="./src/outline/resources/auth.py">info</a>() -> <a href="./src/outline/types/auth_info_response.py">AuthInfoResponse</a></code>

# Collections

Types:

```python
from outline.types import (
    Collection,
    CollectionCreateResponse,
    CollectionRetrieveResponse,
    CollectionUpdateResponse,
    CollectionListResponse,
    CollectionDeleteResponse,
    CollectionAddGroupResponse,
    CollectionAddUserResponse,
    CollectionDocumentsResponse,
    CollectionExportResponse,
    CollectionExportAllResponse,
    CollectionRemoveGroupResponse,
    CollectionRemoveUserResponse,
)
```

Methods:

- <code title="post /collections.create">client.collections.<a href="./src/outline/resources/collections/collections.py">create</a>(\*\*<a href="src/outline/types/collection_create_params.py">params</a>) -> <a href="./src/outline/types/collection_create_response.py">CollectionCreateResponse</a></code>
- <code title="post /collections.info">client.collections.<a href="./src/outline/resources/collections/collections.py">retrieve</a>(\*\*<a href="src/outline/types/collection_retrieve_params.py">params</a>) -> <a href="./src/outline/types/collection_retrieve_response.py">CollectionRetrieveResponse</a></code>
- <code title="post /collections.update">client.collections.<a href="./src/outline/resources/collections/collections.py">update</a>(\*\*<a href="src/outline/types/collection_update_params.py">params</a>) -> <a href="./src/outline/types/collection_update_response.py">CollectionUpdateResponse</a></code>
- <code title="post /collections.list">client.collections.<a href="./src/outline/resources/collections/collections.py">list</a>(\*\*<a href="src/outline/types/collection_list_params.py">params</a>) -> <a href="./src/outline/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="post /collections.delete">client.collections.<a href="./src/outline/resources/collections/collections.py">delete</a>(\*\*<a href="src/outline/types/collection_delete_params.py">params</a>) -> <a href="./src/outline/types/collection_delete_response.py">CollectionDeleteResponse</a></code>
- <code title="post /collections.add_group">client.collections.<a href="./src/outline/resources/collections/collections.py">add_group</a>(\*\*<a href="src/outline/types/collection_add_group_params.py">params</a>) -> <a href="./src/outline/types/collection_add_group_response.py">CollectionAddGroupResponse</a></code>
- <code title="post /collections.add_user">client.collections.<a href="./src/outline/resources/collections/collections.py">add_user</a>(\*\*<a href="src/outline/types/collection_add_user_params.py">params</a>) -> <a href="./src/outline/types/collection_add_user_response.py">CollectionAddUserResponse</a></code>
- <code title="post /collections.documents">client.collections.<a href="./src/outline/resources/collections/collections.py">documents</a>(\*\*<a href="src/outline/types/collection_documents_params.py">params</a>) -> <a href="./src/outline/types/collection_documents_response.py">CollectionDocumentsResponse</a></code>
- <code title="post /collections.export">client.collections.<a href="./src/outline/resources/collections/collections.py">export</a>(\*\*<a href="src/outline/types/collection_export_params.py">params</a>) -> <a href="./src/outline/types/collection_export_response.py">CollectionExportResponse</a></code>
- <code title="post /collections.export_all">client.collections.<a href="./src/outline/resources/collections/collections.py">export_all</a>(\*\*<a href="src/outline/types/collection_export_all_params.py">params</a>) -> <a href="./src/outline/types/collection_export_all_response.py">CollectionExportAllResponse</a></code>
- <code title="post /collections.remove_group">client.collections.<a href="./src/outline/resources/collections/collections.py">remove_group</a>(\*\*<a href="src/outline/types/collection_remove_group_params.py">params</a>) -> <a href="./src/outline/types/collection_remove_group_response.py">CollectionRemoveGroupResponse</a></code>
- <code title="post /collections.remove_user">client.collections.<a href="./src/outline/resources/collections/collections.py">remove_user</a>(\*\*<a href="src/outline/types/collection_remove_user_params.py">params</a>) -> <a href="./src/outline/types/collection_remove_user_response.py">CollectionRemoveUserResponse</a></code>

## Memberships

Types:

```python
from outline.types.collections import MembershipListResponse
```

Methods:

- <code title="post /collections.memberships">client.collections.memberships.<a href="./src/outline/resources/collections/memberships.py">list</a>(\*\*<a href="src/outline/types/collections/membership_list_params.py">params</a>) -> <a href="./src/outline/types/collections/membership_list_response.py">MembershipListResponse</a></code>

## GroupMemberships

Types:

```python
from outline.types.collections import GroupMembershipListResponse
```

Methods:

- <code title="post /collections.group_memberships">client.collections.group_memberships.<a href="./src/outline/resources/collections/group_memberships.py">list</a>(\*\*<a href="src/outline/types/collections/group_membership_list_params.py">params</a>) -> <a href="./src/outline/types/collections/group_membership_list_response.py">GroupMembershipListResponse</a></code>

# Comments

Types:

```python
from outline.types import (
    Comment,
    CommentCreateResponse,
    CommentUpdateResponse,
    CommentListResponse,
    CommentDeleteResponse,
)
```

Methods:

- <code title="post /comments.create">client.comments.<a href="./src/outline/resources/comments.py">create</a>(\*\*<a href="src/outline/types/comment_create_params.py">params</a>) -> <a href="./src/outline/types/comment_create_response.py">CommentCreateResponse</a></code>
- <code title="post /comments.update">client.comments.<a href="./src/outline/resources/comments.py">update</a>(\*\*<a href="src/outline/types/comment_update_params.py">params</a>) -> <a href="./src/outline/types/comment_update_response.py">CommentUpdateResponse</a></code>
- <code title="post /comments.list">client.comments.<a href="./src/outline/resources/comments.py">list</a>(\*\*<a href="src/outline/types/comment_list_params.py">params</a>) -> <a href="./src/outline/types/comment_list_response.py">CommentListResponse</a></code>
- <code title="post /comments.delete">client.comments.<a href="./src/outline/resources/comments.py">delete</a>(\*\*<a href="src/outline/types/comment_delete_params.py">params</a>) -> <a href="./src/outline/types/comment_delete_response.py">CommentDeleteResponse</a></code>

# Documents

Types:

```python
from outline.types import (
    Document,
    DocumentCreateResponse,
    DocumentUpdateResponse,
    DocumentListResponse,
    DocumentDeleteResponse,
    DocumentArchiveResponse,
    DocumentDraftsResponse,
    DocumentExportResponse,
    DocumentImportResponse,
    DocumentInfoResponse,
    DocumentMoveResponse,
    DocumentRestoreResponse,
    DocumentSearchResponse,
    DocumentStarResponse,
    DocumentTemplatizeResponse,
    DocumentUnpublishResponse,
    DocumentUnstarResponse,
    DocumentViewedResponse,
)
```

Methods:

- <code title="post /documents.create">client.documents.<a href="./src/outline/resources/documents.py">create</a>(\*\*<a href="src/outline/types/document_create_params.py">params</a>) -> <a href="./src/outline/types/document_create_response.py">DocumentCreateResponse</a></code>
- <code title="post /documents.update">client.documents.<a href="./src/outline/resources/documents.py">update</a>(\*\*<a href="src/outline/types/document_update_params.py">params</a>) -> <a href="./src/outline/types/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="post /documents.list">client.documents.<a href="./src/outline/resources/documents.py">list</a>(\*\*<a href="src/outline/types/document_list_params.py">params</a>) -> <a href="./src/outline/types/document_list_response.py">DocumentListResponse</a></code>
- <code title="post /documents.delete">client.documents.<a href="./src/outline/resources/documents.py">delete</a>(\*\*<a href="src/outline/types/document_delete_params.py">params</a>) -> <a href="./src/outline/types/document_delete_response.py">DocumentDeleteResponse</a></code>
- <code title="post /documents.archive">client.documents.<a href="./src/outline/resources/documents.py">archive</a>(\*\*<a href="src/outline/types/document_archive_params.py">params</a>) -> <a href="./src/outline/types/document_archive_response.py">DocumentArchiveResponse</a></code>
- <code title="post /documents.drafts">client.documents.<a href="./src/outline/resources/documents.py">drafts</a>(\*\*<a href="src/outline/types/document_drafts_params.py">params</a>) -> <a href="./src/outline/types/document_drafts_response.py">DocumentDraftsResponse</a></code>
- <code title="post /documents.export">client.documents.<a href="./src/outline/resources/documents.py">export</a>(\*\*<a href="src/outline/types/document_export_params.py">params</a>) -> <a href="./src/outline/types/document_export_response.py">DocumentExportResponse</a></code>
- <code title="post /documents.import">client.documents.<a href="./src/outline/resources/documents.py">import\_</a>(\*\*<a href="src/outline/types/document_import_params.py">params</a>) -> <a href="./src/outline/types/document_import_response.py">DocumentImportResponse</a></code>
- <code title="post /documents.info">client.documents.<a href="./src/outline/resources/documents.py">info</a>(\*\*<a href="src/outline/types/document_info_params.py">params</a>) -> <a href="./src/outline/types/document_info_response.py">DocumentInfoResponse</a></code>
- <code title="post /documents.move">client.documents.<a href="./src/outline/resources/documents.py">move</a>(\*\*<a href="src/outline/types/document_move_params.py">params</a>) -> <a href="./src/outline/types/document_move_response.py">DocumentMoveResponse</a></code>
- <code title="post /documents.restore">client.documents.<a href="./src/outline/resources/documents.py">restore</a>(\*\*<a href="src/outline/types/document_restore_params.py">params</a>) -> <a href="./src/outline/types/document_restore_response.py">DocumentRestoreResponse</a></code>
- <code title="post /documents.search">client.documents.<a href="./src/outline/resources/documents.py">search</a>(\*\*<a href="src/outline/types/document_search_params.py">params</a>) -> <a href="./src/outline/types/document_search_response.py">DocumentSearchResponse</a></code>
- <code title="post /documents.star">client.documents.<a href="./src/outline/resources/documents.py">star</a>(\*\*<a href="src/outline/types/document_star_params.py">params</a>) -> <a href="./src/outline/types/document_star_response.py">DocumentStarResponse</a></code>
- <code title="post /documents.templatize">client.documents.<a href="./src/outline/resources/documents.py">templatize</a>(\*\*<a href="src/outline/types/document_templatize_params.py">params</a>) -> <a href="./src/outline/types/document_templatize_response.py">DocumentTemplatizeResponse</a></code>
- <code title="post /documents.unpublish">client.documents.<a href="./src/outline/resources/documents.py">unpublish</a>(\*\*<a href="src/outline/types/document_unpublish_params.py">params</a>) -> <a href="./src/outline/types/document_unpublish_response.py">DocumentUnpublishResponse</a></code>
- <code title="post /documents.unstar">client.documents.<a href="./src/outline/resources/documents.py">unstar</a>(\*\*<a href="src/outline/types/document_unstar_params.py">params</a>) -> <a href="./src/outline/types/document_unstar_response.py">DocumentUnstarResponse</a></code>
- <code title="post /documents.viewed">client.documents.<a href="./src/outline/resources/documents.py">viewed</a>(\*\*<a href="src/outline/types/document_viewed_params.py">params</a>) -> <a href="./src/outline/types/document_viewed_response.py">DocumentViewedResponse</a></code>

# Events

Types:

```python
from outline.types import EventCreateResponse
```

Methods:

- <code title="post /events.list">client.events.<a href="./src/outline/resources/events.py">create</a>(\*\*<a href="src/outline/types/event_create_params.py">params</a>) -> <a href="./src/outline/types/event_create_response.py">EventCreateResponse</a></code>

# FileOperations

Types:

```python
from outline.types import (
    FileOperation,
    FileOperationListResponse,
    FileOperationDeleteResponse,
    FileOperationInfoResponse,
)
```

Methods:

- <code title="post /fileOperations.list">client.file_operations.<a href="./src/outline/resources/file_operations.py">list</a>(\*\*<a href="src/outline/types/file_operation_list_params.py">params</a>) -> <a href="./src/outline/types/file_operation_list_response.py">FileOperationListResponse</a></code>
- <code title="post /fileOperations.delete">client.file_operations.<a href="./src/outline/resources/file_operations.py">delete</a>(\*\*<a href="src/outline/types/file_operation_delete_params.py">params</a>) -> <a href="./src/outline/types/file_operation_delete_response.py">FileOperationDeleteResponse</a></code>
- <code title="post /fileOperations.info">client.file_operations.<a href="./src/outline/resources/file_operations.py">info</a>(\*\*<a href="src/outline/types/file_operation_info_params.py">params</a>) -> <a href="./src/outline/types/file_operation_info_response.py">FileOperationInfoResponse</a></code>
- <code title="post /fileOperations.redirect">client.file_operations.<a href="./src/outline/resources/file_operations.py">redirect</a>(\*\*<a href="src/outline/types/file_operation_redirect_params.py">params</a>) -> BinaryAPIResponse</code>

# Groups

Types:

```python
from outline.types import (
    Group,
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupDeleteResponse,
    GroupInfoResponse,
)
```

Methods:

- <code title="post /groups.create">client.groups.<a href="./src/outline/resources/groups.py">create</a>(\*\*<a href="src/outline/types/group_create_params.py">params</a>) -> <a href="./src/outline/types/group_create_response.py">GroupCreateResponse</a></code>
- <code title="post /groups.update">client.groups.<a href="./src/outline/resources/groups.py">update</a>(\*\*<a href="src/outline/types/group_update_params.py">params</a>) -> <a href="./src/outline/types/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="post /groups.list">client.groups.<a href="./src/outline/resources/groups.py">list</a>(\*\*<a href="src/outline/types/group_list_params.py">params</a>) -> <a href="./src/outline/types/group_list_response.py">GroupListResponse</a></code>
- <code title="post /groups.delete">client.groups.<a href="./src/outline/resources/groups.py">delete</a>(\*\*<a href="src/outline/types/group_delete_params.py">params</a>) -> <a href="./src/outline/types/group_delete_response.py">GroupDeleteResponse</a></code>
- <code title="post /groups.info">client.groups.<a href="./src/outline/resources/groups.py">info</a>(\*\*<a href="src/outline/types/group_info_params.py">params</a>) -> <a href="./src/outline/types/group_info_response.py">GroupInfoResponse</a></code>
