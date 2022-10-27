#!/usr/bin/python3
#This is a module that holds the class file storage
import json
from  models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.city import City

class FileStorage:
    """This class serializes instances to json strings"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """This returns the dictionary of objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """This functon adds a key to the object attribute"""
        key = obj.to_dict()["__class__"] + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """This serializes _objects to the JSON file"""
        ob = {obj: val.to_dict() for obj, val in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(ob, f)
            
    def reload(self):
        """This deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                ob = json.load(f)
                for o in ob.values():
                    cls = o["__class__"]
                    self.new(eval(cls)(**o))

        except IOError:
            return
