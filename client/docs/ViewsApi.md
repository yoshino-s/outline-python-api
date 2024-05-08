# swagger_client.ViewsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**views_create_post**](ViewsApi.md#views_create_post) | **POST** /views.create | Create a view
[**views_list_post**](ViewsApi.md#views_list_post) | **POST** /views.list | List all views

# **views_create_post**
> InlineResponse20038 views_create_post(body=body)

Create a view

Creates a new view for a document. This is documented in the interests of thoroughness however it is recommended that views are not created from outside of the Outline UI.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ViewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ViewsCreateBody() # ViewsCreateBody |  (optional)

try:
    # Create a view
    api_response = api_instance.views_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->views_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ViewsCreateBody**](ViewsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **views_list_post**
> InlineResponse20037 views_list_post(body=body)

List all views

List all users that have viewed a document and the overall view count.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ViewsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ViewsListBody() # ViewsListBody |  (optional)

try:
    # List all views
    api_response = api_instance.views_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ViewsApi->views_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ViewsListBody**](ViewsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

