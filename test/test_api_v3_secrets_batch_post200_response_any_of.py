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

from infisicalapi_client.models.api_v3_secrets_batch_post200_response_any_of import ApiV3SecretsBatchPost200ResponseAnyOf  # noqa: E501

class TestApiV3SecretsBatchPost200ResponseAnyOf(unittest.TestCase):
    """ApiV3SecretsBatchPost200ResponseAnyOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV3SecretsBatchPost200ResponseAnyOf:
        """Test ApiV3SecretsBatchPost200ResponseAnyOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV3SecretsBatchPost200ResponseAnyOf`
        """
        model = ApiV3SecretsBatchPost200ResponseAnyOf()  # noqa: E501
        if include_optional:
            return ApiV3SecretsBatchPost200ResponseAnyOf(
                secrets = [
                    infisicalapi_client.models._api_v1_secret_imports_secrets_get_200_response_secrets_inner_secrets_inner._api_v1_secret_imports_secrets_get_200_response_secrets_inner_secrets_inner(
                        id = '', 
                        version = 1.337, 
                        type = 'shared', 
                        secret_key_ciphertext = '', 
                        secret_key_iv = '', 
                        secret_key_tag = '', 
                        secret_value_ciphertext = '', 
                        secret_value_iv = '', 
                        secret_value_tag = '', 
                        secret_comment_ciphertext = '', 
                        secret_comment_iv = '', 
                        secret_comment_tag = '', 
                        secret_reminder_note = '', 
                        secret_reminder_repeat_days = 1.337, 
                        skip_multiline_encoding = True, 
                        algorithm = 'aes-256-gcm', 
                        key_encoding = 'utf8', 
                        metadata = null, 
                        user_id = '', 
                        folder_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return ApiV3SecretsBatchPost200ResponseAnyOf(
                secrets = [
                    infisicalapi_client.models._api_v1_secret_imports_secrets_get_200_response_secrets_inner_secrets_inner._api_v1_secret_imports_secrets_get_200_response_secrets_inner_secrets_inner(
                        id = '', 
                        version = 1.337, 
                        type = 'shared', 
                        secret_key_ciphertext = '', 
                        secret_key_iv = '', 
                        secret_key_tag = '', 
                        secret_value_ciphertext = '', 
                        secret_value_iv = '', 
                        secret_value_tag = '', 
                        secret_comment_ciphertext = '', 
                        secret_comment_iv = '', 
                        secret_comment_tag = '', 
                        secret_reminder_note = '', 
                        secret_reminder_repeat_days = 1.337, 
                        skip_multiline_encoding = True, 
                        algorithm = 'aes-256-gcm', 
                        key_encoding = 'utf8', 
                        metadata = null, 
                        user_id = '', 
                        folder_id = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testApiV3SecretsBatchPost200ResponseAnyOf(self):
        """Test ApiV3SecretsBatchPost200ResponseAnyOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()