#!/usr/bin/python3
"""Defines unittests for review.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview(unittest.TestCase):
    """Unittests for testing the class, Review."""
    def test_that_instance_stored_in_objects(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_unique_ids(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_different_created_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_different_updated_at(self):
        rev1 = Review()
        sleep(0.05)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        rev = Review()
        rev.id = "127716"
        rev.created_at = rev.updated_at = date
        revstr = rev.__str__()
        self.assertIn("[Review] (127716)", revstr)
        self.assertIn("'id': '127716'", revstr)
        self.assertIn("'created_at': " + date_repr, revstr)
        self.assertIn("'updated_at': " + date_repr, revstr)


if __name__ == "__main__":
    unittest.main()
