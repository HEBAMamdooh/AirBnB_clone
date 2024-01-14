#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class."""

    def test_base_model_creation(self):
        """Test if a BaseModel instance is created successfully."""
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_base_model_str_method(self):
        """Test the __str__ method of BaseModel."""
        my_model = BaseModel()
        string_repr = "[BaseModel] ({}) {}".format(
            my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), string_repr)

    def test_base_model_save_method(self):
        """Test the save method of BaseModel."""
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(original_updated_at, my_model.updated_at)

    def test_base_model_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         my_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
