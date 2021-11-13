#!/usr/bin/python3

"""
Test file for city class
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def setup(self):
        self.city = City()
        return super().setUp()

    def tearDown(self):
        del(self.city)
        return super().tearDown()

    def test_create_istance(self):
        """create a new instance"""
        self.assertIsInstance(self.city, City)

    def test_create_istance_check_parent(self):
        """check if it;s instance of parent"""
        self.assertIsInstance(self.city, BaseModel)

    def test_class_attribut(self):
        """initialize class attribute"""
        self.city.name = "kigali"
        self.assertIs(self.city.name, 'Kigali')

    def test_parent_of_city(self):
        """check if ciy is parent of BaseModel"""
        self.assertEqual(isinstance(self.city, BaseModel), True)
