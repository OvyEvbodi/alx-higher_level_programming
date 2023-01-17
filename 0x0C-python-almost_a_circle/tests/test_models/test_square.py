#!/usr/bin/python3

"""Tests that a ``Square`` class creates an instance of a Square object correctly"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json

class TestSquareClass(unittest.TestCase):
    """test class for the Square class"""

    def test_create_square(self):
        obj_1 = Square(3)
        obj_2 = Square(7)
        obj_3 = Square(1, 3, 4)
        self.assertTrue(obj_1)
        self.assertTrue(obj_2)
        self.assertTrue(obj_3)
        self.assertFalse(obj_1 is obj_2)
        self.assertIsNotNone(obj_3.__doc__)
        
    def test_missing_or_wrong_arg(self):
        obj_1 = Square(3)
        with self.assertRaises((ValueError, TypeError)):
            obj_2 = Square(5, -4, "i")
        with self.assertRaises((ValueError, TypeError)):
            obj_2 = Square(0, -[4], "i")
        with self.assertRaises(ValueError):
            obj_3 = Square(-1)
        with self.assertRaises(ValueError):
            obj_1.size = -2
        with self.assertRaises(TypeError):
            obj_1.x = (1, 3)
        with self.assertRaises(TypeError):
            obj_1.y = [2]
        with self.assertRaises(TypeError):
            obj_1 = Square(4, 6, 3, 2, 4)

    def test_inheritance(self):
        obj_1 = Square(4, 6, 3, 2)
        obj_2 = Square(8)
        self.assertEqual(obj_1.width, 4)
        self.assertNotEqual(obj_1.width, 6)
        self.assertEqual(obj_1.height, 4)
        self.assertNotEqual(obj_1.height, 6)
        self.assertTrue(isinstance(obj_2, Rectangle))
        self.assertTrue(isinstance(obj_1, Rectangle))
        self.assertTrue(isinstance(obj_1, Square))
        self.assertTrue(isinstance(obj_2, Square))
        self.assertTrue(isinstance(obj_1, Base))
        self.assertTrue(isinstance(obj_2, Base))
        self.assertFalse(isinstance(obj_2, int))
        self.assertFalse(isinstance(obj_2, dict))
        self.assertFalse(type(obj_2) == Base)
        self.assertFalse(type(obj_2) == Rectangle)
        self.assertTrue(type(obj_2) == Square)
        self.assertTrue(type(obj_1) == Square)
        self.assertIsNotNone(obj_2.id)

    def test_str(self):
        obj_1 = Square(2, 4, 5,68)

    def test_to_dictionary(self):
        obj_1 = Square(9)
        obj_2 = Square(3, 5, 6)
        obj_dict = obj_2.to_dictionary()
        self.assertEqual(type(obj_dict), dict)
        self.assertFalse(type(obj_dict) == str)
        self.assertIn('size', obj_dict)
        self.assertIn('x', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('y', obj_dict)
