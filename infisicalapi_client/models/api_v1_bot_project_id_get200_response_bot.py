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

from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr

class ApiV1BotProjectIdGet200ResponseBot(BaseModel):
    """
    ApiV1BotProjectIdGet200ResponseBot
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    is_active: Optional[StrictBool] = Field(default=False, alias="isActive")
    public_key: StrictStr = Field(default=..., alias="publicKey")
    encrypted_project_key: Optional[StrictStr] = Field(default=None, alias="encryptedProjectKey")
    encrypted_project_key_nonce: Optional[StrictStr] = Field(default=None, alias="encryptedProjectKeyNonce")
    project_id: StrictStr = Field(default=..., alias="projectId")
    sender_id: Optional[StrictStr] = Field(default=None, alias="senderId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    __properties = ["id", "name", "isActive", "publicKey", "encryptedProjectKey", "encryptedProjectKeyNonce", "projectId", "senderId", "createdAt", "updatedAt"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1BotProjectIdGet200ResponseBot:
        """Create an instance of ApiV1BotProjectIdGet200ResponseBot from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if encrypted_project_key (nullable) is None
        # and __fields_set__ contains the field
        if self.encrypted_project_key is None and "encrypted_project_key" in self.__fields_set__:
            _dict['encryptedProjectKey'] = None

        # set to None if encrypted_project_key_nonce (nullable) is None
        # and __fields_set__ contains the field
        if self.encrypted_project_key_nonce is None and "encrypted_project_key_nonce" in self.__fields_set__:
            _dict['encryptedProjectKeyNonce'] = None

        # set to None if sender_id (nullable) is None
        # and __fields_set__ contains the field
        if self.sender_id is None and "sender_id" in self.__fields_set__:
            _dict['senderId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1BotProjectIdGet200ResponseBot:
        """Create an instance of ApiV1BotProjectIdGet200ResponseBot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1BotProjectIdGet200ResponseBot.parse_obj(obj)

        _obj = ApiV1BotProjectIdGet200ResponseBot.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "is_active": obj.get("isActive") if obj.get("isActive") is not None else False,
            "public_key": obj.get("publicKey"),
            "encrypted_project_key": obj.get("encryptedProjectKey"),
            "encrypted_project_key_nonce": obj.get("encryptedProjectKeyNonce"),
            "project_id": obj.get("projectId"),
            "sender_id": obj.get("senderId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj


