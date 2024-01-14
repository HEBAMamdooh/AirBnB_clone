#!/usr/bin/python3
"""Test State Module"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test State class"""

    def test_attributes(self):
        """Test State attributes"""
        state = State()
        self.assertEqual(state.name, "")
