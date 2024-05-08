# swagger_client.FileOperationsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_operations_delete_post**](FileOperationsApi.md#file_operations_delete_post) | **POST** /fileOperations.delete | Delete a file operation
[**file_operations_info_post**](FileOperationsApi.md#file_operations_info_post) | **POST** /fileOperations.info | Retrieve a file operation
[**file_operations_list_post**](FileOperationsApi.md#file_operations_list_post) | **POST** /fileOperations.list | List all file operations
[**file_operations_redirect_post**](FileOperationsApi.md#file_operations_redirect_post) | **POST** /fileOperations.redirect | Retrieve the file

# **file_operations_delete_post**
> InlineResponse2001 file_operations_delete_post(body=body)

Delete a file operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileOperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileOperationsDeleteBody() # FileOperationsDeleteBody |  (optional)

try:
    # Delete a file operation
    api_response = api_instance.file_operations_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileOperationsApi->file_operations_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileOperationsDeleteBody**](FileOperationsDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_operations_info_post**
> InlineResponse20022 file_operations_info_post(body=body)

Retrieve a file operation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileOperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileOperationsInfoBody() # FileOperationsInfoBody |  (optional)

try:
    # Retrieve a file operation
    api_response = api_instance.file_operations_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileOperationsApi->file_operations_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileOperationsInfoBody**](FileOperationsInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_operations_list_post**
> InlineResponse20023 file_operations_list_post(body=body)

List all file operations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileOperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileOperationsListBody() # FileOperationsListBody |  (optional)

try:
    # List all file operations
    api_response = api_instance.file_operations_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileOperationsApi->file_operations_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileOperationsListBody**](FileOperationsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_operations_redirect_post**
> str file_operations_redirect_post(body=body)

Retrieve the file

Load the resulting file from where it is stored based on the id. A temporary, signed url with embedded credentials is generated on demand.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.FileOperationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FileOperationsRedirectBody() # FileOperationsRedirectBody |  (optional)

try:
    # Retrieve the file
    api_response = api_instance.file_operations_redirect_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileOperationsApi->file_operations_redirect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileOperationsRedirectBody**](FileOperationsRedirectBody.md)|  | [optional] 

### Return type

**str**

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

