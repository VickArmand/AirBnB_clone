#!/usr/bin/python3
"""This model hosts the class TestState"""
import unittest
from models import storage
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """This class tests the State class"""
    def setUp(self):
        """Creates a new State instance to test with"""
        self.new_model = State()
        self.model_key = 'State.' + self.new_model.id

    def test_state(self):
        """This method tests the type of attribute of the new State instance"""
        self.assertEqual(type(self.new_model), State)

    def test_name(self):
        """This method tests if the name is a string"""
        self.assertEqual(type(self.new_model.name), str)

    def test_id(self):
        """This method tests if the id attribute is a string"""
        self.assertEqual(type(self.new_model.id), str)

    def test_timestamps(self):
        """
        This method tests the timestamps created_at and updated_at
        if they are of type datetime
        """
        self.assertEqual(type(self.new_model.created_at), datetime)
        self.assertEqual(type(self.new_model.updated_at), datetime)

    def test_presence(self):
        """
        This tests whether the created instance is saved in the JSON file
        and if it is made from the class State
        """
        all_objects = storage.all()
        self.assertEqual(all_objects[self.model_key], self.new_model)
        self.assertEqual(type(all_objects[self.model_key]), State)
