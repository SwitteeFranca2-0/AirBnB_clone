#!/usr/bin/python3
#This module defines a base class for the airbnb project
import uuid
from datetime import datetime
import models


class BaseModel:
#This is a base model class.
    
    def __init__(self, *args, **kwargs):
        #This initialises vretaed class objects.
        if kwargs:
            self.__dict__.update(kwargs)
            del self.__dict__["__class__"]
            self.__dict__["created_at"] = datetime.fromisoformat(self.__dict__["created_at"])
            self.__dict__["updated_at"] = datetime.fromisoformat(self.__dict__["updated_at"])
        else:    
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        #This defines the string attribute of the class
        obj = self.__class__.__name__
        return '[{}] ({}) {}'.format(obj, self.id, self.__dict__) 
    
    def save(self):
        #This updates the public instance attribute updates_at
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        #This adds the class attributes to a dictionary
        o_dict = {}	
        o_dict.update(self.__dict__)
        o_dict["created_at"] = datetime.isoformat(self.__dict__["created_at"])
        o_dict["updated_at"] = datetime.isoformat(self.__dict__["updated_at"])    
        o_dict["__class__"] = self.__class__.__name__
        return o_dict

