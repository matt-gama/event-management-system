from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    password = Column(String, nullable=False)

    events = relationship("Event", back_populates="owner")