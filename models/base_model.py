#!/usr/bin/python3
"""
base class file
"""

import uuid
from datetime import date, datetime
import models
from json import JSONEncoder


class BaseModel:
    """
    =========
    BaseModel
    =========
    """

    def __init__(self, *args, **kwargs):
        """initialize the instance of the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(
                        value,
                        '%Y-%m-%dT%H:%m:%S.%f')
                elif key == "__class__":
                    continue

                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """save new information to the class object"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary representation of the instance"""
        dict_repr = {}
        for key, value in self.__dict__.items():
            dict_repr[key] = value
            if isinstance(value, datetime):
                dict_repr[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict_repr["__class__"] = type(self).__name__
        return dict_repr

    def __str__(self):
        """return the string formatted message when instance is called"""
        clName = self.__class__.__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)


class BaseModelEncoder(JSONEncoder):
    """JSON Encoder for BaseModel"""

    def default(self, o):
        """default"""
        if isinstance(o, BaseModel):
            return 0,  o.to_dict()
        return super().default(o)
