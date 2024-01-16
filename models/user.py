#!/usr/bin/python3
""" 
User Module 
"""

from models.base_model import BaseModel
import models


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def save(self):
        """Save the current instance to the storage"""
        models.storage.new(self)
        models.storage.save()
