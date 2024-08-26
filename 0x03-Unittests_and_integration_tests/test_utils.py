#!/usr/bin/env python3
"""0. Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), f"'{path[-1]}'")

if __name__ == "__main__":
    unittest.main()
2. Unit Test for utils.get_json
python
Copy code
import unittest
from unittest.mock import patch, Mock
from utils import get_json

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch('utils.requests.get', return_value=mock_response) as mock_get:
            response = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(response, test_payload)

if __name__ == "__main__":
    unittest.main()
