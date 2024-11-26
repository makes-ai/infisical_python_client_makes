# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_workspace_project_slug_roles_post_request_permissions_inner import ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner
from typing_extensions import Annotated

class ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest(BaseModel):
    """
    ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest
    """
    slug: Optional[StrictStr] = Field(default=None, description="The slug of the role.")
    name: Optional[StrictStr] = Field(default=None, description="The name of the role.")
    permissions: Optional[Annotated[List[ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner], Field()]] = Field(default=None, description="The permissions assigned to the role.")
    __properties = ["slug", "name", "permissions"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest:
        """Create an instance of ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item in self.permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['permissions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest:
        """Create an instance of ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest.parse_obj(obj)

        _obj = ApiV1WorkspaceProjectSlugRolesRoleIdPatchRequest.parse_obj({
            "slug": obj.get("slug"),
            "name": obj.get("name"),
            "permissions": [ApiV1WorkspaceProjectSlugRolesPostRequestPermissionsInner.from_dict(_item) for _item in obj.get("permissions")] if obj.get("permissions") is not None else None
        })
        return _obj


