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
from typing import Any, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval(BaseModel):
    """
    ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval
    """
    id: StrictStr = Field(...)
    policy_id: StrictStr = Field(default=..., alias="policyId")
    has_merged: Optional[StrictBool] = Field(default=False, alias="hasMerged")
    status: Optional[StrictStr] = 'open'
    conflicts: Optional[Any] = None
    slug: StrictStr = Field(...)
    folder_id: StrictStr = Field(default=..., alias="folderId")
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    is_replicated: Optional[StrictBool] = Field(default=None, alias="isReplicated")
    committer_user_id: StrictStr = Field(default=..., alias="committerUserId")
    status_changed_by_user_id: Optional[StrictStr] = Field(default=None, alias="statusChangedByUserId")
    bypass_reason: Optional[StrictStr] = Field(default=None, alias="bypassReason")
    __properties = ["id", "policyId", "hasMerged", "status", "conflicts", "slug", "folderId", "createdAt", "updatedAt", "isReplicated", "committerUserId", "statusChangedByUserId", "bypassReason"]

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
    def from_json(cls, json_str: str) -> ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval:
        """Create an instance of ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if conflicts (nullable) is None
        # and __fields_set__ contains the field
        if self.conflicts is None and "conflicts" in self.__fields_set__:
            _dict['conflicts'] = None

        # set to None if is_replicated (nullable) is None
        # and __fields_set__ contains the field
        if self.is_replicated is None and "is_replicated" in self.__fields_set__:
            _dict['isReplicated'] = None

        # set to None if status_changed_by_user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.status_changed_by_user_id is None and "status_changed_by_user_id" in self.__fields_set__:
            _dict['statusChangedByUserId'] = None

        # set to None if bypass_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.bypass_reason is None and "bypass_reason" in self.__fields_set__:
            _dict['bypassReason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval:
        """Create an instance of ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval.parse_obj(obj)

        _obj = ApiV1SecretApprovalRequestsIdMergePost200ResponseApproval.parse_obj({
            "id": obj.get("id"),
            "policy_id": obj.get("policyId"),
            "has_merged": obj.get("hasMerged") if obj.get("hasMerged") is not None else False,
            "status": obj.get("status") if obj.get("status") is not None else 'open',
            "conflicts": obj.get("conflicts"),
            "slug": obj.get("slug"),
            "folder_id": obj.get("folderId"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "is_replicated": obj.get("isReplicated"),
            "committer_user_id": obj.get("committerUserId"),
            "status_changed_by_user_id": obj.get("statusChangedByUserId"),
            "bypass_reason": obj.get("bypassReason")
        })
        return _obj

