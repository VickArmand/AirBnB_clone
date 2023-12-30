#!/usr/bin/python3
"""This model hosts the class TestPlace"""
import unittest
from models import storage
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """This class tests the Place class"""
    def setUp(self):
        """Creates a new Place instance to test with"""
        self.new_model = Place()
        self.model_key = 'Place.' + self.new_model.id

    def test_place(self):
        """This method tests the type of attribute of the new Place instance"""
        self.assertEqual(type(self.new_model), Place)

    def test_number_rooms(self):
        """This method tests if the number_rooms is an int"""
        self.assertEqual(type(self.new_model.number_rooms), int)

    def test_number_bathrooms(self):
        """This method tests if the number_bathrooms is an int"""
        self.assertEqual(type(self.new_model.number_bathrooms), int)

    def test_max_guest(self):
        """This method tests if the max_guest is an int"""
        self.assertEqual(type(self.new_model.max_guest), int)

    def test_price_by_night(self):
        """This method tests if the price_by_night is an int"""
        self.assertEqual(type(self.new_model.price_by_night), int)

    def test_latitude(self):
        """This method tests if the latitude is a float"""
        self.assertEqual(type(self.new_model.latitude), float)

    def test_longitude(self):
        """This method tests if the longitude is an float"""
        self.assertEqual(type(self.new_model.longitude), float)

    def test_amenity_ids(self):
        """This method tests if the longitude is an float"""
        self.assertEqual(type(self.new_model.amenity_ids), list)

    def test_name(self):
        """This method tests if the name is a string"""
        self.assertEqual(type(self.new_model.name), str)

    def test_city_id(self):
        """This method tests if the city_id attribute is a string"""
        self.assertEqual(type(self.new_model.city_id), str)

    def test_user_id(self):
        """This method tests if the user_id attribute is a string"""
        self.assertEqual(type(self.new_model.user_id), str)

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
        and if it is made from the class Place
        """
        all_objects = storage.all()
        self.assertEqual(all_objects[self.model_key], self.new_model)
        self.assertEqual(type(all_objects[self.model_key]), Place)
