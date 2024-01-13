#!/usr/bin/python3
"""
Module containing the init for the models package
"""

def initialize_storage():
    from models.engine import file_storage
    storage = file_storage.storage
