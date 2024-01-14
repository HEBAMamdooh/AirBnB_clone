#!/usr/bin/python3
"""Test User Module"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test User class"""

    def test_attributes(self):
        """Test User attributes"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
