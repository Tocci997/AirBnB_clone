#!/usr/bin/python3
"""defines the FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """represents a makeshift storage"""
    __file_path = "file.json"
    __objects = {}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        name_of_obj_cls = obj.__class__.__name__
        key = "{}.{}".format(name_of_obj_cls, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_all = FileStorage.__objects
        object_dict = {}
        for obj in obj_all.keys():
            object_dict[obj] = obj_all[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(object_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects, if it exists"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                try:
                    object_dict = json.load(f)
                    for key, value in object_dict.items():
                        cls_name, obj_id = key.split('.')
                        name = eval(cls_name)
                        instance = cls(**values)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
