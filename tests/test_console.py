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

    def test_do_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.hbnb_cmd.onecmd("EOF")
            output = f.getvalue().strip()
            self.assertTrue("exiting..." in output)

    def test_do_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                self.hbnb_cmd.onecmd("quit")
            output = f.getvalue().strip()
            self.assertTrue("exiting..." in output)

    def test_emptyline_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.hbnb_cmd.onecmd("")
            output = f.getvalue().strip()
            self.assertTrue(output == "")

    def test_check_for_braces(self):
        # Test when braces are present
        result = self.hbnb_cmd.check_for_braces(
            "some_command({key: 'value'})", "{", "}")
        self.assertEqual(result, (13, 28))

        # Test when braces are not present
        result = self.hbnb_cmd.check_for_braces(
            "some_command(key='value')", "{", "}")
        self.assertEqual(result, (False, False))

    def test_get_list_of_args(self):
        # Test case with all arguments
        command = "User.update('123', 'name', 'John')"
        result = self.hbnb_cmd.get_list_of_args(command)
        self.assertEqual(result, ('User', 'update', '123', 'name', 'John'))

        # Test case without optional arguments
        command = "User.update('123', 'name', 'John')"
        result = self.hbnb_cmd.get_list_of_args(command)
        self.assertEqual(result, ('User', 'update', '123', 'name', 'John'))

    def test_default_method(self):
        with patch('sys.stdout', new=StringIO()) as f:
            # Test update command
            self.hbnb_cmd.default("BaseModel.update('123', 'name', 'John')")
            output = f.getvalue().strip()
            self.assertTrue("** no instance found **" in output)

        with patch('sys.stdout', new=StringIO()) as f:
            # Test unknown syntax
            self.hbnb_cmd.default("InvalidSyntax")
            output = f.getvalue().strip()
            self.assertTrue("*** Unknown syntax: InvalidSyntax" in output)

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

    def test_base_model_all(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("BaseModel.all()")
            output = mock_stdout.getvalue().strip()
            # Replace this with the expected output for BaseModel.all()
            expected_output = "Expected Output for BaseModel.all()"
            self.assertIn(expected_output, output)

if __name__ == '__main__':
    unittest.main()
