#!/usr/bin/env python3
""" This project module contains the first unit test
for client.py file.
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient inherits from unittest. TestCase to test
    client.GithubOrgClient.
    """
    @parameterized.expand([
        ("google", {}),
        ("abc", {})
    ])
    @patch('client.get_json')
    def test_org(self, url, expected_result, mock):
        """ Tests that GithubOrgClient.org returns the correct value.
        """
        mock.return_value = {}
        r = GithubOrgClient(url)
        self.assertEqual(r.org, expected_result)
        mock.assert_called_once()

    def test_public_repos_url(self):
        """ Tests that _public_repos_url returns a known payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = {'repos_url': 'http://testing.url'}
            tg = GithubOrgClient('xyz')
            r = tg._public_repos_url
            self.assertEqual(r, mock.return_value.get('repos_url'))

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Tests that has_license returns the correct values.
        """
        gt = GithubOrgClient
        self.assertEqual(gt.has_license(repo, license_key), expected_result)


if __name__ == "__main__":
    unittest.main()
