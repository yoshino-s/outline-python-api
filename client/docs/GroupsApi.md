# swagger_client.GroupsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_add_user_post**](GroupsApi.md#groups_add_user_post) | **POST** /groups.add_user | Add a group member
[**groups_create_post**](GroupsApi.md#groups_create_post) | **POST** /groups.create | Create a group
[**groups_delete_post**](GroupsApi.md#groups_delete_post) | **POST** /groups.delete | Delete a group
[**groups_info_post**](GroupsApi.md#groups_info_post) | **POST** /groups.info | Retrieve a group
[**groups_list_post**](GroupsApi.md#groups_list_post) | **POST** /groups.list | List all groups
[**groups_memberships_post**](GroupsApi.md#groups_memberships_post) | **POST** /groups.memberships | List all group members
[**groups_remove_user_post**](GroupsApi.md#groups_remove_user_post) | **POST** /groups.remove_user | Remove a group member
[**groups_update_post**](GroupsApi.md#groups_update_post) | **POST** /groups.update | Update a group

# **groups_add_user_post**
> InlineResponse20028 groups_add_user_post(body=body)

Add a group member

This method allows you to add a user to the specified group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsAddUserBody() # GroupsAddUserBody |  (optional)

try:
    # Add a group member
    api_response = api_instance.groups_add_user_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_add_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsAddUserBody**](GroupsAddUserBody.md)|  | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_create_post**
> InlineResponse20026 groups_create_post(body=body)

Create a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsCreateBody() # GroupsCreateBody |  (optional)

try:
    # Create a group
    api_response = api_instance.groups_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsCreateBody**](GroupsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_delete_post**
> InlineResponse2001 groups_delete_post(body=body)

Delete a group

Deleting a group will cause all of its members to lose access to any collections the group has previously been added to. This action can’t be undone so please be careful.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsDeleteBody() # GroupsDeleteBody |  (optional)

try:
    # Delete a group
    api_response = api_instance.groups_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsDeleteBody**](GroupsDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_info_post**
> InlineResponse20024 groups_info_post(body=body)

Retrieve a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsInfoBody() # GroupsInfoBody |  (optional)

try:
    # Retrieve a group
    api_response = api_instance.groups_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsInfoBody**](GroupsInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_list_post**
> InlineResponse20025 groups_list_post(body=body)

List all groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsListBody() # GroupsListBody |  (optional)

try:
    # List all groups
    api_response = api_instance.groups_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsListBody**](GroupsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_memberships_post**
> InlineResponse20027 groups_memberships_post(body=body)

List all group members

List and filter all the members in a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsMembershipsBody() # GroupsMembershipsBody |  (optional)

try:
    # List all group members
    api_response = api_instance.groups_memberships_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_memberships_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsMembershipsBody**](GroupsMembershipsBody.md)|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_remove_user_post**
> InlineResponse20029 groups_remove_user_post(body=body)

Remove a group member

This method allows you to remove a user from the group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsRemoveUserBody() # GroupsRemoveUserBody |  (optional)

try:
    # Remove a group member
    api_response = api_instance.groups_remove_user_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_remove_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsRemoveUserBody**](GroupsRemoveUserBody.md)|  | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_update_post**
> InlineResponse20026 groups_update_post(body=body)

Update a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.GroupsUpdateBody() # GroupsUpdateBody |  (optional)

try:
    # Update a group
    api_response = api_instance.groups_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->groups_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsUpdateBody**](GroupsUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

