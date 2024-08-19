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


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr

class ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner(BaseModel):
    """
    ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner
    """
    name: StrictStr = Field(...)
    title: StrictStr = Field(...)
    image: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    template: Optional[Any] = None
    __properties = ["name", "title", "image", "description", "template"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner:
        """Create an instance of ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if template (nullable) is None
        # and __fields_set__ contains the field
        if self.template is None and "template" in self.__fields_set__:
            _dict['template'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner:
        """Create an instance of ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner.parse_obj(obj)

        _obj = ApiV1SecretRotationProvidersWorkspaceIdGet200ResponseProvidersInner.parse_obj({
            "name": obj.get("name"),
            "title": obj.get("title"),
            "image": obj.get("image"),
            "description": obj.get("description"),
            "template": obj.get("template")
        })
        return _obj

