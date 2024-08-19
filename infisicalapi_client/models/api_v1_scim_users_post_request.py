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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from infisicalapi_client.models.api_v1_scim_users_get200_response_resources_inner_name import ApiV1ScimUsersGet200ResponseResourcesInnerName
from infisicalapi_client.models.api_v1_scim_users_post_request_emails_inner import ApiV1ScimUsersPostRequestEmailsInner

class ApiV1ScimUsersPostRequest(BaseModel):
    """
    ApiV1ScimUsersPostRequest
    """
    schemas: conlist(StrictStr) = Field(...)
    user_name: StrictStr = Field(default=..., alias="userName")
    name: ApiV1ScimUsersGet200ResponseResourcesInnerName = Field(...)
    emails: Optional[conlist(ApiV1ScimUsersPostRequestEmailsInner)] = None
    active: StrictBool = Field(...)
    __properties = ["schemas", "userName", "name", "emails", "active"]

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
    def from_json(cls, json_str: str) -> ApiV1ScimUsersPostRequest:
        """Create an instance of ApiV1ScimUsersPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of name
        if self.name:
            _dict['name'] = self.name.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item in self.emails:
                if _item:
                    _items.append(_item.to_dict())
            _dict['emails'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1ScimUsersPostRequest:
        """Create an instance of ApiV1ScimUsersPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1ScimUsersPostRequest.parse_obj(obj)

        _obj = ApiV1ScimUsersPostRequest.parse_obj({
            "schemas": obj.get("schemas"),
            "user_name": obj.get("userName"),
            "name": ApiV1ScimUsersGet200ResponseResourcesInnerName.from_dict(obj.get("name")) if obj.get("name") is not None else None,
            "emails": [ApiV1ScimUsersPostRequestEmailsInner.from_dict(_item) for _item in obj.get("emails")] if obj.get("emails") is not None else None,
            "active": obj.get("active")
        })
        return _obj

