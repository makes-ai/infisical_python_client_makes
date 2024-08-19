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

from infisicalapi_client.models.api_v1_additional_privilege_identity_patch_request_privilege_details import ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails  # noqa: E501

class TestApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails(unittest.TestCase):
    """ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails:
        """Test ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails`
        """
        model = ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails()  # noqa: E501
        if include_optional:
            return ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails(
                slug = '0',
                permissions = [
                    infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner._api_v1_workspace__projectSlug__roles_post_request_permissions_inner(
                        action = 'read', 
                        subject = 'role', 
                        conditions = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner_conditions._api_v1_workspace__projectSlug__roles_post_request_permissions_inner_conditions(
                            environment = '', 
                            secret_path = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner_conditions_secret_path._api_v1_workspace__projectSlug__roles_post_request_permissions_inner_conditions_secretPath(
                                __glob = '0', ), ), )
                    ],
                privilege_permission = infisicalapi_client.models._api_v1_additional_privilege_identity_permanent_post_request_privilege_permission._api_v1_additional_privilege_identity_permanent_post_request_privilegePermission(
                    actions = [
                        'read'
                        ], 
                    subject = 'secrets', 
                    conditions = infisicalapi_client.models._api_v1_additional_privilege_identity_permanent_post_request_privilege_permission_conditions._api_v1_additional_privilege_identity_permanent_post_request_privilegePermission_conditions(
                        environment = '', 
                        secret_path = infisicalapi_client.models._api_v1_workspace__project_slug__roles_post_request_permissions_inner_conditions_secret_path._api_v1_workspace__projectSlug__roles_post_request_permissions_inner_conditions_secretPath(
                            __glob = '0', ), ), ),
                is_temporary = True,
                temporary_mode = 'relative',
                temporary_range = '',
                temporary_access_start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails(
        )
        """

    def testApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails(self):
        """Test ApiV1AdditionalPrivilegeIdentityPatchRequestPrivilegeDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()