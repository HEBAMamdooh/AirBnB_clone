#!/usr/bin/python3
"""Unittests for User class"""
import unittest
import os
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def tearDown(self):
        """Remove test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test instance creation and attributes"""
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_save_reload_user(self):
        """Test saving and reloading User instance"""
        self.user.first_name = "John"
        self.user.email = "john@mail.com"
        self.user.password = "pass123"
        self.user.save()

        all_objs = storage.all()
        user_key = "User." + self.user.id
        self.assertTrue(user_key in all_objs)
        reloaded_user = all_objs[user_key]
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.email, "john@mail.com")
        self.assertEqual(reloaded_user.password, "pass123")

    def test_create_new_user(self):
        """Test creating a new User instance"""
        new_user = User()
        new_user.first_name = "Alice"
        new_user.email = "alice@mail.com"
        new_user.password = "alicepass"
        new_user.save()

        all_objs = storage.all()
        new_user_key = "User." + new_user.id
        self.assertTrue(new_user_key in all_objs)
        reloaded_new_user = all_objs[new_user_key]
        self.assertEqual(reloaded_new_user.first_name, "Alice")
        self.assertEqual(reloaded_new_user.email, "alice@mail.com")
        self.assertEqual(reloaded_new_user.password, "alicepass")


if __name__ == "__main__":
    unittest.main()
