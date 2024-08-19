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

from infisicalapi_client.models.api_v1_workspace_workspace_id_trusted_ips_post_request import ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest  # noqa: E501

class TestApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest(unittest.TestCase):
    """ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest:
        """Test ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest`
        """
        model = ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest()  # noqa: E501
        if include_optional:
            return ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest(
                ip_address = '',
                comment = '',
                is_active = True
            )
        else:
            return ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest(
                ip_address = '',
                is_active = True,
        )
        """

    def testApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest(self):
        """Test ApiV1WorkspaceWorkspaceIdTrustedIpsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()