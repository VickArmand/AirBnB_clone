#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
This module hosts the class BaseModel
"""


class BaseModel:
    """
    This class defines all common attributes/methods for other classes
    Public instance attributes:
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime
        when an instance is created
        updated_at: datetime - assign with the current datetime when an
        instance is created and it will be updated every time
        you change your object
    methods
        __str__: should print: [<class name>] (<self.id>) <self.__dict__>
        save: updates the public instance attribute
        updated_at with the current datetime
        to_dict(self): returns a dictionary containing
        all keys/values of __dict__ of the instance
    """
    def __init__(self, *args, **kwargs):
        """
        This method is called when an object or instance is created
        if kwargs is not empty
            each key of this dictionary is an attribute name
            (Note __class__ from kwargs is the only one that
            should not be added as an attribute.)

            each value of this dictionary is the value of this attribute name

            created_at and updated_at are strings in this dictionary,
            but inside your BaseModel instance is working with datetime object.
            You have to convert these strings into datetime object.

        otherwise: create id and created_at as a new instance
        """
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            dateformat = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value,
                                                           dateformat)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Prints object information"""
        clsname = self.__class__.__name__
        return (f"[{clsname}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        self.__dict__["__class__"] = self.__class__.__name__
        if type(self.created_at) != str:
            self.__dict__["created_at"] = "{:%Y-%m-%dT%H:%M:%S.%f}".format(
                    self.created_at)
        if type(self.updated_at) != str:
            self.__dict__["updated_at"] = "{:%Y-%m-%dT%H:%M:%S.%f}".format(
                    self.updated_at)
        return self.__dict__
