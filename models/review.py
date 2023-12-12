#!/usr/bin/python3
"""This module creates a Review class, Defines the Review class."""
<<<<<<< HEAD
from base_model import BaseModel


=======
from models.base_model import BaseModel
>>>>>>> f311c11037fa557b0a32a76ca2e6fc5353e542dd
class Review(BaseModel):

    """Class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
