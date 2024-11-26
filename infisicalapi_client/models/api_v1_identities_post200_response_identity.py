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

from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, Field, StrictStr

class ApiV1IdentitiesPost200ResponseIdentity(BaseModel):
    """
    ApiV1IdentitiesPost200ResponseIdentity
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    auth_method: Optional[StrictStr] = Field(default=None, alias="authMethod")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    __properties = ["id", "name", "authMethod", "createdAt", "updatedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1IdentitiesPost200ResponseIdentity:
        """Create an instance of ApiV1IdentitiesPost200ResponseIdentity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if auth_method (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_method is None and "auth_method" in self.__fields_set__:
            _dict['authMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IdentitiesPost200ResponseIdentity:
        """Create an instance of ApiV1IdentitiesPost200ResponseIdentity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IdentitiesPost200ResponseIdentity.parse_obj(obj)

        _obj = ApiV1IdentitiesPost200ResponseIdentity.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "auth_method": obj.get("authMethod"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


