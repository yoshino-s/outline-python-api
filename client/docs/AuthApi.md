# swagger_client.AuthApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_config_post**](AuthApi.md#auth_config_post) | **POST** /auth.config | Retrieve auth config
[**auth_info_post**](AuthApi.md#auth_info_post) | **POST** /auth.info | Retrieve auth

# **auth_config_post**
> InlineResponse2003 auth_config_post()

Retrieve auth config

Retrieve authentication options

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve auth config
    api_response = api_instance.auth_config_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_config_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_info_post**
> InlineResponse2002 auth_info_post()

Retrieve auth

Retrieve authentication details for the current API key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))

try:
    # Retrieve auth
    api_response = api_instance.auth_info_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->auth_info_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

