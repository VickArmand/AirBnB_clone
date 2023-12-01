#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
"""
This module hosts FileStorage class
"""


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)

        __objects: dictionary - empty but will store all objects
        by <class name>.id

    Public instance methods:
        all(self): returns the dictionary __objects

        new(self, obj): sets in __objects the obj with
        key <obj class name>.id

        save(self): serializes __objects to the JSON file

        reload(self): deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, "w") as fw:
            obj_dict = FileStorage.__objects
            for key, value in obj_dict.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, fw)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, "r") as fr:
                data = json.load(fr)
                for obj in data.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
