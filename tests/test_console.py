#!/usr/bin/python3
"""This model hosts the class TestUser"""
import unittest
from models import storage
from datetime import datetime
from console import HBNBCommand as hbc
from console import User, storage


class TestConsole(unittest.TestCase):
    """This class tests the User class"""
    def setUp(self):
        """Creates a new User instance to test with"""
        self.hbc_obj = hbc()
        self.new_model = User()
        self.model_key = 'User.{}'.format(self.new_model.id)

    def test_precmd(self):
        """This method tests whether precmd returns the right output"""
        self.assertEqual(self.hbc_obj.precmd("User.all()"), "all User")
        self.assertEqual(self.hbc_obj.precmd("all User"), "all User")

    def test_create(self):
        """This method tests the creation of a new User instance"""
        size = len(storage.all())
        self.hbc_obj.do_create("User")
        new_size = len(storage.all())
        self.assertEqual(size + 1, new_size)

    def test_update(self):
        """This method tests the updation of a user instance"""
        all_obj = storage.all()
        update_str = 'User {} email "aibnb@mail.com"'.format(
                self.new_model.id)
        self.hbc_obj.do_update(update_str)
        self.assertEqual(all_obj[self.model_key].__dict__['email'],
                         'aibnb@mail.com')

    def test_destroy(self):
        """This method tests the deletion of the created user instance"""
        size = len(storage.all())
        self.hbc_obj.do_destroy("User {}" .format(self.new_model.id))
        new_size = len(storage.all())
        self.assertEqual(size - 1, new_size)

    def tearDown(self):
        self.hbc_obj.do_destroy("User {}" .format(self.new_model.id))
