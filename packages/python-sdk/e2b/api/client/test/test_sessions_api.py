# coding: utf-8

"""
    Devbook

    Devbook API  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import e2b.api.client
from e2b.api.client.api.sessions_api import SessionsApi  # noqa: E501
from e2b.api.client.rest import ApiException


class TestSessionsApi(unittest.TestCase):
    """SessionsApi unit test stubs"""

    def setUp(self):
        self.api = e2b.api.client.api.sessions_api.SessionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sessions_get(self):
        """Test case for sessions_get"""
        pass

    def test_sessions_post(self):
        """Test case for sessions_post"""
        pass

    def test_sessions_session_id_delete(self):
        """Test case for sessions_session_id_delete"""
        pass

    def test_sessions_session_id_refresh_post(self):
        """Test case for sessions_session_id_refresh_post"""
        pass


if __name__ == "__main__":
    unittest.main()
