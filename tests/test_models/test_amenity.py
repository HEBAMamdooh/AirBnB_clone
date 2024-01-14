#!/usr/bin/python3
"""Test Amenity Module"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
