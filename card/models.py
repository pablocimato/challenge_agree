from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
     __tablename__ = "users_table"
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String(20), unique=True)
     password = Column(String(100))
     
 #    creator = relationship("Card", back_populates="cards")

class Card(Base):
     __tablename__ = "cards_table"
     id = Column(Integer, primary_key=True, index=True)
     name = Column(String(20), unique=True)
     edition = Column(String(20))
     types = Column(String(20))
     subtypes = Column(String(20))
     atk = Column(Integer)
     defe = Column(Integer)
     stars = Column(Integer)
     description = Column(String(100))
     price = Column(Integer)
     cardimage = Column(String(20))
#     user_id = Column(String(20), ForeignKey('users_table.name'))

#     cards = relationship("User", back_populates="creator")


    
    