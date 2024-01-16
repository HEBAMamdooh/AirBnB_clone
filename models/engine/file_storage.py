#!/usr/bin/python3
"""File storage class"""

import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a file and deserializes to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        dict_attrs = obj.to_dict()
        new_key = "{}.{}".format(dict_attrs["__class__"], dict_attrs["id"])
        self.__objects[new_key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file, indent=2)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r") as file:
                content = file.read()
                dict_from_file = {}
                if content != "":
                    dict_from_file = json.loads(content)
                for file_key, dict_obj in dict_from_file.items():
                    if file_key not in FileStorage.__objects.keys():
                        className = dict_obj["__class__"]
                        newInst = eval("{}(**dict_obj)".format(className))
                        self.new(newInst)
        except FileNotFoundError:
            pass
