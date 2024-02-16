#!/usr/bin/python3
"""Defines unittests for state.py"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing the class, State."""
    def test_that_instance_stored_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_two_states_unique_ids(self):
        Imo = State()
        Abia = State()
        self.assertNotEqual(Imo.id, Abia.id)

    def test_different_created_at(self):
        Imo = State()
        sleep(0.05)
        Abia = State()
        self.assertLess(Imo.created_at, Abia.created_at)

    def test_different_updated_at(self):
        Imo = State()
        sleep(0.05)
        Abia = State()
        self.assertLess(Imo.updated_at, Abia.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        state = State()
        state.id = "091544"
        state.created_at = state.updated_at = date
        statestr = state.__str__()
        self.assertIn("[State] (091544)", statestr)
        self.assertIn("'id': '091544'", statestr)
        self.assertIn("'created_at': " + date_repr, statestr)
        self.assertIn("'updated_at': " + date_repr, statestr)


if __name__ == "__main__":
    unittest.main()
