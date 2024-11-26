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
from typing import Any, List, Optional
from pydantic import ConfigDict, BaseModel, Field, StrictBool, StrictStr
from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response_requests_inner_policy import ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy
from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response_requests_inner_privilege import ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege
from infisicalapi_client.models.api_v1_access_approvals_requests_get200_response_requests_inner_reviewers_inner import ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner
from typing_extensions import Annotated

class ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner(BaseModel):
    """
    ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner
    """
    id: StrictStr = Field(...)
    policy_id: StrictStr = Field(default=..., alias="policyId")
    privilege_id: Optional[StrictStr] = Field(default=None, alias="privilegeId")
    requested_by: StrictStr = Field(default=..., alias="requestedBy")
    is_temporary: StrictBool = Field(default=..., alias="isTemporary")
    temporary_range: Optional[StrictStr] = Field(default=None, alias="temporaryRange")
    permissions: Optional[Any] = None
    created_at: datetime = Field(default=..., alias="createdAt")
    updated_at: datetime = Field(default=..., alias="updatedAt")
    environment_name: StrictStr = Field(default=..., alias="environmentName")
    is_approved: StrictBool = Field(default=..., alias="isApproved")
    privilege: Optional[ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege] = Field(...)
    policy: ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy = Field(...)
    reviewers: Annotated[List[ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner], Field()] = Field(...)
    __properties = ["id", "policyId", "privilegeId", "requestedBy", "isTemporary", "temporaryRange", "permissions", "createdAt", "updatedAt", "environmentName", "isApproved", "privilege", "policy", "reviewers"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner:
        """Create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of privilege
        if self.privilege:
            _dict['privilege'] = self.privilege.to_dict()
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in reviewers (list)
        _items = []
        if self.reviewers:
            for _item in self.reviewers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reviewers'] = _items
        # set to None if privilege_id (nullable) is None
        # and __fields_set__ contains the field
        if self.privilege_id is None and "privilege_id" in self.__fields_set__:
            _dict['privilegeId'] = None

        # set to None if temporary_range (nullable) is None
        # and __fields_set__ contains the field
        if self.temporary_range is None and "temporary_range" in self.__fields_set__:
            _dict['temporaryRange'] = None

        # set to None if permissions (nullable) is None
        # and __fields_set__ contains the field
        if self.permissions is None and "permissions" in self.__fields_set__:
            _dict['permissions'] = None

        # set to None if privilege (nullable) is None
        # and __fields_set__ contains the field
        if self.privilege is None and "privilege" in self.__fields_set__:
            _dict['privilege'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner:
        """Create an instance of ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner.parse_obj(obj)

        _obj = ApiV1AccessApprovalsRequestsGet200ResponseRequestsInner.parse_obj({
            "id": obj.get("id"),
            "policy_id": obj.get("policyId"),
            "privilege_id": obj.get("privilegeId"),
            "requested_by": obj.get("requestedBy"),
            "is_temporary": obj.get("isTemporary"),
            "temporary_range": obj.get("temporaryRange"),
            "permissions": obj.get("permissions"),
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt"),
            "environment_name": obj.get("environmentName"),
            "is_approved": obj.get("isApproved"),
            "privilege": ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPrivilege.from_dict(obj.get("privilege")) if obj.get("privilege") is not None else None,
            "policy": ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerPolicy.from_dict(obj.get("policy")) if obj.get("policy") is not None else None,
            "reviewers": [ApiV1AccessApprovalsRequestsGet200ResponseRequestsInnerReviewersInner.from_dict(_item) for _item in obj.get("reviewers")] if obj.get("reviewers") is not None else None
        })
        return _obj


