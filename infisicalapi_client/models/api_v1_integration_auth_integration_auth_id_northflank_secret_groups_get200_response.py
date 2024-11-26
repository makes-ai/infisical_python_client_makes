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


from typing import List
from pydantic import ConfigDict, BaseModel, Field
from infisicalapi_client.models.api_v1_integration_auth_integration_auth_id_northflank_secret_groups_get200_response_secret_groups_inner import ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner
from typing_extensions import Annotated

class ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response(BaseModel):
    """
    ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response
    """
    secret_groups: Annotated[List[ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner], Field()] = Field(default=..., alias="secretGroups")
    __properties = ["secretGroups"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response:
        """Create an instance of ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in secret_groups (list)
        _items = []
        if self.secret_groups:
            for _item in self.secret_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['secretGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response:
        """Create an instance of ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response.parse_obj(obj)

        _obj = ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200Response.parse_obj({
            "secret_groups": [ApiV1IntegrationAuthIntegrationAuthIdNorthflankSecretGroupsGet200ResponseSecretGroupsInner.from_dict(_item) for _item in obj.get("secretGroups")] if obj.get("secretGroups") is not None else None
        })
        return _obj


