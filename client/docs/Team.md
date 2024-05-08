# Team

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] 
**name** | **str** | The name of this team, it is usually auto-generated when the first SSO connection is made but can be changed if neccessary. | [optional] 
**avatar_url** | **str** | The URL for the image associated with this team, it will be displayed in the team switcher and in the top left of the knowledge base along with the name. | [optional] 
**sharing** | **bool** | Whether this team has share links globally enabled. If this value is false then all sharing UI and APIs are disabled. | [optional] 
**default_collection_id** | **str** | If set then the referenced collection is where users will be redirected to after signing in instead of the Home screen | [optional] 
**default_user_role** | [**UserRole**](UserRole.md) |  | [optional] 
**member_collection_create** | **bool** | Whether members are allowed to create new collections. If false then only admins can create collections. | [optional] 
**document_embeds** | **bool** | Whether this team has embeds in documents globally enabled. It can be disabled to reduce potential data leakage to third parties. | [optional] 
**collaborative_editing** | **bool** | Whether this team has collaborative editing in documents globally enabled. | [optional] 
**invite_required** | **bool** | Whether an invite is required to join this team, if false users may join with a linked SSO provider. | [optional] 
**allowed_domains** | **list[str]** |  | [optional] 
**guest_signin** | **bool** | Whether this team has guest signin enabled. Guests can signin with an email address and are not required to have a Google Workspace/Slack SSO account once invited. | [optional] 
**subdomain** | **str** | Represents the subdomain at which this team&#x27;s knowledge base can be accessed. | [optional] 
**url** | **str** | The fully qualified URL at which this team&#x27;s knowledge base can be accessed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

