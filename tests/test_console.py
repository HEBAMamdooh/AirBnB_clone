#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
import os
from models import storage
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test the console.py functionality"""

    def setUp(self):
        """Set up test environment"""
        self.hbnb_console = HBNBCommand()

    def tearDown(self):
        """Remove test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create_show_destroy(self):
        """Test create, show, and destroy commands"""
        with StringIO() as f, redirect_stdout(f):
            self.hbnb_console.onecmd("create User")
            user_id = f.getvalue().strip()

            self.hbnb_console.onecmd(f"show User {user_id}")
            self.assertIn(user_id, f.getvalue())

            self.hbnb_console.onecmd(f"destroy User {user_id}")
            self.assertNotIn(user_id, storage.all())

    def test_all_update(self):
        """Test all and update commands"""
        with StringIO() as f, redirect_stdout(f):
            self.hbnb_console.onecmd("create User")
            user_id = f.getvalue().strip()

            self.hbnb_console.onecmd("all User")
            self.assertIn(user_id, f.getvalue())

            self.hbnb_console.onecmd(f"update User {user_id} first_name Alice")
            self.hbnb_console.onecmd(f"show User {user_id}")
            self.assertIn("Alice", f.getvalue())

    def test_quit_EOF(self):
        """Test quit and EOF commands"""
        with self.assertRaises(SystemExit):
            self.hbnb_console.onecmd("quit")

        with self.assertRaises(SystemExit):
            self.hbnb_console.onecmd("EOF")


if __name__ == "__main__":
    unittest.main()
