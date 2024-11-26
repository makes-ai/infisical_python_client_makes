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
from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictBool, StrictStr

class ApiV1SsoOidcConfigPatchRequest(BaseModel):
    """
    ApiV1SsoOidcConfigPatchRequest
    """
    allowed_email_domains: Optional[StrictStr] = Field(default='', alias="allowedEmailDomains")
    discovery_url: Optional[StrictStr] = Field(default=None, alias="discoveryURL")
    configuration_type: Optional[StrictStr] = Field(default=None, alias="configurationType")
    issuer: Optional[StrictStr] = None
    authorization_endpoint: Optional[StrictStr] = Field(default=None, alias="authorizationEndpoint")
    jwks_uri: Optional[StrictStr] = Field(default=None, alias="jwksUri")
    token_endpoint: Optional[StrictStr] = Field(default=None, alias="tokenEndpoint")
    userinfo_endpoint: Optional[StrictStr] = Field(default=None, alias="userinfoEndpoint")
    client_id: Optional[StrictStr] = Field(default=None, alias="clientId")
    client_secret: Optional[StrictStr] = Field(default=None, alias="clientSecret")
    is_active: Optional[StrictBool] = Field(default=None, alias="isActive")
    org_slug: StrictStr = Field(default=..., alias="orgSlug")
    __properties = ["allowedEmailDomains", "discoveryURL", "configurationType", "issuer", "authorizationEndpoint", "jwksUri", "tokenEndpoint", "userinfoEndpoint", "clientId", "clientSecret", "isActive", "orgSlug"]

    @field_validator('configuration_type')
    @classmethod
    def configuration_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('custom', 'discoveryURL'):
            raise ValueError("must be one of enum values ('custom', 'discoveryURL')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SsoOidcConfigPatchRequest:
        """Create an instance of ApiV1SsoOidcConfigPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SsoOidcConfigPatchRequest:
        """Create an instance of ApiV1SsoOidcConfigPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SsoOidcConfigPatchRequest.parse_obj(obj)

        _obj = ApiV1SsoOidcConfigPatchRequest.parse_obj({
            "allowed_email_domains": obj.get("allowedEmailDomains") if obj.get("allowedEmailDomains") is not None else '',
            "discovery_url": obj.get("discoveryURL"),
            "configuration_type": obj.get("configurationType"),
            "issuer": obj.get("issuer"),
            "authorization_endpoint": obj.get("authorizationEndpoint"),
            "jwks_uri": obj.get("jwksUri"),
            "token_endpoint": obj.get("tokenEndpoint"),
            "userinfo_endpoint": obj.get("userinfoEndpoint"),
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret"),
            "is_active": obj.get("isActive"),
            "org_slug": obj.get("orgSlug")
        })
        return _obj


