# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] 
**name** | **str** | The name of this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary. | [optional] 
**avatar_url** | **str** | The URL for the image associated with this user, it will be displayed in the application UI and email notifications. | [optional] 
**email** | **str** | The email associated with this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary. | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**is_suspended** | **bool** | Whether this user has been suspended. | [optional] 
**last_active_at** | **datetime** | The last time this user made an API request, this value is updated at most every 5 minutes. | [optional] 
**created_at** | **datetime** | The date and time that this user first signed in or was invited as a guest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

