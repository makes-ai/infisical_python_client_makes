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
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr

class ApiV1SsoOidcConfigGet200Response(BaseModel):
    """
    ApiV1SsoOidcConfigGet200Response
    """
    id: StrictStr = Field(...)
    issuer: Optional[StrictStr] = None
    authorization_endpoint: Optional[StrictStr] = Field(default=None, alias="authorizationEndpoint")
    jwks_uri: Optional[StrictStr] = Field(default=None, alias="jwksUri")
    token_endpoint: Optional[StrictStr] = Field(default=None, alias="tokenEndpoint")
    userinfo_endpoint: Optional[StrictStr] = Field(default=None, alias="userinfoEndpoint")
    configuration_type: StrictStr = Field(default=..., alias="configurationType")
    discovery_url: Optional[StrictStr] = Field(default=None, alias="discoveryURL")
    is_active: StrictBool = Field(default=..., alias="isActive")
    org_id: StrictStr = Field(default=..., alias="orgId")
    allowed_email_domains: Optional[StrictStr] = Field(default=None, alias="allowedEmailDomains")
    client_id: StrictStr = Field(default=..., alias="clientId")
    client_secret: StrictStr = Field(default=..., alias="clientSecret")
    __properties = ["id", "issuer", "authorizationEndpoint", "jwksUri", "tokenEndpoint", "userinfoEndpoint", "configurationType", "discoveryURL", "isActive", "orgId", "allowedEmailDomains", "clientId", "clientSecret"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SsoOidcConfigGet200Response:
        """Create an instance of ApiV1SsoOidcConfigGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if issuer (nullable) is None
        # and __fields_set__ contains the field
        if self.issuer is None and "issuer" in self.__fields_set__:
            _dict['issuer'] = None

        # set to None if authorization_endpoint (nullable) is None
        # and __fields_set__ contains the field
        if self.authorization_endpoint is None and "authorization_endpoint" in self.__fields_set__:
            _dict['authorizationEndpoint'] = None

        # set to None if jwks_uri (nullable) is None
        # and __fields_set__ contains the field
        if self.jwks_uri is None and "jwks_uri" in self.__fields_set__:
            _dict['jwksUri'] = None

        # set to None if token_endpoint (nullable) is None
        # and __fields_set__ contains the field
        if self.token_endpoint is None and "token_endpoint" in self.__fields_set__:
            _dict['tokenEndpoint'] = None

        # set to None if userinfo_endpoint (nullable) is None
        # and __fields_set__ contains the field
        if self.userinfo_endpoint is None and "userinfo_endpoint" in self.__fields_set__:
            _dict['userinfoEndpoint'] = None

        # set to None if discovery_url (nullable) is None
        # and __fields_set__ contains the field
        if self.discovery_url is None and "discovery_url" in self.__fields_set__:
            _dict['discoveryURL'] = None

        # set to None if allowed_email_domains (nullable) is None
        # and __fields_set__ contains the field
        if self.allowed_email_domains is None and "allowed_email_domains" in self.__fields_set__:
            _dict['allowedEmailDomains'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SsoOidcConfigGet200Response:
        """Create an instance of ApiV1SsoOidcConfigGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SsoOidcConfigGet200Response.parse_obj(obj)

        _obj = ApiV1SsoOidcConfigGet200Response.parse_obj({
            "id": obj.get("id"),
            "issuer": obj.get("issuer"),
            "authorization_endpoint": obj.get("authorizationEndpoint"),
            "jwks_uri": obj.get("jwksUri"),
            "token_endpoint": obj.get("tokenEndpoint"),
            "userinfo_endpoint": obj.get("userinfoEndpoint"),
            "configuration_type": obj.get("configurationType"),
            "discovery_url": obj.get("discoveryURL"),
            "is_active": obj.get("isActive"),
            "org_id": obj.get("orgId"),
            "allowed_email_domains": obj.get("allowedEmailDomains"),
            "client_id": obj.get("clientId"),
            "client_secret": obj.get("clientSecret")
        })
        return _obj


