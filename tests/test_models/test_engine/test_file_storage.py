#!/usr/bin/python3
"""Test FileStorage Module"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""

    def test_all(self):
        """Test all method"""
        fs = FileStorage()
        self.assertIsInstance(fs.all(), dict)

    def test_new(self):
        """Test new method"""
        fs = FileStorage()
        user = User()
        fs.new(user)
        key = "{}.{}".format(type(user).__name__, user.id)
        self.assertIn(key, fs.all())

    def test_save_reload_user(self):
        """Test save and reload method for User"""
        file_path = "file.json"
        user = User()
        user.first_name = "John"
        user.email = "john@example.com"
        user.password = "password123"
        user.save()

        fs1 = FileStorage()
        fs1.save()
        fs1.reload()
        user_key = "User.{}".format(user.id)
        self.assertIn(user_key, fs1.all())
        self.assertEqual(fs1.all()[user_key].first_name, "John")
        os.remove(file_path)


if __name__ == "__main__":
    unittest.main()
