#!/usr/bin/python3
"""This module creates user review class"""

from models.base_model import BaseModel

class review(BaseModel):
    """Class for managing the user review objects"""
    place_id = ""
    user_id = ""
    text = ""