#!/usr/bin/python3
"""This module is for the test of the base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """This is the test class for the base class"""

    def setUp(self) -> None:
        """SEtup function for the test class"""
        Base._Base__nb_objects = 0

    def tearDown(self) -> None:
        """Clean up function for the test class"""
        Base._Base__nb_objects = 0

    def test_incrementing_id(self):
        """Test the incrementing of the id"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test the custom id"""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_nb_objects_with_no_and_id(self):
        """Test the __nb_objects"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b3 = Base()
        self.assertEqual(b3.id, 3)
