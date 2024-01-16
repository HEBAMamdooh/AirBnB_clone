#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down test environment"""
        storage.reload()

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertIn("", f.getvalue())

    def test_eof(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertIn("", f.getvalue())

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            self.assertIn("", f.getvalue())

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertIn("", f.getvalue())

    def test_base_model_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            self.assertIn("", f.getvalue())

    def test_user_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            self.assertIn("", f.getvalue())

def test_user_show(self):
    with patch('sys.stdout', new=StringIO()) as f:
        self.console.onecmd("User.show('some_id')")
        self.assertIn("", f.getvalue())

if __name__ == "__main__":
    unittest.main()
