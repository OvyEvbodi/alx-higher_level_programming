#!/usr/bin/python3

"""unit testing for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests that the function ``max_integer`` works as expected"""
    def test_max(self):
        self.assertEqual(max_integer([7, 8]), 8)
        self.assertEqual(max_integer([-7, -8]), -7)
        self.assertEqual(max_integer([0, 10]), 10)

    def test_empty_arg(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_arg_is_list(self):
        with self.assertRaises(TypeError):
            max_integer(9)
        with self.assertRaises(TypeError):
            max_integer(8.9)
        with self.assertRaises(KeyError):
            max_integer({"one": 68, "two": 200})
