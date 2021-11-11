#!/user/bin/python3
""" Test file for the base_model class"""
import unittest
from models.base_model import BaseModel
import models
import json
import os


class TestClass(unittest.TestCase):
    """ Test cases"""

    def setUp(self):
        self.model = BaseModel()
        return super().setUp()

    def tearDown(self):
        del (self.model)
        if os.path.exists("file.json"):
            os.remove("file.json")
            return models.storage.reset()
        return super().tearDown()

    def test_create_istance(self):
        """ Test case init instance"""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        self.model.save()

        file = 'fiel.json'
        with open(file, mode="r+", encoding="utf-8") as f:
            file_string = f.read()
            data = json.loads(file_string)

        self.assertTrue('{}.{}'
                        .format(type(self.model).__name__, self.model.id)
                        )

        self.assertDictEqual(self.model.to_dict(), data[
            '{}.{}'.format(type(self.model).__name__, self.model.id)]
        )

    def test_assign_attribute(self):
        """Test new attribute"""
        self.model.name = "My_First_Model"
        self.model.my_number = 89
        self.assertIs(self.model.name, "My_First_Model")
        self.assertIs(self.model.my_number, 89)


if __name__ == '__main__':
    unittest.main()