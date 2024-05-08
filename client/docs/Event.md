# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] 
**name** | **str** |  | [optional] 
**model_id** | **str** | Identifier for the object this event is associated with when it is not one of document, collection, or user. | [optional] 
**actor_id** | **str** | The user that performed the action. | [optional] 
**actor_ip_address** | **str** | The ip address the action was performed from. This field is only returned when the &#x60;auditLog&#x60; boolean is true. | [optional] 
**collection_id** | **str** | Identifier for the associated collection, if any | [optional] 
**document_id** | **str** | Identifier for the associated document, if any | [optional] 
**created_at** | **datetime** | The date and time that this event was created | [optional] 
**data** | **object** | Additional unstructured data associated with the event | [optional] 
**actor** | [**User**](User.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

