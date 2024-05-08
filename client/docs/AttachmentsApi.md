# swagger_client.AttachmentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_create_post**](AttachmentsApi.md#attachments_create_post) | **POST** /attachments.create | Create an attachment
[**attachments_delete_post**](AttachmentsApi.md#attachments_delete_post) | **POST** /attachments.delete | Delete an attachment
[**attachments_redirect_post**](AttachmentsApi.md#attachments_redirect_post) | **POST** /attachments.redirect | Retrieve an attachment

# **attachments_create_post**
> InlineResponse200 attachments_create_post(body=body)

Create an attachment

Creating an attachment object creates a database record and returns the inputs needed to generate a signed url and upload the file from the client to cloud storage.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttachmentsCreateBody() # AttachmentsCreateBody |  (optional)

try:
    # Create an attachment
    api_response = api_instance.attachments_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->attachments_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachmentsCreateBody**](AttachmentsCreateBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_delete_post**
> InlineResponse2001 attachments_delete_post(body=body)

Delete an attachment

Deleting an attachment is permanant. It will not delete references or links to the attachment that may exist in your documents.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttachmentsDeleteBody() # AttachmentsDeleteBody |  (optional)

try:
    # Delete an attachment
    api_response = api_instance.attachments_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->attachments_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachmentsDeleteBody**](AttachmentsDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_redirect_post**
> attachments_redirect_post(body=body)

Retrieve an attachment

Load an attachment from where it is stored based on the id. If the attachment is private then a temporary, signed url with embedded credentials is generated on demand.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.AttachmentsRedirectBody() # AttachmentsRedirectBody |  (optional)

try:
    # Retrieve an attachment
    api_instance.attachments_redirect_post(body=body)
except ApiException as e:
    print("Exception when calling AttachmentsApi->attachments_redirect_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttachmentsRedirectBody**](AttachmentsRedirectBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

