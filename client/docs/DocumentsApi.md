# swagger_client.DocumentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_archive_post**](DocumentsApi.md#documents_archive_post) | **POST** /documents.archive | Archive a document
[**documents_create_post**](DocumentsApi.md#documents_create_post) | **POST** /documents.create | Create a document
[**documents_delete_post**](DocumentsApi.md#documents_delete_post) | **POST** /documents.delete | Delete a document
[**documents_drafts_post**](DocumentsApi.md#documents_drafts_post) | **POST** /documents.drafts | List all draft documents
[**documents_export_post**](DocumentsApi.md#documents_export_post) | **POST** /documents.export | Export a document as markdown
[**documents_import_post**](DocumentsApi.md#documents_import_post) | **POST** /documents.import | Import a file as a document
[**documents_info_post**](DocumentsApi.md#documents_info_post) | **POST** /documents.info | Retrieve a document
[**documents_list_post**](DocumentsApi.md#documents_list_post) | **POST** /documents.list | List all documents
[**documents_move_post**](DocumentsApi.md#documents_move_post) | **POST** /documents.move | Move a document
[**documents_restore_post**](DocumentsApi.md#documents_restore_post) | **POST** /documents.restore | Restore a document
[**documents_search_post**](DocumentsApi.md#documents_search_post) | **POST** /documents.search | Search all documents
[**documents_star_post**](DocumentsApi.md#documents_star_post) | **POST** /documents.star | Star a document
[**documents_templatize_post**](DocumentsApi.md#documents_templatize_post) | **POST** /documents.templatize | Create a template from a document
[**documents_unpublish_post**](DocumentsApi.md#documents_unpublish_post) | **POST** /documents.unpublish | Unpublish a document
[**documents_unstar_post**](DocumentsApi.md#documents_unstar_post) | **POST** /documents.unstar | Unstar a document
[**documents_update_post**](DocumentsApi.md#documents_update_post) | **POST** /documents.update | Update a document
[**documents_viewed_post**](DocumentsApi.md#documents_viewed_post) | **POST** /documents.viewed | List all recently viewed documents

# **documents_archive_post**
> InlineResponse20018 documents_archive_post(body=body)

Archive a document

Archiving a document allows outdated information to be moved out of sight whilst retaining the ability to optionally search and restore it later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsArchiveBody() # DocumentsArchiveBody |  (optional)

try:
    # Archive a document
    api_response = api_instance.documents_archive_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_archive_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsArchiveBody**](DocumentsArchiveBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_create_post**
> InlineResponse20018 documents_create_post(body=body)

Create a document

This method allows you to create or publish a new document. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsCreateBody() # DocumentsCreateBody |  (optional)

try:
    # Create a document
    api_response = api_instance.documents_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsCreateBody**](DocumentsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_delete_post**
> InlineResponse2001 documents_delete_post(body=body)

Delete a document

Deleting a document moves it to the trash. If not restored within 30 days it is permenantly deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsDeleteBody() # DocumentsDeleteBody |  (optional)

try:
    # Delete a document
    api_response = api_instance.documents_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsDeleteBody**](DocumentsDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_drafts_post**
> InlineResponse20014 documents_drafts_post(body=body)

List all draft documents

This method will list all draft documents belonging to the current user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsDraftsBody() # DocumentsDraftsBody |  (optional)

try:
    # List all draft documents
    api_response = api_instance.documents_drafts_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_drafts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsDraftsBody**](DocumentsDraftsBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_export_post**
> InlineResponse20016 documents_export_post(body=body)

Export a document as markdown

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsExportBody() # DocumentsExportBody |  (optional)

try:
    # Export a document as markdown
    api_response = api_instance.documents_export_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsExportBody**](DocumentsExportBody.md)|  | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_import_post**
> InlineResponse20015 documents_import_post(file=file, collection_id=collection_id, parent_document_id=parent_document_id, template=template, publish=publish)

Import a file as a document

This method allows you to create a new document by importing an existing file. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
file = NULL # object |  (optional)
collection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
parent_document_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
template = true # bool |  (optional)
publish = true # bool |  (optional)

try:
    # Import a file as a document
    api_response = api_instance.documents_import_post(file=file, collection_id=collection_id, parent_document_id=parent_document_id, template=template, publish=publish)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_import_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](.md)|  | [optional] 
 **collection_id** | [**str**](.md)|  | [optional] 
 **parent_document_id** | [**str**](.md)|  | [optional] 
 **template** | **bool**|  | [optional] 
 **publish** | **bool**|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_info_post**
> InlineResponse20015 documents_info_post(body=body)

Retrieve a document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsInfoBody() # DocumentsInfoBody |  (optional)

try:
    # Retrieve a document
    api_response = api_instance.documents_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsInfoBody**](DocumentsInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_list_post**
> InlineResponse20014 documents_list_post(body=body)

List all documents

This method will list all published documents and draft documents belonging to the current user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsListBody() # DocumentsListBody |  (optional)

try:
    # List all documents
    api_response = api_instance.documents_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsListBody**](DocumentsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_move_post**
> InlineResponse20020 documents_move_post(body=body)

Move a document

Move a document to a new location or collection. If no parent document is provided, the document will be moved to the collection root.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsMoveBody() # DocumentsMoveBody |  (optional)

try:
    # Move a document
    api_response = api_instance.documents_move_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_move_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsMoveBody**](DocumentsMoveBody.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_restore_post**
> InlineResponse20018 documents_restore_post(body=body)

Restore a document

If a document has been archived or deleted, it can be restored. Optionally a revision can be passed to restore the document to a previous point in time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsRestoreBody() # DocumentsRestoreBody |  (optional)

try:
    # Restore a document
    api_response = api_instance.documents_restore_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_restore_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsRestoreBody**](DocumentsRestoreBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_search_post**
> InlineResponse20017 documents_search_post(body=body)

Search all documents

This methods allows you to search your teams documents with keywords. Note that search results will be restricted to those accessible by the current access token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsSearchBody() # DocumentsSearchBody |  (optional)

try:
    # Search all documents
    api_response = api_instance.documents_search_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_search_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsSearchBody**](DocumentsSearchBody.md)|  | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_star_post**
> InlineResponse20019 documents_star_post(body=body)

Star a document

Starring a document gives it extra priority in the UI and makes it easier to find important information later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsStarBody() # DocumentsStarBody |  (optional)

try:
    # Star a document
    api_response = api_instance.documents_star_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_star_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsStarBody**](DocumentsStarBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_templatize_post**
> InlineResponse20018 documents_templatize_post(body=body)

Create a template from a document

This method allows you to createa new template using an existing document as the basis

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsTemplatizeBody() # DocumentsTemplatizeBody |  (optional)

try:
    # Create a template from a document
    api_response = api_instance.documents_templatize_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_templatize_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsTemplatizeBody**](DocumentsTemplatizeBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_unpublish_post**
> InlineResponse20018 documents_unpublish_post(body=body)

Unpublish a document

Unpublishing a document moves it back to a draft status and out of the collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsUnpublishBody() # DocumentsUnpublishBody |  (optional)

try:
    # Unpublish a document
    api_response = api_instance.documents_unpublish_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_unpublish_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsUnpublishBody**](DocumentsUnpublishBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_unstar_post**
> InlineResponse20019 documents_unstar_post(body=body)

Unstar a document

Starring a document gives it extra priority in the UI and makes it easier to find important information later.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsUnstarBody() # DocumentsUnstarBody |  (optional)

try:
    # Unstar a document
    api_response = api_instance.documents_unstar_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_unstar_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsUnstarBody**](DocumentsUnstarBody.md)|  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_update_post**
> InlineResponse20018 documents_update_post(body=body)

Update a document

This method allows you to modify an already created document

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsUpdateBody() # DocumentsUpdateBody |  (optional)

try:
    # Update a document
    api_response = api_instance.documents_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsUpdateBody**](DocumentsUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_viewed_post**
> InlineResponse20014 documents_viewed_post(body=body)

List all recently viewed documents

This method will list all documents recently viewed by the current user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DocumentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.DocumentsViewedBody() # DocumentsViewedBody |  (optional)

try:
    # List all recently viewed documents
    api_response = api_instance.documents_viewed_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentsApi->documents_viewed_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentsViewedBody**](DocumentsViewedBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

