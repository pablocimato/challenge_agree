from fastapi import FastAPI, Depends
import schema, models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/cards")
def create():
    return {"message": "welcome to FastAPI!"}