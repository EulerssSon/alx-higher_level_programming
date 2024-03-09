#!/usr/bin/python3
"""This module is to test Rectangle class"""
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangleClass(unittest.TestCase):
    """This is the class to test the
    Rectangle class"""

    def setUp(self) -> None:
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(10, 2, 0, 0, 13)

    def tearDown(self) -> None:
        Base._Base__nb_objects = 0

    def test_id(self):
        """This is to test the id attribute"""
        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertEqual(self.r4.id, 13)

    def test2ArgsRectangle(self):
        new_rect = Rectangle(8, 7)
        self.assertEqual(new_rect.width, 8)
        self.assertEqual(new_rect.height, 7)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 3)

    def test3ArgsRectangle(self):
        new_rect = Rectangle(8, 7, 0)
        self.assertEqual(new_rect.width, 8)
        self.assertEqual(new_rect.height, 7)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 3)

    def test4ArgsRectangle(self):
        new_rect = Rectangle(8, 7, 0, 0)
        self.assertEqual(new_rect.width, 8)
        self.assertEqual(new_rect.height, 7)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 3)

    def test5ArgsRectangle(self):
        new_rect = Rectangle(8, 7, 0, 0, 55)
        self.assertEqual(new_rect.width, 8)
        self.assertEqual(new_rect.height, 7)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 55)

    def test5ArgsRectangle(self):
        new_rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(new_rect.width, 8)
        self.assertEqual(new_rect.height, 7)
        self.assertEqual(new_rect.x, 0)
        self.assertEqual(new_rect.y, 0)
        self.assertEqual(new_rect.id, 12)

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

    def testMakeRectWithWrongAttrValuorType(self):
        with self.assertRaises(ValueError):
            new_rect = Rectangle(8, 7, 0, -1, 12)
        with self.assertRaises(TypeError):
            new_rect = Rectangle(8, 7, 0, 1.5, 12)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(0, 7, 0, 1, 12)
        with self.assertRaises(TypeError):
            new_rect = Rectangle("hello", 7, 0, 1, 12)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(-8, 7, 0, 1, 12)
        with self.assertRaises(TypeError):
            new_rect = Rectangle(8, "hello", 0, 1, 12)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(8, -7, 0, 1, 12)
        with self.assertRaises(TypeError):
            new_rect = Rectangle(8, 7, "hello", 1, 12)
        with self.assertRaises(TypeError):
            new_rect = Rectangle(8, 7, 0, "hello", 12)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(8, 7, 0, -1, 12)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            new_rect = Rectangle(1, 2, -55)

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

    def test_area(self):
        """This is to test the area method"""
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)
        self.assertEqual(self.r4.area(), 20)

        new_rect = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(new_rect.area(), 56)
        new_rect.width = 10
        self.assertEqual(new_rect.area(), 70)

    def test___str__(self):
        """This is to test the __str__ method"""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 0/0 - 2/10")
        self.assertEqual(str(self.r3), "[Rectangle] (12) 0/0 - 10/2")
        self.assertEqual(str(self.r4), "[Rectangle] (13) 0/0 - 10/2")

    def test_display_rect_withXY(self):
        """This is to test the display method"""
        r1 = Rectangle(2, 3, 2, 2, 12)
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_rect_withoutXY(self):
        """This is to test the display method"""
        r1 = Rectangle(2, 3)
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "##\n##\n##\n")

    def test_display_rect_withX(self):
        """This is to test the display method"""
        r1 = Rectangle(2, 3, 2)
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "  ##\n  ##\n  ##\n")

    def test_update0(self):
        """This is to test the update method"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update1(self):
        """This is to test the update method with args && kwargs"""
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(89, 2, 3, 4, 5, id=90)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(89, 2, 3, 4, 5, id=90, x=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(89, 2, 3, 4, 5, id=90, x=1, y=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        # if args is not empty, kwargs is not used
        r1.update(89, 2, 3, 4, 5, id=90, x=1, y=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(89, 2, 3, 4, 5, id=90, x=1, y=1, width=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(89, 2, 3, 4, 5, id=90, x=1, y=1, width=1, height=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        # if args is empty, kwargs is used
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (89) 2/5 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")
