#!/usr/bin/env python3
""" This project module contains the first unit test
for utils.access_nested_map.
"""

import unittest
import requests
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap inherits from unittest. TestCase to test
    utils.access_nested_map.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Tests if access_nested_map method returns what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Tests if access_nested_map method raise an exception.
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """ TestAccessNestedMap inherits from unittest. TestCase to test
    utils.get_json.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Tests if get_json method returns the expected result.
        """
        with patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock.assert_called_once()


if __name__ == "__main__":
    unittest.main()
