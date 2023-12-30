#!/usr/bin/python3
"""This model hosts the class TestReview"""
import unittest
from models import storage
from datetime import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """This class tests the Review class"""
    def setUp(self):
        """Creates a new Review instance to test with"""
        self.new_model = Review()
        self.model_key = 'Review.' + self.new_model.id

    def test_review(self):
        """This method tests the type of the new Review instance"""
        self.assertEqual(type(self.new_model), Review)

    def test_place_id(self):
        """This method tests if the place_id is a string"""
        self.assertEqual(type(self.new_model.place_id), str)

    def test_user_id(self):
        """This method tests if the user_id is a string"""
        self.assertEqual(type(self.new_model.user_id), str)

    def test_text(self):
        """This method tests if the text is a string"""
        self.assertEqual(type(self.new_model.text), str)

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
        and if it is made from the class Review
        """
        all_objects = storage.all()
        self.assertEqual(all_objects[self.model_key], self.new_model)
        self.assertEqual(type(all_objects[self.model_key]), Review)
