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

    def test_same_type_as_attr_list(self):
        # Test case with a valid list
        result = self.hbnb_cmd.same_type_as_attr('[1, 2, 3]', list)
        self.assertEqual(result, [1, 2, 3])

        # Test case with a list containing non-string elements
        result = self.hbnb_cmd.same_type_as_attr('[1, "2", 3]', list)
        self.assertFalse(result)

        # Test case with invalid list syntax
        result = self.hbnb_cmd.same_type_as_attr('not_a_list', list)
        self.assertFalse(result)

    def test_same_type_as_attr_str(self):
        # Test case with a valid string
        result = self.hbnb_cmd.same_type_as_attr('hello', str)
        self.assertEqual(result, 'hello')

    def test_same_type_as_attr_int(self):
        # Test case with a valid integer
        result = self.hbnb_cmd.same_type_as_attr('42', int)
        self.assertEqual(result, 42)

        # Test case with an invalid integer
        result = self.hbnb_cmd.same_type_as_attr('not_an_integer', int)
        self.assertFalse(result)

    def test_same_type_as_attr_float(self):
        # Test case with a valid float
        result = self.hbnb_cmd.same_type_as_attr('3.14', float)
        self.assertEqual(result, 3.14)

        # Test case with an invalid float
        result = self.hbnb_cmd.same_type_as_attr('not_a_float', float)
        self.assertFalse(result)

    def test_same_type_as_attr_invalid_type(self):
        # Test case with an invalid type
        result = self.hbnb_cmd.same_type_as_attr('value', object)
        self.assertFalse(result)

    def test_convert_new_val_int(self):
        # Test case with a valid integer
        result = self.hbnb_cmd.convert_new_val('42')
        self.assertEqual(result, 42)

        # Test case with an invalid integer
        result = self.hbnb_cmd.convert_new_val('not_an_integer')
        self.assertEqual(result, 'not_an_integer')

    def test_convert_new_val_float(self):
        # Test case with a valid float
        result = self.hbnb_cmd.convert_new_val('3.14')
        self.assertEqual(result, 3.14)

        # Test case with an invalid float
        result = self.hbnb_cmd.convert_new_val('not_a_float')
        self.assertEqual(result, 'not_a_float')

    def test_convert_new_val_list(self):
        # Test case with a valid list
        result = self.hbnb_cmd.convert_new_val('[1, 2, 3]')
        self.assertEqual(result, [1, 2, 3])

        # Test case with an invalid list
        result = self.hbnb_cmd.convert_new_val('not_a_list')
        self.assertEqual(result, 'not_a_list')

    def test_convert_new_val_other_types(self):
        # Test case with other types (should return the input unchanged)
        result = self.hbnb_cmd.convert_new_val('hello')
        self.assertEqual(result, 'hello')

        result = self.hbnb_cmd.convert_new_val('{"key": "value"}')
        self.assertEqual(result, '{"key": "value"}')

if __name__ == '__main__':
    unittest.main()
