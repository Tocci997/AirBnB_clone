#!/usr/bin/python3
"""Defines unittests for place.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing the class, Place."""
    def test_that_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_unique_ids(self):
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_different_created_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.created_at, place2.created_at)

    def test_different_updated_at(self):
        place1 = Place()
        sleep(0.05)
        place2 = Place()
        self.assertLess(place1.updated_at, place2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        place = Place()
        place.id = "123555"
        place.created_at = place.updated_at = date
        placestr = place.__str__()
        self.assertIn("[Place] (123555)", placestr)
        self.assertIn("'id': '123555'", placestr)
        self.assertIn("'created_at': " + date_repr, placestr)
        self.assertIn("'updated_at': " + date_repr, placestr)


if __name__ == "__main__":
    unittest.main()
