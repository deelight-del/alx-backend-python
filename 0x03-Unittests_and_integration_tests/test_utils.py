#!/usr/bin/env python3
"""In this module, we write unittest to
test the utils.access_nested map"""


import unittest
import unittest.mock as mock
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map, get_json, memoize
import inspect


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence) -> None:
        """Method to test the exception of the access_nested function"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class implementation to test the
    the requests.get method of the request class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Mapping) -> None:
        # Run a context manager that mocks the requests.get
        # method from the utils class (where it is going to be exec)
        # check mock doc.
        # Also mock return_value of the json method equal to test_payload.
        with mock.patch("utils.requests.get",
                        new_callable=mock.Mock,
                        ) as mock_object:
            mock_object.return_value.json.return_value = test_payload
            test_result = get_json(test_url)
            mock_object.assert_called_once_with(test_url)
            self.assertEqual(test_result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class implementation to test the memoize function
    and its interactions"""
    def test_memoize(self):
        class TestClass:
            """A test class"""
            def a_method(self):
                """Some method"""
                return 42

            @memoize
            def a_property(self):
                """A property method"""
                return self.a_method()
        with mock.patch.object(TestClass, 'a_method') as mock_object:
            mock_object.return_value = 42
            instance = TestClass()
            first_call = instance.a_property
            second_call = instance.a_property
            self.assertEqual(second_call, 42)
            mock_object.assert_called_once()
