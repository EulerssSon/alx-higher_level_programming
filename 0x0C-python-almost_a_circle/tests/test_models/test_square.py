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

    def test_update(self):
        """This is a test for the update method of the square"""
        new_s1 = Square(1, 1, 1, 1)
        new_s1.update(89)
        self.assertEqual(str(new_s1), "[Square] (89) 1/1 - 1")
        new_s1.update(89, 2)
        self.assertEqual(str(new_s1), "[Square] (89) 1/1 - 2")
        new_s1.update(89, 2, 3)
        self.assertEqual(str(new_s1), "[Square] (89) 3/1 - 2")
        new_s1.update(89, 2, 3, 4)
        self.assertEqual(str(new_s1), "[Square] (89) 3/4 - 2")
        # test with kwargs
        new_s1.update(size=1)
        self.assertEqual(str(new_s1), "[Square] (89) 3/4 - 1")
        new_s1.update(size=10, x=2)
        self.assertEqual(str(new_s1), "[Square] (89) 2/4 - 10")
        new_s1.update(y=3, size=2, x=1)
        self.assertEqual(str(new_s1), "[Square] (89) 1/3 - 2")
        new_s1.update(x=1, size=2, y=3, id=89)
        self.assertEqual(str(new_s1), "[Square] (89) 1/3 - 2")
        new_s1.update(1, id=89)
        self.assertEqual(str(new_s1), "[Square] (1) 1/3 - 2")
        new_s1.update(1, id=89, size=3)
        ss = Square(5,id=1)
        self.assertEqual(str(ss), "[Square] (1) 0/0 - 5")
        ss.update(10)
        self.assertEqual(str(ss), "[Square] (10) 0/0 - 5")
        ss.update(1, 2)
        self.assertEqual(str(ss), "[Square] (1) 0/0 - 2")
        ss.update(1, 2, 3)
        self.assertEqual(str(ss), "[Square] (1) 3/0 - 2")
        ss.update(1, 2, 3, 4)
        self.assertEqual(str(ss), "[Square] (1) 3/4 - 2")
        ss.update(x=12)
        self.assertEqual(str(ss), "[Square] (1) 12/4 - 2")
        ss.update(size=7, y=1)
        self.assertEqual(str(ss), "[Square] (1) 12/1 - 7")
        ss.update(size=7, id=98, y=1)
        self.assertEqual(str(ss), "[Square] (98) 12/1 - 7")

    def testSquareWithWrongAttr(self):
        """This is a test for the square with wrong attributes"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "hello")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_to_dictionary(self):
        """This is a test for the to_dictionary method of the square"""
        self.assertEqual(self.s1.to_dictionary(), {'id': 1, 'size': 5, 'x': 0, 'y': 0})
        self.assertEqual(self.s2.to_dictionary(), {'id': 2, 'size': 4, 'x': 8, 'y': 0})
        self.assertEqual(self.s3.to_dictionary(), {'id': 3, 'size': 3, 'x': 4, 'y': 5})
        self.assertEqual(self.s4.to_dictionary(), {'id': 6, 'size': 2, 'x': 3, 'y': 4})

    def test_to_json_string(self):
        """This is a test for the to_json_string method of the square"""
        self.assertEqual(Square.to_json_string([{'id': 1, 'size': 5, 'x': 0, 'y': 0}]), '[{"id": 1, "size": 5, "x": 0, "y": 0}]')
        self.assertEqual(Square.to_json_string([{'id': 2, 'size': 4, 'x': 8, 'y': 0}]), '[{"id": 2, "size": 4, "x": 8, "y": 0}]')
        self.assertEqual(Square.to_json_string([{'id': 3, 'size': 3, 'x': 4, 'y': 5}]), '[{"id": 3, "size": 3, "x": 4, "y": 5}]')
        self.assertEqual(Square.to_json_string([{'id': 6, 'size': 2, 'x': 3, 'y': 4}]), '[{"id": 6, "size": 2, "x": 3, "y": 4}]')
        self.assertEqual(Square.to_json_string([]), '[]')
        self.assertEqual(Square.to_json_string(None), '[]')
