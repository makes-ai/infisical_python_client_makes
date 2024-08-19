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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret(BaseModel):
    """
    ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret
    """
    secret_key: StrictStr = Field(default=..., alias="secretKey")
    id: StrictStr = Field(...)
    version: Union[StrictFloat, StrictInt] = Field(...)
    __properties = ["secretKey", "id", "version"]

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
    def from_json(cls, json_str: str) -> ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret:
        """Create an instance of ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret:
        """Create an instance of ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret.parse_obj(obj)

        _obj = ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret.parse_obj({
            "secret_key": obj.get("secretKey"),
            "id": obj.get("id"),
            "version": obj.get("version")
        })
        return _obj

