#!/usr/bin/python3
"""Defines the BaseModel class"""
import models
import uuid
from datetime import datetime
import storage


class BaseModel:
    """Describes a class BaseModel"""
    def __init__(self, *args, **kwargs):
        time_date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_date_format))
                else:
                    setattr(self, k, v)

        models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def __str__(self):
        """returns a formated string"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        dict_nary = self.__dict__.copy()
        dict_nary["__class__"] = self.__class__.__name__
        dict_nary["created_at"] = self.created_at.isoformat()
        dict_nary["updated_at"] = self.updated_at.isoformat()

        return dict_nary
