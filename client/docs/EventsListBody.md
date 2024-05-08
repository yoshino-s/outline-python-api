# EventsListBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**name** | **str** | Filter to a specific event, e.g. \&quot;collections.create\&quot;. Event names are in the format \&quot;objects.verb\&quot; | [optional] 
**actor_id** | **str** | Filter to events performed by the selected user | [optional] 
**document_id** | **str** | Filter to events performed in the selected document | [optional] 
**collection_id** | **str** | Filter to events performed in the selected collection | [optional] 
**audit_log** | **bool** | Whether to return detailed events suitable for an audit log. Without this flag less detailed event types will be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

