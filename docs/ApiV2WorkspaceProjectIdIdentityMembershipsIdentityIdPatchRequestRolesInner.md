# ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role slug to assign to the newly created identity project membership. | 
**is_temporary** | **bool** | Whether the assigned role is temporary. If isTemporary is set true, must provide temporaryMode, temporaryRange and temporaryAccessStartTime. | 
**temporary_mode** | **str** | Type of temporary expiry. | 
**temporary_range** | **str** | Expiry time for temporary access. In relative mode it could be 1s,2m,3h | 
**temporary_access_start_time** | **datetime** | Time to which the temporary access starts | 

## Example

```python
from infisicalapi_client.models.api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner import ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner from a JSON string
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_instance = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner.from_json(json)
# print the JSON string representation of the object
print ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner.to_json()

# convert the object into a dict
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_dict = api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_instance.to_dict()
# create an instance of ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner from a dict
api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_from_dict = ApiV2WorkspaceProjectIdIdentityMembershipsIdentityIdPatchRequestRolesInner.from_dict(api_v2_workspace_project_id_identity_memberships_identity_id_patch_request_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

