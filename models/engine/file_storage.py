#!/usr/bin/python3
"""File storage class"""
import json
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User

class FileStorage:
    """Serializes instances to a file and deserializes to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, value in FileStorage.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialized_objects, f)

def reload(self):
    """Deserializes the JSON file to __objects"""
    try:
        with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
            loaded_objects = json.load(f)
        for key, value in loaded_objects.items():
            class_name = key.split('.')[0]
            obj = eval(class_name)(**value)
            FileStorage.__objects[key] = obj
    except FileNotFoundError:
        pass
