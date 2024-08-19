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

class ApiV1AuthUniversalAuthLoginPostRequest(BaseModel):
    """
    ApiV1AuthUniversalAuthLoginPostRequest
    """
    client_id: StrictStr = Field(default=..., alias="clientId", description="Your Machine Identity Client ID.")
    client_secret: StrictStr = Field(default=..., alias="clientSecret", description="Your Machine Identity Client Secret.")
    __properties = ["clientId", "clientSecret"]

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
    def from_json(cls, json_str: str) -> ApiV1AuthUniversalAuthLoginPostRequest:
        """Create an instance of ApiV1AuthUniversalAuthLoginPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AuthUniversalAuthLoginPostRequest:
        """Create an instance of ApiV1AuthUniversalAuthLoginPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AuthUniversalAuthLoginPostRequest.parse_obj(obj)

        _obj = ApiV1AuthUniversalAuthLoginPostRequest.parse_obj({
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret")
        })
        return _obj

