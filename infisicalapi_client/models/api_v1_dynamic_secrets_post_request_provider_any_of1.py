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



from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictStr
from infisicalapi_client.models.api_v1_dynamic_secrets_post_request_provider_any_of1_inputs import ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs

class ApiV1DynamicSecretsPostRequestProviderAnyOf1(BaseModel):
    """
    ApiV1DynamicSecretsPostRequestProviderAnyOf1
    """
    type: StrictStr = Field(...)
    inputs: ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs = Field(...)
    __properties = ["type", "inputs"]

    @field_validator('type')
    @classmethod
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('cassandra'):
            raise ValueError("must be one of enum values ('cassandra')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsPostRequestProviderAnyOf1:
        """Create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of inputs
        if self.inputs:
            _dict['inputs'] = self.inputs.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsPostRequestProviderAnyOf1:
        """Create an instance of ApiV1DynamicSecretsPostRequestProviderAnyOf1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsPostRequestProviderAnyOf1.parse_obj(obj)

        _obj = ApiV1DynamicSecretsPostRequestProviderAnyOf1.parse_obj({
            "type": obj.get("type"),
            "inputs": ApiV1DynamicSecretsPostRequestProviderAnyOf1Inputs.from_dict(obj.get("inputs")) if obj.get("inputs") is not None else None
        })
        return _obj


