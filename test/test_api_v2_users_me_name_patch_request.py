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

from infisicalapi_client.models.api_v2_users_me_name_patch_request import ApiV2UsersMeNamePatchRequest  # noqa: E501

class TestApiV2UsersMeNamePatchRequest(unittest.TestCase):
    """ApiV2UsersMeNamePatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV2UsersMeNamePatchRequest:
        """Test ApiV2UsersMeNamePatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV2UsersMeNamePatchRequest`
        """
        model = ApiV2UsersMeNamePatchRequest()  # noqa: E501
        if include_optional:
            return ApiV2UsersMeNamePatchRequest(
                first_name = '',
                last_name = ''
            )
        else:
            return ApiV2UsersMeNamePatchRequest(
                first_name = '',
                last_name = '',
        )
        """

    def testApiV2UsersMeNamePatchRequest(self):
        """Test ApiV2UsersMeNamePatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()