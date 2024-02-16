#!/usr/bin/python3
"""Defines unittests for user.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing the class, User."""
    def test_that_instance_stored_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_email_is_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_is_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_unique_ids(self):
        Tocci = User()
        Dominic = User()
        self.assertNotEqual(Tocci.id, Dominic.id)

    def test_different_created_at(self):
        Tocci = User()
        sleep(0.05)
        Dominic = User()
        self.assertLess(Tocci.created_at, Dominic.created_at)

    def test_different_updated_at(self):
        Tocci = User()
        sleep(0.05)
        Dominic = User()
        self.assertLess(Tocci.updated_at, Dominic.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        user = User()
        user.id = "070145"
        user.created_at = user.updated_at = date
        userstr = user.__str__()
        self.assertIn("[User] (070145)", userstr)
        self.assertIn("'id': '070145'", userstr)
        self.assertIn("'created_at': " + date_repr, userstr)
        self.assertIn("'updated_at': " + date_repr, userstr)


if __name__ == "__main__":
    unittest.main()
