# swagger_client.SharesApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shares_create_post**](SharesApi.md#shares_create_post) | **POST** /shares.create | Create a share
[**shares_info_post**](SharesApi.md#shares_info_post) | **POST** /shares.info | Retrieve a share object
[**shares_list_post**](SharesApi.md#shares_list_post) | **POST** /shares.list | List all shares
[**shares_revoke_post**](SharesApi.md#shares_revoke_post) | **POST** /shares.revoke | Revoke a share
[**shares_update_post**](SharesApi.md#shares_update_post) | **POST** /shares.update | Update a share

# **shares_create_post**
> InlineResponse20032 shares_create_post(body=body)

Create a share

Creates a new share link that can be used by to access a document. If you request multiple shares for the same document with the same API key, the same share object will be returned. By default all shares are unpublished.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SharesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharesCreateBody() # SharesCreateBody |  (optional)

try:
    # Create a share
    api_response = api_instance.shares_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharesApi->shares_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesCreateBody**](SharesCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_info_post**
> InlineResponse20032 shares_info_post(body=body)

Retrieve a share object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SharesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharesInfoBody() # SharesInfoBody |  (optional)

try:
    # Retrieve a share object
    api_response = api_instance.shares_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharesApi->shares_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesInfoBody**](SharesInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_list_post**
> InlineResponse20033 shares_list_post(body=body)

List all shares

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SharesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharesListBody() # SharesListBody |  (optional)

try:
    # List all shares
    api_response = api_instance.shares_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharesApi->shares_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesListBody**](SharesListBody.md)|  | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_revoke_post**
> InlineResponse2001 shares_revoke_post(body=body)

Revoke a share

Makes the share link inactive so that it can no longer be used to access the document.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SharesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharesRevokeBody() # SharesRevokeBody |  (optional)

try:
    # Revoke a share
    api_response = api_instance.shares_revoke_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharesApi->shares_revoke_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesRevokeBody**](SharesRevokeBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_update_post**
> InlineResponse20032 shares_update_post(body=body)

Update a share

Allows changing an existing shares published status, which removes authentication and makes it available to anyone with the link.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.SharesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SharesUpdateBody() # SharesUpdateBody |  (optional)

try:
    # Update a share
    api_response = api_instance.shares_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharesApi->shares_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SharesUpdateBody**](SharesUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

