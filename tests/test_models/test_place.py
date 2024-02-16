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

    def test_city_id_is_public_class_attribute(self):
        Island = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(Island))
        self.assertNotIn("city_id", Island.__dict__)

    def test_user_id_is_public_class_attribute(self):
        Island = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(Island))
        self.assertNotIn("user_id", Island.__dict__)

    def test_name_is_public_class_attribute(self):
        Island = Place()
        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(Island))
        self.assertNotIn("name", Island.__dict__)

    def test_description_is_public_class_attribute(self):
        Abj = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(Abj))
        self.assertNotIn("desctiption", Abj.__dict__)

    def test_number_rooms_is_public_class_attribute(self):
        Abj = Place()
        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(Abj))
        self.assertNotIn("number_rooms", Abj.__dict__)

    def test_number_bathrooms_is_public_class_attribute(self):
        Abj = Place()
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(Abj))
        self.assertNotIn("number_bathrooms", Abj.__dict__)

    def test_max_guest_is_public_class_attribute(self):
        Aba = Place()
        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(Aba))
        self.assertNotIn("max_guest", Aba.__dict__)

    def test_price_by_night_is_public_class_attribute(self):
        Aba = Place()
        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(Aba))
        self.assertNotIn("price_by_night", Aba.__dict__)

    def test_latitude_is_public_class_attribute(self):
        Aba = Place()
        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(Aba))
        self.assertNotIn("latitude", Aba.__dict__)

    def test_longitude_is_public_class_attribute(self):
        Aba = Place()
        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(Aba))
        self.assertNotIn("longitude", Aba.__dict__)

    def test_amenity_ids_is_public_class_attribute(self):
        Aba = Place()
        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(Aba))
        self.assertNotIn("amenity_ids", Aba.__dict__)

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
