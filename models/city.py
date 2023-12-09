#!/usr/bin/python3
"""This module creates user city class"""

from models.base_model import BaseModel

class city(BaseModel):
    """Class for managing the user city objects"""
    state_id = ""
    name = ""