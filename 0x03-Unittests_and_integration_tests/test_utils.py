#!/usr/bin/env python3
""" This project module contains the first unit test
for utils.access_nested_map.
"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap inherits from unittest.TestCase to test
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
