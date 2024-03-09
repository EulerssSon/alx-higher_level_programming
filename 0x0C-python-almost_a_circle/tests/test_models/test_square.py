#!/usr/bin/python3
"""This module is class that inherits from the rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is a class to test the square class"""

    def setUp(self) -> None:
        """This is the setup for the test cases"""
        self.s1 = Square(5)
        self.s2 = Square(4, 8)
        self.s3 = Square(3, 4, 5)
        self.s4 = Square(2, 3, 4, 6)

    def tearDown(self) -> None:
        """This is the teardown for the test cases"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """This is a test for the id of the square"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 6)

    def test_x(self):
        """This is a test for the x coordinate of the square"""
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 8)
        self.assertEqual(self.s3.x, 4)
        self.assertEqual(self.s4.x, 3)

    def test_x_setter(self):
        """This is a test for the x coordinate setter of the square"""
        self.s1.x = 3
        self.assertEqual(self.s1.x, 3)
        self.s2.x = 5
        self.assertEqual(self.s2.x, 5)
        self.s3.x = 6
        self.assertEqual(self.s3.x, 6)
        self.s4.x = 7
        self.assertEqual(self.s4.x, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.s1.x = "hello"
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.s2.x = -1

    def test_y(self):
        """This is a test for the y coordinate of the square"""
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 5)
        self.assertEqual(self.s4.y, 4)

    def test_y_setter(self):
        """This is a test for the y coordinate setter of the square"""
        self.s1.y = 3
        self.assertEqual(self.s1.y, 3)
        self.s2.y = 5
        self.assertEqual(self.s2.y, 5)
        self.s3.y = 6
        self.assertEqual(self.s3.y, 6)
        self.s4.y = 7
        self.assertEqual(self.s4.y, 7)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.s1.y = "hello"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s2.y = -1

    def test_str(self):
        """This is a test for the str method of the square"""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(self.s2), "[Square] (2) 8/0 - 4")
        self.assertEqual(str(self.s3), "[Square] (3) 4/5 - 3")
        self.assertEqual(str(self.s4), "[Square] (6) 3/4 - 2")

    def test_size(self):
        """This is a test for the size of the square"""
        self.assertEqual(self.s1.size, 5)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s3.size, 3)
        self.assertEqual(self.s4.size, 2)

    def test_size_setter(self):
        """This is a test for the size setter of the square"""
        self.s1.size = 3
        self.assertEqual(self.s1.size, 3)
        self.s2.size = 6
        self.assertEqual(self.s2.size, 6)
        self.s3.size = 7
        self.assertEqual(self.s3.size, 7)
        self.s4.size = 8
        self.assertEqual(self.s4.size, 8)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s1.size = "hello"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.s2.size = 0
