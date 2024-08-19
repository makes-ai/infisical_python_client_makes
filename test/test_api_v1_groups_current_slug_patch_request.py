# coding: utf-8

"""
    Infisical API

    List of all available APIs that can be consumed

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from infisicalapi_client.models.api_v1_groups_current_slug_patch_request import ApiV1GroupsCurrentSlugPatchRequest  # noqa: E501

class TestApiV1GroupsCurrentSlugPatchRequest(unittest.TestCase):
    """ApiV1GroupsCurrentSlugPatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1GroupsCurrentSlugPatchRequest:
        """Test ApiV1GroupsCurrentSlugPatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1GroupsCurrentSlugPatchRequest`
        """
        model = ApiV1GroupsCurrentSlugPatchRequest()  # noqa: E501
        if include_optional:
            return ApiV1GroupsCurrentSlugPatchRequest(
                name = '0',
                slug = '01234',
                role = '0'
            )
        else:
            return ApiV1GroupsCurrentSlugPatchRequest(
        )
        """

    def testApiV1GroupsCurrentSlugPatchRequest(self):
        """Test ApiV1GroupsCurrentSlugPatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()