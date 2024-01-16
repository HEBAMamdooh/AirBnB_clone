#!/usr/bin/python3
"""
    TestConsole module
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import *


class TestConsoleFunction(unittest.TestCase):
    classes = ["User", "State", "Review", "Place", "City", "BaseModel"]
    actual_obj = None
    actual_id = ""
    actual_class = ""

    def test_create_new_obj(self):
        if len(storage.all()) != 6:
            for class_name in self.classes:
                with patch('sys.stdout', new=StringIO()) as f:
                    HBNBCommand().onecmd("create {}".format(class_name))
                    instance_after = len(storage.all())
                    self.actual_class = class_name
                    self.actual_id = f.getvalue()[:-1]
                    key_id = class_name + "." + self.actual_id
                    self.actual_obj = storage.all()[key_id]
                    self.assertNotEqual(self.actual_obj, None)
                    self.assertIn(self.actual_class, self.classes)

    def test_count_obj(self):
        """
            <class name>.count()
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.count()".format(class_name))
                count = 0
                for key, obj in storage.all().items():
                    if type(obj) is eval(class_name):
                        count += 1
                self.assertEqual(eval(f.getvalue()[:-1]), count)

    @staticmethod
    def get_first_occurence_by_class_name(class_name):
        """
            :return first occurence found
        """

        for key, val in storage.all().items():
            if type(val) is eval(class_name):
                return val

    @staticmethod
    def get_all_obj_by_classname(class_name):
        """
        :return all object found in storage
        """
        res = []
        for key, val in storage.all().items():
            if type(val) is eval(class_name):
                res.append(str(val))
        return res

    def test_show_obj(self):
        """
            <class name>.show(<id>)
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                obj = self.get_first_occurence_by_class_name(class_name)
                if obj:
                    HBNBCommand().onecmd("{}.show({})".format(
                        class_name,
                        obj.id))
                    HBNBCommand().onecmd("{}.show({})".format(class_name,
                                                              obj.id))
                    self.assertEqual(str(obj), f.getvalue()[:-1])

    def test_all_obj(self):
        """
            <class name>.all()
        """
        for class_name in self.classes:
            with patch('sys.stdout', new=StringIO()) as f:
                all_class_name = self.get_all_obj_by_classname(class_name)
                HBNBCommand().onecmd("{}.all()".format(class_name))
                self.assertEqual(all_class_name, eval(f.getvalue()))

    def test_destroy_obj(self):
        """
            <class name>.destroy(<id>)
        """

    def test_update_obj(self):
        """
            <class name>.update(<id>, <attribute name>, <attribute value>)
        """
        tests = {"t_int": 120, "t_list": ["id,1", "id,2"],
                 "t_str": "this is str", "t_float": 5.2}
        for class_name in self.classes:
            obj = self.get_first_occurence_by_class_name(class_name)
            for key, val in tests.items():
                with patch('sys.stdout', new=StringIO()) as f:
                    if obj:
                        HBNBCommand().onecmd(
                            "{}.update(\"{}\", \"{}\", {})".format(class_name,
                                                                   obj.id,
                                                                   key,
                                                                   val))
                        newval = getattr(obj, key)
                        self.assertEqual(type(val), type(newval))
                        self.assertEqual(val, newval)

        tests = {"number_rooms": 120, "amenity_ids": ["id,1", "id,2"],
                 "description": "this is str", "latitude": 5.2}
        obj = self.get_first_occurence_by_class_name("Place")
        for key, val in tests.items():
            with patch('sys.stdout', new=StringIO()) as f:
                if obj:
                    HBNBCommand().onecmd(
                        "{}.update(\"{}\", \"{}\", {})".format("Place",
                                                               obj.id,
                                                               key,
                                                               val))
                    newval = getattr(obj, key)
                    self.assertEqual(type(val), type(newval))
                    self.assertEqual(val, newval)
                    """
                    """
