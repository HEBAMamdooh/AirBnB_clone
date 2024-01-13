#!/usr/bin/python3
"""
Module containing the FileStorage class
"""

import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """
    FileStorage class for serializing and deserializing instances to and from JSON
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        json_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_dict = json.load(file)
                for key, obj_dict in json_dict.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    obj = cls(**obj_dict)
                    self.__objects[key] = obj


# Create a unique FileStorage instance for the application
storage = FileStorage()
# Call reload() method on this variable
storage.reload()
