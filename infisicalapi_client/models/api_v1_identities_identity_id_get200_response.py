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



from pydantic import ConfigDict, BaseModel, Field
from infisicalapi_client.models.api_v1_identities_get200_response_identities_inner import ApiV1IdentitiesGet200ResponseIdentitiesInner

class ApiV1IdentitiesIdentityIdGet200Response(BaseModel):
    """
    ApiV1IdentitiesIdentityIdGet200Response
    """
    identity: ApiV1IdentitiesGet200ResponseIdentitiesInner = Field(...)
    __properties = ["identity"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1IdentitiesIdentityIdGet200Response:
        """Create an instance of ApiV1IdentitiesIdentityIdGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IdentitiesIdentityIdGet200Response:
        """Create an instance of ApiV1IdentitiesIdentityIdGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IdentitiesIdentityIdGet200Response.parse_obj(obj)

        _obj = ApiV1IdentitiesIdentityIdGet200Response.parse_obj({
            "identity": ApiV1IdentitiesGet200ResponseIdentitiesInner.from_dict(obj.get("identity")) if obj.get("identity") is not None else None
        })
        return _obj


