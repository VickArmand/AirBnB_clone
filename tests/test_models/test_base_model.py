#!/usr/bin/python3
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
"""
This test module hosts class TestBaseModel
"""


class TestBaseModel(unittest.TestCase):
    """
    This class has methods which test the BaseModel class
    """
    def setUp(self):
        """we first want to create a BaseModel instance"""
        self.new_model = BaseModel()
        self.model_key = 'BaseModel.' + self.new_model.id

    def test_timestamps(self):
        """This tests the data type of timestamps: created_at, updated_at"""
        self.assertEqual(type(self.new_model.created_at), datetime)
        self.assertEqual(type(self.new_model.updated_at), datetime)

    def test_id(self):
        """
        This tests if the id attribute of
        the created instance is a string
        """
        self.assertEqual(type(self.new_model.id), str)

    def test_presence(self):
        """
        This tests whether the created instance is saved in the JSON file
        and if it is made from the class BaseModel
        """
        all_objects = storage.all()
        self.assertEqual(all_objects[self.model_key], self.new_model)
        self.assertEqual(type(all_objects[self.model_key]), BaseModel)

    def test_instance(self):
        """
        This tests if the created instance is is made from the class BaseModel
        """
        self.assertEqual(type(self.new_model), BaseModel)
