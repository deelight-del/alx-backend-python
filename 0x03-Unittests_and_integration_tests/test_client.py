#!/usr/bin/env python3
"""Module to parameterize and patch as decorators"""


import unittest
import client
import unittest.mock as mock
from parameterized import parameterized
import typing


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

    def test_public_repos_url(self):
        """Unit test of of the _public_repos_url of
        the GithubOrgClient class"""
        with mock.patch(
            "client.GithubOrgClient.org", callable=mock.PropertyMock
        ) as pm:
            pm.return_value = {"repos_url": True}
            actual_payload = client.GithubOrgClient("abc")._public_repos_url
            self.assertTrue(actual_payload)

    @parameterized.expand([
        (
            "abc",
            "abc.com",
            #  {"abc": {"name": "abc-payload", "license": "abcL"}},
            [{"name": "abc-payload", "license": "abcL"}],
            None,
            ["abc-payload"],
         ),
        (
            "abc",
            "abc.com",
            #  {"abc": {"name": "abc-payload", "license": {"key": "abcL"}}},
            [{"name": "abc-payload", "license": {"key": "abcL"}}],
            "abcL",
            ["abc-payload"]
         ),
        (
            "abc",
            "abc.com",
            #  {"abc": {"name": "abc-payload", "license": "abcL"}},
            [{"name": "abc-payload", "license": "abcL"}],
            "abcL",
            []
         )
        # ("google", "google.xy", [{"name": "google-payload"}], None, [])
    ])
    @mock.patch("client.get_json")
    def test_public_repos(
        self,
        mock_org_name: str,
        mock_url: str,
        mock_json_payload: typing.Mapping,
        mock_license: str,
        expected_list: typing.List,
        mock_get_json: mock.Mock
        ):
        """Method to test the public_repos method
        of the GithubOrgClient"""
        mock_get_json.configure_mock(**{
            "return_value": mock_json_payload
        })
        with mock.patch(
            "client.GithubOrgClient._public_repos_url",
            callable=mock.PropertyMock
        ) as pm:
            pm.return_value = mock_url
            #  mock_get_json.side_effect = pm
            pm()
            gh_instance = client.GithubOrgClient(mock_org_name)
            actual_list = gh_instance.public_repos(mock_license)
        self.assertSequenceEqual(expected_list, actual_list)
        pm.assert_called_once()
        mock_get_json.assert_called_once()
