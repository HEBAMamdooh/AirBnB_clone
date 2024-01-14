#!/usr/bin/python3
"""
Module for BaseModel class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class for AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key not in ["__class__"]:
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def save(self):
        """Save the instance to the storage."""
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """Return the string representation of the instance."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.to_dict()
        )
