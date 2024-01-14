#!/usr/bin/python3
"""
Module for FileStorage class.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class for serialization and deserialization of instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file (__file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserialize the JSON file (__file_path) to __objects."""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                loaded_objects = json.load(file)
                for key, obj_dict in loaded_objects.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
