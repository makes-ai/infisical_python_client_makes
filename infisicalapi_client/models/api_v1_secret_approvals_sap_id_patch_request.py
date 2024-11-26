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


from typing import List, Optional, Union
from pydantic import field_validator, ConfigDict, BaseModel, Field, StrictStr
from typing_extensions import Annotated

class ApiV1SecretApprovalsSapIdPatchRequest(BaseModel):
    """
    ApiV1SecretApprovalsSapIdPatchRequest
    """
    name: Optional[StrictStr] = None
    approvers: Annotated[List[StrictStr], Field(min_length=1)] = Field(...)
    approvals: Optional[Union[Annotated[float, Field(ge=1, strict=True)], Annotated[int, Field(ge=1, strict=True)]]] = 1
    secret_path: Optional[StrictStr] = Field(default=None, alias="secretPath")
    enforcement_level: Optional[StrictStr] = Field(default=None, alias="enforcementLevel")
    __properties = ["name", "approvers", "approvals", "secretPath", "enforcementLevel"]

    @field_validator('enforcement_level')
    @classmethod
    def enforcement_level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('hard', 'soft'):
            raise ValueError("must be one of enum values ('hard', 'soft')")
        return value
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1SecretApprovalsSapIdPatchRequest:
        """Create an instance of ApiV1SecretApprovalsSapIdPatchRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if secret_path (nullable) is None
        # and __fields_set__ contains the field
        if self.secret_path is None and "secret_path" in self.__fields_set__:
            _dict['secretPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretApprovalsSapIdPatchRequest:
        """Create an instance of ApiV1SecretApprovalsSapIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretApprovalsSapIdPatchRequest.parse_obj(obj)

        _obj = ApiV1SecretApprovalsSapIdPatchRequest.parse_obj({
            "name": obj.get("name"),
            "approvers": obj.get("approvers"),
            "approvals": obj.get("approvals") if obj.get("approvals") is not None else 1,
            "secret_path": obj.get("secretPath"),
            "enforcement_level": obj.get("enforcementLevel")
        })
        return _obj


