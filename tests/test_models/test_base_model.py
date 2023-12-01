#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
"""
This test module hosts class TestBaseModel
"""


class TestBaseModel(unittest.TestCase):
    """
    This class has methods which test the BaseModel class
    """
    def test_timestamps(self):
        """This tests the equality of timestamps: created_at, updated_at"""
        self.assertAlmostEqual(BaseModel().created_at, datetime.now())
        self.assertAlmostEqual(BaseModel().updated_at, datetime.now())
