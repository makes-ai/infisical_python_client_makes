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



from pydantic import ConfigDict, BaseModel, Field, StrictStr

class ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner(BaseModel):
    """
    ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner
    """
    id: StrictStr = Field(...)
    key: StrictStr = Field(...)
    secret_id: StrictStr = Field(default=..., alias="secretId")
    rotation_id: StrictStr = Field(default=..., alias="rotationId")
    __properties = ["id", "key", "secretId", "rotationId"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner:
        """Create an instance of ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner:
        """Create an instance of ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner.parse_obj(obj)

        _obj = ApiV1SecretRotationsPost200ResponseSecretRotationOutputsInner.parse_obj({
            "id": obj.get("id"),
            "key": obj.get("key"),
            "secret_id": obj.get("secretId"),
            "rotation_id": obj.get("rotationId")
        })
        return _obj


