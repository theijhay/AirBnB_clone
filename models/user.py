#!/usr/bin/python3
"""This is a class User that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""