#!/usr/bin/env python3
"""Module to parameterize and patch as decorators"""


import unittest
import client
import unittest.mock as mock
from parameterized import parameterized, parameterized_class
import typing
from fixtures import TEST_PAYLOAD
import requests


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
            [{"name": "abc-payload", "license": {"key": "abcL"}},
             {'name': "payload-2"}],
            None,
            ["abc-payload", "payload-2"]
         )
    ])
    @mock.patch("client.get_json")
    def test_public_repos(
            self,
            mock_org_name: str,
            mock_url: str,
            mock_json_payload: typing.Mapping,
            mock_license: str,
            expected_list: typing.List,
            mock_get_json: mock.Mock) -> None:

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
            gh_instance = client.GithubOrgClient(mock_org_name)
            actual_list = gh_instance.public_repos(mock_license)
        self.assertSequenceEqual(expected_list, actual_list)
        # pm.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: typing.Mapping,
                         license_key: str, expected: bool) -> None:
        """test method to test of has_license method"""
        self.assertEqual(
            client.GithubOrgClient("random").has_license(
                repo, license_key
            ),
            expected
        )


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"), [
    (
        TEST_PAYLOAD[0][0],
        TEST_PAYLOAD[0][1],
        TEST_PAYLOAD[0][2],
        TEST_PAYLOAD[0][3]
     )
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Class for integration testing."""
    @classmethod
    def setUpClass(cls):
        """Set up class"""
        # Define a side_effect function on the patch
        # that returns different mock payloads depending on
        # the url passed to the mock.
        # Note: The payload returned in the side_effect is a
        # mock object that has a `json.return_value` attr`.
        # This kind of construction perfectly simulates/mock the
        # request.get(url).json().
        side_effect = (
            lambda x: mock.Mock(**{"json.return_value": cls.org_payload})
            if x == "https://api.github.com/orgs/google"
            else (
                    mock.Mock(**{"json.return_value": cls.repos_payload})
                    if x == "https://api.github.com/orgs/google/repos"
                    else None
                )
        )

        # else in this case is when x is
        # https://api.github.com/orgs/google/repos
        cls.get_patcher = mock.patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Method to test that all the functions before public_repos that
        use requests.get work properly, if the right
        document is returned"""
        self.assertSequenceEqual(
                client.GithubOrgClient("google").public_repos(),
                self.expected_repos
        )

    def test_public_repos_with_apache_license(self):
        """Method to test that only payload with apache2-license
        is returned when license of repos_url is given as apache-2"""
        self.assertSequenceEqual(
            client.GithubOrgClient("google").public_repos("apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls):
        """Tear down class"""
        cls.get_patcher.stop()
