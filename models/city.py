#!/usr/bin/python3
from models.base_model import BaseModel
"""
This module hosts class City
"""


class City(BaseModel):
    """
    Public class attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
