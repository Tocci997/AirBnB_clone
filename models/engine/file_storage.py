#!/usr/bin/python3
"""defines the FileStorage class"""

import json
import os
from models.base_model import BaseModel

class FileStorage:
    """represents a makeshift storage"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name_of_obj_cls = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(name_of_obj_cls, obj.id)] = obj

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = FileStorage.__objects
        object_dict = {}
        for obj in obj_dict.keys():
            object_dict[obj] = obj_dict[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects, if it exists"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    object_dict = json.load(f)
                    for k, v in object_dict.items():
                        cls_name, obj_id = k.split('.')
                        name = eval(cls_name)
                        instance = cls(**v)
                        FileStorage.__objects[k] = instance
                except Exception:
                    pass
