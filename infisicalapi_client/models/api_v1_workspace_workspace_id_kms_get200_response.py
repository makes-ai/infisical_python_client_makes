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
from infisicalapi_client.models.api_v1_workspace_workspace_id_kms_get200_response_secret_manager_kms_key import ApiV1WorkspaceWorkspaceIdKmsGet200ResponseSecretManagerKmsKey

class ApiV1WorkspaceWorkspaceIdKmsGet200Response(BaseModel):
    """
    ApiV1WorkspaceWorkspaceIdKmsGet200Response
    """
    secret_manager_kms_key: ApiV1WorkspaceWorkspaceIdKmsGet200ResponseSecretManagerKmsKey = Field(default=..., alias="secretManagerKmsKey")
    __properties = ["secretManagerKmsKey"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1WorkspaceWorkspaceIdKmsGet200Response:
        """Create an instance of ApiV1WorkspaceWorkspaceIdKmsGet200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of secret_manager_kms_key
        if self.secret_manager_kms_key:
            _dict['secretManagerKmsKey'] = self.secret_manager_kms_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceWorkspaceIdKmsGet200Response:
        """Create an instance of ApiV1WorkspaceWorkspaceIdKmsGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceWorkspaceIdKmsGet200Response.parse_obj(obj)

        _obj = ApiV1WorkspaceWorkspaceIdKmsGet200Response.parse_obj({
            "secret_manager_kms_key": ApiV1WorkspaceWorkspaceIdKmsGet200ResponseSecretManagerKmsKey.from_dict(obj.get("secretManagerKmsKey")) if obj.get("secretManagerKmsKey") is not None else None
        })
        return _obj


