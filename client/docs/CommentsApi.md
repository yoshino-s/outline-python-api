# swagger_client.CommentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_create_post**](CommentsApi.md#comments_create_post) | **POST** /comments.create | Create a comment
[**comments_delete_post**](CommentsApi.md#comments_delete_post) | **POST** /comments.delete | Delete a comment
[**comments_list_post**](CommentsApi.md#comments_list_post) | **POST** /comments.list | List all comments
[**comments_update_post**](CommentsApi.md#comments_update_post) | **POST** /comments.update | Update a comment

# **comments_create_post**
> InlineResponse20013 comments_create_post(body=body)

Create a comment

Create a comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentsCreateBody() # CommentsCreateBody |  (optional)

try:
    # Create a comment
    api_response = api_instance.comments_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->comments_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentsCreateBody**](CommentsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_delete_post**
> InlineResponse2001 comments_delete_post(body=body)

Delete a comment

Delete a comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentsDeleteBody() # CommentsDeleteBody |  (optional)

try:
    # Delete a comment
    api_response = api_instance.comments_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->comments_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentsDeleteBody**](CommentsDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_list_post**
> InlineResponse20014 comments_list_post(body=body)

List all comments

This method will list all comments matching the given properties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentsListBody() # CommentsListBody |  (optional)

try:
    # List all comments
    api_response = api_instance.comments_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->comments_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentsListBody**](CommentsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_update_post**
> InlineResponse20013 comments_update_post(body=body)

Update a comment

Update a comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.CommentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CommentsUpdateBody() # CommentsUpdateBody |  (optional)

try:
    # Update a comment
    api_response = api_instance.comments_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->comments_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CommentsUpdateBody**](CommentsUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

