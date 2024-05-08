# swagger_client.EventsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_list_post**](EventsApi.md#events_list_post) | **POST** /events.list | List all events

# **events_list_post**
> InlineResponse20021 events_list_post(body=body)

List all events

Events are an audit trail of important events that happen in the knowledge base.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.EventsApi(swagger_client.ApiClient(configuration))
body = swagger_client.EventsListBody() # EventsListBody |  (optional)

try:
    # List all events
    api_response = api_instance.events_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->events_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventsListBody**](EventsListBody.md)|  | [optional] 

### Return type

[**InlineResponse20021**](InlineResponse20021.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

