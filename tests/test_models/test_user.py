#!/usr/bin/python3
"""This model hosts the class TestUser"""
import unittest
from models import storage
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """This class tests the User class"""
    def setUp(self):
        """Creates a new User instance to test with"""
        self.new_model = User()
        self.model_key = 'User.' + self.new_model.id

    def test_user(self):
        """This method tests the type of attribute of the new User instance"""
        self.assertEqual(type(self.new_model), User)

    def test_email(self):
        """This method tests if the email is a string"""
        self.assertEqual(type(self.new_model.email), str)

    def test_password(self):
        """This method tests if the password is a string"""
        self.assertEqual(type(self.new_model.password), str)

    def test_fullname(self):
        """This method tests if the first and last names are strings"""
        self.assertEqual(type(self.new_model.first_name), str)
        self.assertEqual(type(self.new_model.last_name), str)

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
        and if it is made from the class User
        """
        all_objects = storage.all()
        self.assertEqual(all_objects[self.model_key], self.new_model)
        self.assertEqual(type(all_objects[self.model_key]), User)
