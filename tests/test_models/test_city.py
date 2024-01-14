#!/usr/bin/python3
"""Test City Module"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test City class"""

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
