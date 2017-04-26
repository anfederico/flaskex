from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///accounts.db', echo=True)
Base   = declarative_base()

class User(Base):
    __tablename__ = "user"
 
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True)
    password = Column(String(30))
    email    = Column(String(50))
    c1       = Column(String(15))
    c2       = Column(String(15))

    def __repr__(self):
        return '<User %r>' % (self.username)
    
# Create Models
Base.metadata.create_all(engine)