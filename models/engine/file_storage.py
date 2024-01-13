#!/usr/bin/python3
"""
Module containing the FileStorage class
"""

import json
from os.path import exists
from models.base_model import BaseModel, User, State, City, Amenity, Place, Review


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
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to

    def to_dict(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        return obj_dict

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)
        """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    cls_name = value["__class__"]
                    del value["__class__"]
                    new_instance = eval(cls_name)(**value)
                    FileStorage.__objects[key] = new_instance
        except FileNotFoundError:
            pass


# Create a unique FileStorage instance for the application
storage = FileStorage()
# Call reload() method on this variable
storage.reload()
