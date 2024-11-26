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
from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictStr

class ApiV1WebhooksPostRequest(BaseModel):
    """
    ApiV1WebhooksPostRequest
    """
    type: Optional[StrictStr] = 'general'
    workspace_id: StrictStr = Field(default=..., alias="workspaceId")
    environment: StrictStr = Field(...)
    webhook_url: StrictStr = Field(default=..., alias="webhookUrl")
    webhook_secret_key: Optional[StrictStr] = Field(default=None, alias="webhookSecretKey")
    secret_path: Optional[StrictStr] = Field(default='/', alias="secretPath")
    __properties = ["type", "workspaceId", "environment", "webhookUrl", "webhookSecretKey", "secretPath"]

    @field_validator('type')
    @classmethod
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('general', 'slack'):
            raise ValueError("must be one of enum values ('general', 'slack')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WebhooksPostRequest:
        """Create an instance of ApiV1WebhooksPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WebhooksPostRequest:
        """Create an instance of ApiV1WebhooksPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WebhooksPostRequest.parse_obj(obj)

        _obj = ApiV1WebhooksPostRequest.parse_obj({
            "type": obj.get("type") if obj.get("type") is not None else 'general',
            "workspace_id": obj.get("workspaceId"),
            "environment": obj.get("environment"),
            "webhook_url": obj.get("webhookUrl"),
            "webhook_secret_key": obj.get("webhookSecretKey"),
            "secret_path": obj.get("secretPath") if obj.get("secretPath") is not None else '/'
        })
        return _obj


