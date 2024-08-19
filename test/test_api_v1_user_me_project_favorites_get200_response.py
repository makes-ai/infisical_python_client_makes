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

from infisicalapi_client.models.api_v1_user_me_project_favorites_get200_response import ApiV1UserMeProjectFavoritesGet200Response  # noqa: E501

class TestApiV1UserMeProjectFavoritesGet200Response(unittest.TestCase):
    """ApiV1UserMeProjectFavoritesGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1UserMeProjectFavoritesGet200Response:
        """Test ApiV1UserMeProjectFavoritesGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1UserMeProjectFavoritesGet200Response`
        """
        model = ApiV1UserMeProjectFavoritesGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1UserMeProjectFavoritesGet200Response(
                project_favorites = [
                    ''
                    ]
            )
        else:
            return ApiV1UserMeProjectFavoritesGet200Response(
                project_favorites = [
                    ''
                    ],
        )
        """

    def testApiV1UserMeProjectFavoritesGet200Response(self):
        """Test ApiV1UserMeProjectFavoritesGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()