#!/usr/bin/python3
"""Defines unittests for amenity.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing the class, Amenity."""
    def test_that_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_unique_ids(self):
        amen1 = Amenity()
        amen2 = Amenity()
        self.assertNotEqual(amen1.id, amen2.id)

    def test_different_created_at(self):
        amen1 = Amenity()
        sleep(0.05)
        amen2 = Amenity()
        self.assertLess(amen1.created_at, amen2.created_at)

    def test_different_updated_at(self):
        amen1 = Amenity()
        sleep(0.05)
        amen2 = Amenity()
        self.assertLess(amen1.updated_at, amen2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        amen = Amenity()
        amen.id = "121912"
        amen.created_at = amen.updated_at = date
        amenstr = amen.__str__()
        self.assertIn("[Amenity] (121912)", amenstr)
        self.assertIn("'id': '121912'", amenstr)
        self.assertIn("'created_at': " + date_repr, amenstr)
        self.assertIn("'updated_at': " + date_repr, amenstr)


if __name__ == "__main__":
    unittest.main()
