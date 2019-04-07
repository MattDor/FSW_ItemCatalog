from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import datetime
 
Base = declarative_base()

class Category(Base):

    __tablename__ = 'category'
   
    id   = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id
       }
 

class User(Base):

    __tablename__ = 'user'

    name  = Column(String(100), nullable = False)
    id    = Column(Integer, primary_key = True)
    email = Column(String(500))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'  : self.email,
           'id'           : self.id
       }


class Item(Base):

    __tablename__ = 'item'

    name        = Column(String(100), nullable = False)
    id          = Column(Integer, primary_key = True)
    description = Column(String(500))
    added_date  = Column(DateTime, default=datetime.datetime.now())
    category_id = Column(Integer,ForeignKey('category.id'))
    user_id     = Column(Integer,ForeignKey('user.id'))
    category    = relationship(Category)
    user        = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'                 : self.name,
           'description'          : self.description,
           'id'                   : self.id,
           'category_id'          : self.category_id,
           'user_id'              : self.user_id
       }



engine = create_engine('sqlite:///itemstore.db')
 

Base.metadata.create_all(engine)
