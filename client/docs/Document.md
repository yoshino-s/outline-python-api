# Document

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] 
**collection_id** | **str** | Identifier for the associated collection. | [optional] 
**parent_document_id** | **str** | Identifier for the document this is a child of, if any. | [optional] 
**title** | **str** | The title of the document. | [optional] 
**full_width** | **bool** | Whether this document should be displayed in a full-width view. | [optional] 
**emoji** | **str** | An emoji associated with the document. | [optional] 
**text** | **str** | The text content of the document, contains markdown formatting | [optional] 
**url_id** | **str** | A short unique ID that can be used to identify the document as an alternative to the UUID | [optional] 
**collaborators** | [**list[User]**](User.md) |  | [optional] 
**pinned** | **bool** | Whether this document is pinned in the collection | [optional] 
**template** | **bool** | Whether this document is a template | [optional] 
**template_id** | **str** | Unique identifier for the template this document was created from, if any | [optional] 
**revision** | **float** | A number that is auto incrementing with every revision of the document that is saved | [optional] 
**created_at** | **datetime** | The date and time that this object was created | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** | The date and time that this object was last changed | [optional] 
**updated_by** | [**User**](User.md) |  | [optional] 
**published_at** | **datetime** | The date and time that this object was published | [optional] 
**archived_at** | **datetime** | The date and time that this object was archived | [optional] 
**deleted_at** | **datetime** | The date and time that this object was deleted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

