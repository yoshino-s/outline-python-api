# swagger_client.CollectionsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_add_group_post**](CollectionsApi.md#collections_add_group_post) | **POST** /collections.add_group | Add a group to a collection
[**collections_add_user_post**](CollectionsApi.md#collections_add_user_post) | **POST** /collections.add_user | Add a collection user
[**collections_create_post**](CollectionsApi.md#collections_create_post) | **POST** /collections.create | Create a collection
[**collections_delete_post**](CollectionsApi.md#collections_delete_post) | **POST** /collections.delete | Delete a collection
[**collections_documents_post**](CollectionsApi.md#collections_documents_post) | **POST** /collections.documents | Retrieve a collections document structure
[**collections_export_all_post**](CollectionsApi.md#collections_export_all_post) | **POST** /collections.export_all | Export all collections
[**collections_export_post**](CollectionsApi.md#collections_export_post) | **POST** /collections.export | Export a collection
[**collections_group_memberships_post**](CollectionsApi.md#collections_group_memberships_post) | **POST** /collections.group_memberships | List all collection group members
[**collections_info_post**](CollectionsApi.md#collections_info_post) | **POST** /collections.info | Retrieve a collection
[**collections_list_post**](CollectionsApi.md#collections_list_post) | **POST** /collections.list | List all collections
[**collections_memberships_post**](CollectionsApi.md#collections_memberships_post) | **POST** /collections.memberships | List all collection memberships
[**collections_remove_group_post**](CollectionsApi.md#collections_remove_group_post) | **POST** /collections.remove_group | Remove a collection group
[**collections_remove_user_post**](CollectionsApi.md#collections_remove_user_post) | **POST** /collections.remove_user | Remove a collection user
[**collections_update_post**](CollectionsApi.md#collections_update_post) | **POST** /collections.update | Update a collection

# **collections_add_group_post**
> InlineResponse20010 collections_add_group_post(body=body)

Add a group to a collection

This method allows you to give all members in a group access to a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsAddGroupBody() # CollectionsAddGroupBody |  (optional)

try:
    # Add a group to a collection
    api_response = api_instance.collections_add_group_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_add_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsAddGroupBody**](CollectionsAddGroupBody.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_add_user_post**
> InlineResponse2008 collections_add_user_post(body=body)

Add a collection user

This method allows you to add a user membership to the specified collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsAddUserBody() # CollectionsAddUserBody |  (optional)

try:
    # Add a collection user
    api_response = api_instance.collections_add_user_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_add_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsAddUserBody**](CollectionsAddUserBody.md)|  | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_create_post**
> InlineResponse2007 collections_create_post(body=body)

Create a collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsCreateBody() # CollectionsCreateBody |  (optional)

try:
    # Create a collection
    api_response = api_instance.collections_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsCreateBody**](CollectionsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_delete_post**
> InlineResponse2001 collections_delete_post(body=body)

Delete a collection

Delete a collection and all of its documents. This action can’t be undone so please be careful.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsDeleteBody() # CollectionsDeleteBody |  (optional)

try:
    # Delete a collection
    api_response = api_instance.collections_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsDeleteBody**](CollectionsDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_documents_post**
> InlineResponse2005 collections_documents_post(body=body)

Retrieve a collections document structure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsDocumentsBody() # CollectionsDocumentsBody |  (optional)

try:
    # Retrieve a collections document structure
    api_response = api_instance.collections_documents_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_documents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsDocumentsBody**](CollectionsDocumentsBody.md)|  | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_export_all_post**
> InlineResponse20012 collections_export_all_post(body=body)

Export all collections

Triggers a bulk export of all documents in and their attachments. The endpoint returns a `FileOperation` that can be queried through the fileOperations endpoint to track the progress of the export and get the url for the final file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsExportAllBody() # CollectionsExportAllBody |  (optional)

try:
    # Export all collections
    api_response = api_instance.collections_export_all_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_export_all_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsExportAllBody**](CollectionsExportAllBody.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_export_post**
> InlineResponse20012 collections_export_post(body=body)

Export a collection

Triggers a bulk export of the collection in markdown format and their attachments. If documents are nested then they will be nested in folders inside the zip file. The endpoint returns a `FileOperation` that can be queried to track the progress of the export and get the url for the final file.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsExportBody() # CollectionsExportBody |  (optional)

try:
    # Export a collection
    api_response = api_instance.collections_export_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_export_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsExportBody**](CollectionsExportBody.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_group_memberships_post**
> InlineResponse20011 collections_group_memberships_post(body=body)

List all collection group members

This method allows you to list a collections group memberships. This is the list of groups that have been given access to the collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsGroupMembershipsBody() # CollectionsGroupMembershipsBody |  (optional)

try:
    # List all collection group members
    api_response = api_instance.collections_group_memberships_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_group_memberships_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsGroupMembershipsBody**](CollectionsGroupMembershipsBody.md)|  | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_info_post**
> InlineResponse2004 collections_info_post(body=body)

Retrieve a collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsInfoBody() # CollectionsInfoBody |  (optional)

try:
    # Retrieve a collection
    api_response = api_instance.collections_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsInfoBody**](CollectionsInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_list_post**
> InlineResponse2006 collections_list_post(body=body)

List all collections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pagination() # Pagination |  (optional)

try:
    # List all collections
    api_response = api_instance.collections_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pagination**](Pagination.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_memberships_post**
> InlineResponse2009 collections_memberships_post(body=body)

List all collection memberships

This method allows you to list a collections individual memberships. It's important to note that memberships returned from this endpoint do not include group memberships.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsMembershipsBody() # CollectionsMembershipsBody |  (optional)

try:
    # List all collection memberships
    api_response = api_instance.collections_memberships_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_memberships_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsMembershipsBody**](CollectionsMembershipsBody.md)|  | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_remove_group_post**
> InlineResponse2001 collections_remove_group_post(body=body)

Remove a collection group

This method allows you to revoke all members in a group access to a collection. Note that members of the group may still retain access through other groups or individual memberships.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsRemoveGroupBody() # CollectionsRemoveGroupBody |  (optional)

try:
    # Remove a collection group
    api_response = api_instance.collections_remove_group_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_remove_group_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsRemoveGroupBody**](CollectionsRemoveGroupBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_remove_user_post**
> InlineResponse2001 collections_remove_user_post(body=body)

Remove a collection user

This method allows you to remove a user from the specified collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsRemoveUserBody() # CollectionsRemoveUserBody |  (optional)

try:
    # Remove a collection user
    api_response = api_instance.collections_remove_user_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_remove_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsRemoveUserBody**](CollectionsRemoveUserBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_update_post**
> InlineResponse2007 collections_update_post(body=body)

Update a collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CollectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CollectionsUpdateBody() # CollectionsUpdateBody |  (optional)

try:
    # Update a collection
    api_response = api_instance.collections_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsUpdateBody**](CollectionsUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

