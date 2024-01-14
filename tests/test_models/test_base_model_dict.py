#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModelDict(unittest.TestCase):
    """Test cases for BaseModel class with dictionary representation."""

    def test_base_model_dict_creation(self):
        """Test if a BaseModel instance is created successfully from a dictionary."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_dict = my_model.to_dict()

        my_new_model = BaseModel(**my_model_dict)

        self.assertIsInstance(my_new_model, BaseModel)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertFalse(my_model is my_new_model)


if __name__ == '__main__':
    unittest.main()
