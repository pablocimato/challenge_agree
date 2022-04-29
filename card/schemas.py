from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
     id: int
     name: str
     password: str

class Card(BaseModel):
     id: int
     name: str
     edition: str
     types: str
     subtypes: str
     atk: int
     defe: int
     stars: int
     description: str
     price: int
     cardimage: str

class BaseCard(Card):
     id: int
     name: str
     types: str

     class Config():
          orm_mode = True

class ShowUsers(BaseModel):
     id: int
     name: str
     cards: List[BaseCard] = []
     class Config():
          orm_mode = True

class ShowCards(BaseModel):
     id: int
     name: str
     types: str
     subtypes: str

#    creator: ShowUsers           no puedo relacionar las tablas, no busca el campo creator

     class Config():
          orm_mode = True
          
class Login(BaseModel):
    username: str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None