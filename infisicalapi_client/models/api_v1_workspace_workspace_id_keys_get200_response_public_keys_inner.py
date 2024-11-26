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


from typing import Optional
from pydantic import ConfigDict, BaseModel, Field, StrictStr

class ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner
    """
    public_key: Optional[StrictStr] = Field(default=None, alias="publicKey")
    user_id: StrictStr = Field(default=..., alias="userId")
    __properties = ["publicKey", "userId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner:
        """Create an instance of ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner:
        """Create an instance of ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdKeysGet200ResponsePublicKeysInner.parse_obj({
            "public_key": obj.get("publicKey"),
            "user_id": obj.get("userId")
        })
        return _obj


