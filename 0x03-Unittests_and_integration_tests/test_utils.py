#!/usr/bin/env python3
"""In this module, we write unittest to
test the utils.access_nested map"""


import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class Test Method that defines test_* methods
    for testing the function access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """Method to test the access nested map
        function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
