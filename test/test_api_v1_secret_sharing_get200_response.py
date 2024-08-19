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

from infisicalapi_client.models.api_v1_secret_sharing_get200_response import ApiV1SecretSharingGet200Response  # noqa: E501

class TestApiV1SecretSharingGet200Response(unittest.TestCase):
    """ApiV1SecretSharingGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1SecretSharingGet200Response:
        """Test ApiV1SecretSharingGet200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1SecretSharingGet200Response`
        """
        model = ApiV1SecretSharingGet200Response()  # noqa: E501
        if include_optional:
            return ApiV1SecretSharingGet200Response(
                secrets = [
                    infisicalapi_client.models._api_v1_secret_sharing_get_200_response_secrets_inner._api_v1_secret_sharing_get_200_response_secrets_inner(
                        id = '', 
                        encrypted_value = '', 
                        iv = '', 
                        tag = '', 
                        hashed_hex = '', 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user_id = '', 
                        org_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expires_after_views = 1.337, 
                        access_type = 'anyone', 
                        name = '', 
                        last_viewed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                total_count = 1.337
            )
        else:
            return ApiV1SecretSharingGet200Response(
                secrets = [
                    infisicalapi_client.models._api_v1_secret_sharing_get_200_response_secrets_inner._api_v1_secret_sharing_get_200_response_secrets_inner(
                        id = '', 
                        encrypted_value = '', 
                        iv = '', 
                        tag = '', 
                        hashed_hex = '', 
                        expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        user_id = '', 
                        org_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        expires_after_views = 1.337, 
                        access_type = 'anyone', 
                        name = '', 
                        last_viewed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                total_count = 1.337,
        )
        """

    def testApiV1SecretSharingGet200Response(self):
        """Test ApiV1SecretSharingGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()