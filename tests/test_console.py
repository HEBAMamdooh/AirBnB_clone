#!/usr/bin/python3
"""Unittest for HBNBCommand class"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test the console"""

    def setUp(self):
        """Set up for the test"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down the test"""
        try:
            os.remove("file.json")
        except:
            pass

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit(self, mock_stdout):
        """Test quit command"""
        with patch('builtins.input', return_value="quit"):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, mock_stdout):
        """Test EOF command"""
        with patch('builtins.input', return_value="EOF"):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        """Test emptyline command"""
        with patch('builtins.input', return_value=""):
            self.console.cmdloop()
            self.assertEqual(mock_stdout.getvalue(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test create command"""
        with patch('builtins.input', return_value="create BaseModel"):
            self.console.cmdloop()
            self.assertTrue(mock_stdout.getvalue() != "")
            self.assertTrue(len(storage.all()) == 1)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test show command"""
        with patch('builtins.input', return_value="create BaseModel"):
            self.console.cmdloop()
            obj_id = mock_stdout.getvalue().strip()
            mock_stdout.truncate(0)
            with patch('builtins.input', return_value="show BaseModel {}".format(obj_id)):
                self.console.cmdloop()
                self.assertTrue(mock_stdout.getvalue() != "")
                self.assertTrue(obj_id in mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test destroy command"""
        with patch('builtins.input', return_value="create BaseModel"):
            self.console.cmdloop()
            obj_id = mock_stdout.getvalue().strip()
            mock_stdout.truncate(0)
            with patch('builtins.input', return_value="destroy BaseModel {}".format(obj_id)):
                self.console.cmdloop()
                self.assertTrue(mock_stdout.getvalue() == "")
                self.assertTrue(obj_id not in storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test all command"""
        with patch('builtins.input', return_value="create BaseModel"):
            self.console.cmdloop()
            mock_stdout.truncate(0)
            with patch('builtins.input', return_value="all BaseModel"):
                self.console.cmdloop()
                self.assertTrue(mock_stdout.getvalue() != "")

    # Add similar test methods for other console commands (count, update, etc.)


if __name__ == "__main__":
    unittest.main()
