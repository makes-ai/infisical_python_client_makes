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
from infisicalapi_client.models.api_v1_organization_organization_id_permissions_get200_response_membership import ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership

class ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response(BaseModel):
    """
    ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response
    """
    membership: ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership = Field(...)
    __properties = ["membership"]
    model_config = ConfigDict(populate_by_name=True, validate_assignment=True)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response:
        """Create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of membership
        if self.membership:
            _dict['membership'] = self.membership.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response:
        """Create an instance of ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response.parse_obj(obj)

        _obj = ApiV2OrganizationsOrganizationIdMembershipsMembershipIdDelete200Response.parse_obj({
            "membership": ApiV1OrganizationOrganizationIdPermissionsGet200ResponseMembership.from_dict(obj.get("membership")) if obj.get("membership") is not None else None
        })
        return _obj


