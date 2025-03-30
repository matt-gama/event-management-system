from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.core.security import hash_password



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    password = Column(String, nullable=False)

    def __init__(self, email:str, name:str, lastname:str, password:str):
        self.email = email
        self.password = hash_password(password) 
        self.name = name
        self.lastname = lastname 

    events = relationship("Event", back_populates="owner")