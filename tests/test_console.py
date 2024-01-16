#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb_cmd = HBNBCommand()

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Assuming the ID is a UUID

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertTrue(obj_id in output)

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd(f"destroy BaseModel {obj_id}")

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(obj_id in output)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd(f"update BaseModel {obj_id} name 'NewName'")

        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertTrue("NewName" in output)


if __name__ == '__main__':
    unittest.main()
