#!/usr/bin/python3
"""
Init file for models module.
"""

from models.engine.file_storage import FileStorage
from .base_model import BaseModel
from .amenity import Amenity
from .review import Review
from .state import State
from .place import Place
from .user import User
from .city import City

storage = FileStorage()
storage.reload()
