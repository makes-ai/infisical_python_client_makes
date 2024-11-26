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
from pydantic import ConfigDict, BaseModel, Field, StrictStr

class ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser(BaseModel):
    """
    ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser
    """
    username: StrictStr = Field(...)
    email: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    id: StrictStr = Field(...)
    public_key: Optional[StrictStr] = Field(default=..., alias="publicKey")
    __properties = ["username", "email", "firstName", "lastName", "id", "publicKey"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser:
        """Create an instance of ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.first_name is None and "first_name" in self.__fields_set__:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.last_name is None and "last_name" in self.__fields_set__:
            _dict['lastName'] = None

        # set to None if public_key (nullable) is None
        # and __fields_set__ contains the field
        if self.public_key is None and "public_key" in self.__fields_set__:
            _dict['publicKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser:
        """Create an instance of ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser.parse_obj(obj)

        _obj = ApiV1OrganizationOrganizationIdUsersGet200ResponseUsersInnerUser.parse_obj({
            "username": obj.get("username"),
            "email": obj.get("email"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "id": obj.get("id"),
            "public_key": obj.get("publicKey")
        })
        return _obj


