#!/usr/bin/python3
"""Unit tests for saving and reloading BaseModel instances."""
import unittest
from models import storage
from models.base_model import BaseModel


class TestSaveReloadBaseModel(unittest.TestCase):
    """Test cases for saving and reloading BaseModel instances."""

    def test_save_reload_base_model(self):
        """Test saving and reloading of BaseModel instances."""
        all_objs_before = storage.all()
        print("-- Reloaded objects before --")
        for obj_id in all_objs_before.keys():
            obj = all_objs_before[obj_id]
            print(obj)

        print("-- Create a new object --")
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        all_objs_after = storage.all()
        print("-- Reloaded objects after --")
        for obj_id in all_objs_after.keys():
            obj = all_objs_after[obj_id]
            print(obj)

        self.assertIsInstance(my_model, BaseModel)
        self.assertIn(my_model, all_objs_after.values())
        self.assertNotEqual(all_objs_before, all_objs_after)


if __name__ == '__main__':
    unittest.main()
