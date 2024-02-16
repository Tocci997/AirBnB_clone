#!/usr/bin/python3
"""Defines unittests for city.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing the class, City."""
    def test_that_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_unique_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_different_created_at(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.created_at, city2.created_at)

    def test_different_updated_at(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        city = City()
        city.id = "121219"
        city.created_at = city.updated_at = date
        citystr = city.__str__()
        self.assertIn("[City] (121219)", citystr)
        self.assertIn("'id': '121219'", citystr)
        self.assertIn("'created_at': " + date_repr, citystr)
        self.assertIn("'updated_at': " + date_repr, citystr)


if __name__ == "__main__":
    unittest.main()
