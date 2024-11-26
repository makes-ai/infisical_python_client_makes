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
from pydantic import StringConstraints, ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class ApiV1DynamicSecretsLeasesPostRequest(BaseModel):
    """
    ApiV1DynamicSecretsLeasesPostRequest
    """
    dynamic_secret_name: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="dynamicSecretName", description="The name of the dynamic secret.")
    project_slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="projectSlug", description="The slug of the project of the dynamic secret in.")
    ttl: Optional[StrictStr] = Field(default=None, description="The lease lifetime ttl. If not provided the default TTL of dynamic secret will be used.")
    path: Optional[StrictStr] = Field(default='/', description="The path of the dynamic secret in.")
    environment_slug: Annotated[str, StringConstraints(strict=True, min_length=1)] = Field(default=..., alias="environmentSlug", description="The path of the dynamic secret in.")
    __properties = ["dynamicSecretName", "projectSlug", "ttl", "path", "environmentSlug"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1DynamicSecretsLeasesPostRequest:
        """Create an instance of ApiV1DynamicSecretsLeasesPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1DynamicSecretsLeasesPostRequest:
        """Create an instance of ApiV1DynamicSecretsLeasesPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1DynamicSecretsLeasesPostRequest.parse_obj(obj)

        _obj = ApiV1DynamicSecretsLeasesPostRequest.parse_obj({
            "dynamic_secret_name": obj.get("dynamicSecretName"),
            "project_slug": obj.get("projectSlug"),
            "ttl": obj.get("ttl"),
            "path": obj.get("path") if obj.get("path") is not None else '/',
            "environment_slug": obj.get("environmentSlug")
        })
        return _obj


