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

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertIn("BaseModel.", f.getvalue())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertIn("BaseModel", f.getvalue())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertEqual(storage.all(), {})

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
            self.console.onecmd("all")
            output = f.getvalue().strip()
            self.assertIn("BaseModel", output)
            self.assertIn("User", output)

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
            self.console.onecmd(f"update BaseModel {obj_id} name 'new_name'")
            self.console.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertIn("new_name", output)


if __name__ == "__main__":
    unittest.main()
