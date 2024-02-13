#!/usr/bin/python3
"""Defines the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """A class that handles user information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
