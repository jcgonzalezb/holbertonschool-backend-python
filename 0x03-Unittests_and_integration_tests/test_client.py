#!/usr/bin/env python3
""" This project module contains the first unit test
for utils.access_nested_map.
"""

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ TestAccessNestedMap inherits from unittest. TestCase to test
    utils.access_nested_map.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_org(self, nested_map, path, expected_result):
        """ Tests that GithubOrgClient.org returns the correct value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
