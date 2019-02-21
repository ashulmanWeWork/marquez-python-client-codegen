# coding: utf-8

"""
    Marquez

    Marquez is an open source **metadata service** for the **collection**, **aggregation**, and **visualization** of a data ecosystem's metadata.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import marquez_codegen_client
from marquez_codegen_client.api.namespaces_api import NamespacesApi  # noqa: E501
from marquez_codegen_client.rest import ApiException


class TestNamespacesApi(unittest.TestCase):
    """NamespacesApi unit test stubs"""

    def setUp(self):
        self.api = marquez_codegen_client.api.namespaces_api.NamespacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_namespaces_get(self):
        """Test case for namespaces_get

        List all namespaces  # noqa: E501
        """
        pass

    def test_namespaces_namespace_get(self):
        """Test case for namespaces_namespace_get

        Retrieve a namespace  # noqa: E501
        """
        pass

    def test_namespaces_namespace_put(self):
        """Test case for namespaces_namespace_put

        Create a namespace  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
