#!/usr/bin/python3
"""Test Console Module"""

import unittest
import sys
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test HBNBCommand class"""

    def setUp(self):
        """Redirect stdout for testing"""
        self.console_stdout = StringIO()
        sys.stdout = self.console_stdout

    def tearDown(self):
        """Reset redirect."""
        sys.stdout = sys.__stdout__

    def test_quit(self):
        """Test quit command"""
        HBNBCommand().onecmd("quit")
        self.assertEqual(self.console_stdout.getvalue(), "")
