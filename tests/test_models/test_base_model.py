#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def test_instance_creation(self):
        """
        Test instance creation and attributes
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str_method(self):
        """
        Test the __str__ method of BaseModel
        """
        my_model = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), str_rep)

    def test_save_method(self):
        """
        Test the save method of BaseModel
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method of BaseModel
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        obj_dict = my_model.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["name"], "My First Model")
        self.assertEqual(obj_dict["my_number"], 89)


if __name__ == "__main__":
    unittest.main()
