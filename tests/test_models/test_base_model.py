#!/usr/bin/python3
"""a test module for testing our code"""
import os
import models
from datetime import datetime
import unittest
from time import sleep
from models.base_model import BaseModel


class BaseModelTest(unittest.TestCase):
    """tests our BaseModel class"""
    def test_init(self):
        eg_model = BaseModel()

        self.assertIsNotNone(eg_model.id)
        self.assertIsNotNone(eg_model.created_at)
        self.assertIsNotNone(eg_model.updated_at)

    def test_save(self):
        @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_to_dict(self):
        eg_model = BaseModel()
        eg_model_dict = eg_model.to_dict()

        self.assertIsInstance(eg_model_dict, dict)
        self.assertEqual(eg_model_dict["__class__"], 'BaseModel')
        self.assertEqual(eg_model_dict["id"], eg_model.id)
        self.assertEqual(eg_model_dict["created_at"],
                         eg_model.created_at.isoformat())
        self.assertEqual(eg_model_dict["updated_at"],
                         eg_model.updated_at.isoformat())

    def test_str(self):
        eg_model = BaseModel()

        self.assertTrue(str(eg_model).startswith('[BaseModel]'))
        self.assertIn(eg_model.id, str(eg_model))
        self.assertIn(str(eg_model.__dict__), str(eg_model))


if __name__ == "__main__":
    unittest.main()
