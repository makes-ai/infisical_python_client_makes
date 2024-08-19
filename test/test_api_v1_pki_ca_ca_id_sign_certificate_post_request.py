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

from infisicalapi_client.models.api_v1_pki_ca_ca_id_sign_certificate_post_request import ApiV1PkiCaCaIdSignCertificatePostRequest  # noqa: E501

class TestApiV1PkiCaCaIdSignCertificatePostRequest(unittest.TestCase):
    """ApiV1PkiCaCaIdSignCertificatePostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiV1PkiCaCaIdSignCertificatePostRequest:
        """Test ApiV1PkiCaCaIdSignCertificatePostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiV1PkiCaCaIdSignCertificatePostRequest`
        """
        model = ApiV1PkiCaCaIdSignCertificatePostRequest()  # noqa: E501
        if include_optional:
            return ApiV1PkiCaCaIdSignCertificatePostRequest(
                csr = '0',
                friendly_name = '',
                common_name = '0',
                alt_names = '',
                ttl = '',
                not_before = '',
                not_after = ''
            )
        else:
            return ApiV1PkiCaCaIdSignCertificatePostRequest(
                csr = '0',
                ttl = '',
        )
        """

    def testApiV1PkiCaCaIdSignCertificatePostRequest(self):
        """Test ApiV1PkiCaCaIdSignCertificatePostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()