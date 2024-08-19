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



from pydantic import BaseModel, Field, StrictStr

class ApiV1WorkspaceProjectIdTagsPostRequest(BaseModel):
    """
    ApiV1WorkspaceProjectIdTagsPostRequest
    """
    slug: StrictStr = Field(default=..., description="The slug of the tag to create.")
    color: StrictStr = Field(default=..., description="The color of the tag to create.")
    __properties = ["slug", "color"]

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
    def from_json(cls, json_str: str) -> ApiV1WorkspaceProjectIdTagsPostRequest:
        """Create an instance of ApiV1WorkspaceProjectIdTagsPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiV1WorkspaceProjectIdTagsPostRequest:
        """Create an instance of ApiV1WorkspaceProjectIdTagsPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiV1WorkspaceProjectIdTagsPostRequest.parse_obj(obj)

        _obj = ApiV1WorkspaceProjectIdTagsPostRequest.parse_obj({
            "slug": obj.get("slug"),
            "color": obj.get("color")
        })
        return _obj

