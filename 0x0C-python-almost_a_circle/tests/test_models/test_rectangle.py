"""This module is to test Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """This is the class to test the
    Rectangle class"""

    def setUp(self) -> None:
        """This is the setup for the test"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(10, 2, 0, 0, 13)

    def tearDown(self) -> None:
        """This is the clean up for the test"""
        del self.r1
        del self.r2
        del self.r3
        del self.r4

    def test_width(self):
        """This is to test the width attribute"""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)
        self.assertEqual(self.r4.width, 10)

    def test_width_setter(self):
        """This is to test the width setter"""
        with self.assertRaises(TypeError):
            self.r1.width = "hello"
        with self.assertRaises(ValueError):
            self.r1.width = -1
        with self.assertRaises(TypeError):
            self.r1.width = 1.5
        with self.assertRaises(ValueError):
            self.r1.width = 0

    def test_height(self):
        """This is to test the height attribute"""
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r4.height, 2)

    def test_height_setter(self):
        """This is to test the height setter"""
        with self.assertRaises(TypeError):
            self.r1.height = "hello"
        with self.assertRaises(ValueError):
            self.r1.height = -1
        with self.assertRaises(TypeError):
            self.r1.height = 1.5
        with self.assertRaises(ValueError):
            self.r1.height = 0

    def test_x(self):
        """This is to test the x attribute"""
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 0)
        self.assertEqual(self.r4.x, 0)

    def test_x_setter(self):
        """This is to test the x setter"""
        with self.assertRaises(TypeError):
            self.r1.x = "hello"
        with self.assertRaises(ValueError):
            self.r1.x = -1
        with self.assertRaises(TypeError):
            self.r1.x = 1.5

    def test_y(self):
        """This is to test the y attribute"""
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 0)
        self.assertEqual(self.r4.y, 0)

    def test_y_setter(self):
        """This is to test the y setter"""
        with self.assertRaises(TypeError):
            self.r1.y = "hello"
        with self.assertRaises(ValueError):
            self.r1.y = -1
        with self.assertRaises(TypeError):
            self.r1.y = 1.5
