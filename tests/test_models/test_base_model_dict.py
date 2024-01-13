#!/usr/bin/python3
"""
Unittest for BaseModel class with dictionary representation
"""

import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """
    Test cases for BaseModel class with dictionary representation
    """

    def test_dict_representation(self):
        """
        Test instance creation from dictionary representation
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        self.assertNotEqual(my_model, my_new_model)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)


if __name__ == "__main__":
    unittest.main()
