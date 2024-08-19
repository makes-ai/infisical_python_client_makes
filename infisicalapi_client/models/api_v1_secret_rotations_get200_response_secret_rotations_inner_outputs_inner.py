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



from pydantic import BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_secret_rotations_get200_response_secret_rotations_inner_outputs_inner_secret import ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret

class ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner(BaseModel):
    """
    ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner
    """
    key: StrictStr = Field(...)
    secret: ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret = Field(...)
    __properties = ["key", "secret"]

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
    def from_json(cls, json_str: str) -> ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner:
        """Create an instance of ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of secret
        if self.secret:
            _dict['secret'] = self.secret.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner:
        """Create an instance of ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner.parse_obj(obj)

        _obj = ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInner.parse_obj({
            "key": obj.get("key"),
            "secret": ApiV1SecretRotationsGet200ResponseSecretRotationsInnerOutputsInnerSecret.from_dict(obj.get("secret")) if obj.get("secret") is not None else None
        })
        return _obj

