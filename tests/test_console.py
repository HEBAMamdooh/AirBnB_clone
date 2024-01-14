#!/usr/bin/python3
"""Unittests for console module"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test the console"""

    def setUp(self):
        """Setup for the test"""
        self.console = HBNBCommand()
        self.storage = storage
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Teardown for the test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_create(self):
        """Test create command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State")
            state_id = mock_stdout.getvalue().strip()
            state = self.storage.all().get("State.{}".format(state_id))
            self.assertIsInstance(state, State)

    def test_show(self):
        """Test show command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State")
            state_id = mock_stdout.getvalue().strip()
            self.console.onecmd("show State {}".format(state_id))
            expected_output = "[State] ({}) {}".format(state_id,
                                                       str(self.storage.all()["State.{}".format(state_id)]))
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_destroy(self):
        """Test destroy command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State")
            state_id = mock_stdout.getvalue().strip()
            self.console.onecmd("destroy State {}".format(state_id))
            state = self.storage.all().get("State.{}".format(state_id))
            self.assertIsNone(state)

    def test_all(self):
        """Test all command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State")
            self.console.onecmd("create City")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("create Review")
            self.console.onecmd("all")
            expected_output = "[State] ({}) {}\n[City] ({}) {}\n[User] ({}) {}\n[Place] ({}) {}\n[Review] ({}) {}".format(
                list(self.storage.all()["State"].keys())[0],
                str(self.storage.all()["State"].values())[10:-1],
                list(self.storage.all()["City"].keys())[0],
                str(self.storage.all()["City"].values())[10:-1],
                list(self.storage.all()["User"].keys())[0],
                str(self.storage.all()["User"].values())[10:-1],
                list(self.storage.all()["Place"].keys())[0],
                str(self.storage.all()["Place"].values())[10:-1],
                list(self.storage.all()["Review"].keys())[0],
                str(self.storage.all()["Review"].values())[10:-1]
            )
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_update(self):
        """Test update command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State")
            state_id = mock_stdout.getvalue().strip()
            self.console.onecmd(
                'update State {} name "California"'.format(state_id))
            self.console.onecmd("show State {}".format(state_id))
            expected_output = "[State] ({}) {}".format(state_id,
                                                       str(self.storage.all()["State.{}".format(state_id)]))
            self.assertIn("California", mock_stdout.getvalue().strip())

    def test_all_instances_by_class_name(self):
        """Test all instances by class name command"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create State")
            self.console.onecmd("create City")
            self.console.onecmd("create User")
            self.console.onecmd("create Place")
            self.console.onecmd("create Review")
            self.console.onecmd("State.all()")
            expected_output = "[State] ({}) {}".format(
                list(self.storage.all()["State"].keys())[0],
                str(self.storage.all()["State"].values())[10:-1]
            )
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)


if __name__ == "__main__":
    unittest.main()
