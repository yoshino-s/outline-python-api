# swagger_client.RevisionsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revisions_info_post**](RevisionsApi.md#revisions_info_post) | **POST** /revisions.info | Retrieve a revision
[**revisions_list_post**](RevisionsApi.md#revisions_list_post) | **POST** /revisions.list | List all revisions

# **revisions_info_post**
> InlineResponse20030 revisions_info_post(body=body)

Retrieve a revision

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RevisionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RevisionsInfoBody() # RevisionsInfoBody |  (optional)

try:
    # Retrieve a revision
    api_response = api_instance.revisions_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevisionsApi->revisions_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevisionsInfoBody**](RevisionsInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revisions_list_post**
> InlineResponse20031 revisions_list_post(body=body)

List all revisions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.RevisionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RevisionsListBody() # RevisionsListBody |  (optional)

try:
    # List all revisions
    api_response = api_instance.revisions_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RevisionsApi->revisions_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RevisionsListBody**](RevisionsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

