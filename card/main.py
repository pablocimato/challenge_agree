from fastapi import FastAPI
from .database import engine
from . import models
from .routers import cards, users, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(cards.router)
app.include_router(users.router)
app.include_router(authentication.router)


