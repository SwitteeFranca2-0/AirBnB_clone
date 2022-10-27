#!/usr/bin/python3
#This module contains the palce class

from models.base_model import BaseModel

class Review(BaseModel):
    """This defines the Review class"""
    place_id = ""
    user_id = ""
    text = ""

