#!/usr/bin/env python3
"""Module to parameterize and patch as decorators"""


import unittest
import client
import unittest.mock as mock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """The class to test the Github Org client
    and its methods."""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    @mock.patch('client.get_json')
    def test_org(self, test_url, test_payload, mock_get_json):
        """The function that tests the org method"""
        mock_get_json.configure_mock(**{
            "return_value": test_payload
        })
        gh_instance = client.GithubOrgClient(test_url)
        self.assertEqual(gh_instance.org, test_payload)
        self.assertEqual(gh_instance.org, test_payload)
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(test_url)
        )