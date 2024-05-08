# swagger_client.UsersApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_activate_post**](UsersApi.md#users_activate_post) | **POST** /users.activate | Activate a user
[**users_delete_post**](UsersApi.md#users_delete_post) | **POST** /users.delete | Delete a user
[**users_info_post**](UsersApi.md#users_info_post) | **POST** /users.info | Retrieve a user
[**users_invite_post**](UsersApi.md#users_invite_post) | **POST** /users.invite | Invite users
[**users_list_post**](UsersApi.md#users_list_post) | **POST** /users.list | List all users
[**users_suspend_post**](UsersApi.md#users_suspend_post) | **POST** /users.suspend | Suspend a user
[**users_update_post**](UsersApi.md#users_update_post) | **POST** /users.update | Update a user
[**users_update_role_post**](UsersApi.md#users_update_role_post) | **POST** /users.update_role | Change a users role

# **users_activate_post**
> InlineResponse20035 users_activate_post(body=body)

Activate a user

Activating a previously suspended user allows them to signin again. Users that are activated will cause billing totals to be re-calculated in the hosted version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersActivateBody() # UsersActivateBody |  (optional)

try:
    # Activate a user
    api_response = api_instance.users_activate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_activate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersActivateBody**](UsersActivateBody.md)|  | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_post**
> InlineResponse2001 users_delete_post(body=body)

Delete a user

Deleting a user removes the object entirely. In almost every circumstance it is preferable to suspend a user, as a deleted user can be recreated by signing in with SSO again.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersDeleteBody() # UsersDeleteBody |  (optional)

try:
    # Delete a user
    api_response = api_instance.users_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersDeleteBody**](UsersDeleteBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_info_post**
> InlineResponse20035 users_info_post(body=body)

Retrieve a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersInfoBody() # UsersInfoBody |  (optional)

try:
    # Retrieve a user
    api_response = api_instance.users_info_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersInfoBody**](UsersInfoBody.md)|  | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_invite_post**
> InlineResponse20034 users_invite_post(body=body)

Invite users

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersInviteBody() # UsersInviteBody |  (optional)

try:
    # Invite users
    api_response = api_instance.users_invite_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_invite_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersInviteBody**](UsersInviteBody.md)|  | [optional] 

### Return type

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_post**
> InlineResponse20036 users_list_post(body=body)

List all users

List and filter all the users in the team

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersListBody() # UsersListBody |  (optional)

try:
    # List all users
    api_response = api_instance.users_list_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersListBody**](UsersListBody.md)|  | [optional] 

### Return type

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_suspend_post**
> InlineResponse20035 users_suspend_post(body=body)

Suspend a user

Suspending a user prevents the user from signing in. Users that are suspended are also not counted against billing totals in the hosted version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersSuspendBody() # UsersSuspendBody |  (optional)

try:
    # Suspend a user
    api_response = api_instance.users_suspend_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_suspend_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersSuspendBody**](UsersSuspendBody.md)|  | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_post**
> InlineResponse20035 users_update_post(body=body)

Update a user

Update a users name or avatar. If no `id` is passed then the user associated with the authentication will be updated by default.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersUpdateBody() # UsersUpdateBody |  (optional)

try:
    # Update a user
    api_response = api_instance.users_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersUpdateBody**](UsersUpdateBody.md)|  | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_role_post**
> InlineResponse20035 users_update_role_post(body=body)

Change a users role

Change the role of a user, only available to admin authorization.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UsersUpdateRoleBody() # UsersUpdateRoleBody |  (optional)

try:
    # Change a users role
    api_response = api_instance.users_update_role_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update_role_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersUpdateRoleBody**](UsersUpdateRoleBody.md)|  | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

