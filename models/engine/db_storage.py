#!/usr/bin/python3
"""Store the information in a database"""
from os import getenv
from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Table, select
from models.state import State
from models.city import City
from models.base_model import Base
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """initialize the class"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        url = 'mysql+mysqldb://{}:{}@{}:3306/{}'.format(user,
                                                        password, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)
        env = getenv('HBNB_ENV')
        if env == 'test':
            # drop all tables
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query all on the current database session """
        classes = {"City": City, "State": State,
                "User": User, "Place": Place, "Review": Review,
                "Amenity": Amenity}
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """ add a new object to the database"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not none"""
        if obj is None:
            pass
        self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        create the current database session
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """call remove method on self.__session)"""
        self.__session.remove()
