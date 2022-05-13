#!/usr/bin/env python3
""" This project module contains the first unit test
for utils.access_nested_map.
"""
from parameterized import parameterized
import unittest
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap inherits from unittest.TestCase to test
    utils.access_nested_map.
    """
    @parameterized.expand(
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b")
    )

    def TestAccessNestedMap(self, nested_map, path):
        """ Method to test that the method returns what it is supposed to.
        """
        self.assertEqual(nested_map, path)


if __name__ == '__main__':
    unittest.main()
