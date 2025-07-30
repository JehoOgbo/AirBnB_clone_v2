#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    # declare class attributes
    @declared_attr
    def id(cls):
        return Column(String(60), primary_key=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=datetime.utcnow())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime, nullable=False, default=datetime.utcnow())

    #id = Column(String(60), primary_key=True, nullable=False)
    #created_at = Column(
            #DateTime, nullable=False, default=datetime.utcnow())
    #updated_at = Column(
            #DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                kwargs['updated_at'] = datetime.now()
            try:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            except KeyError:
                kwargs['created_at'] = datetime.now()
            try:
                del kwargs['__class__']
            except KeyError:
                pass;
            try:
                new = kwargs['id']
            except KeyError:
                kwargs['id'] = str(uuid.uuid4())
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        try:
            del dictionary['_sa_instance_state']
        except KeyError:
            pass
        return dictionary

    def delete(self):
        """Delete the current instance from storage"""
        storage.delete(self)
