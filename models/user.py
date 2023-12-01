#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module hosts class User
"""


class User(BaseModel):
    """
    inherits from BaseModel
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
