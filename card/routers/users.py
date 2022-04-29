from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, database, models, ouath2
from ..hashing import Hash
from typing import List
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=['Users'])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    new_user = models.User(id=request.id, name=request.name, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model=schemas.ShowUsers)
def show (id,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(ouath2.get_current_user)):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
         detail= f"User {id} is not created")
    return user