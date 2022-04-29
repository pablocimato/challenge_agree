from fastapi import APIRouter, Depends, status, Response, HTTPException, File, Form, UploadFile
from .. import schemas, database, models, ouath2
from ..hashing import Hash
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(prefix="/card", tags=['Cards'])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Card,db: Session = Depends(database.get_db), current_user: schemas.User = Depends(ouath2.get_current_user)):
    new_card = models.Card(id=request.id,name=request.name,edition=request.edition,
                            types=request.types,subtypes=request.subtypes,
                            atk=request.atk,defe=request.defe,stars=request.stars,
                            description=request.description,price=request.price,cardimage=request.cardimage)

    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(database.get_db),current_user: schemas.User = Depends(ouath2.get_current_user)):
    card=db.query(models.Card).filter(models.Card.id == id)
    if not card.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
         detail= f"Card with the id {id} is not available")
    card.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

@router.put ('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Card, db: Session= Depends(database.get_db),current_user: schemas.User = Depends(ouath2.get_current_user)):
    card=db.query(models.Card).filter(models.Card.id == id)
    if not card.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} not found")
    card.update(request)
    db.commit()
    return 'updated'

@router.get('/', response_model=List[schemas.ShowCards])
def all(db: Session = Depends(database.get_db),current_user: schemas.User = Depends(ouath2.get_current_user)):
    cards=db.query(models.Card).all()
    return cards

@router.get('/{id}', response_model=schemas.ShowCards)
def show (id,db: Session = Depends(database.get_db),current_user: schemas.User = Depends(ouath2.get_current_user)):
    card=db.query(models.Card).filter(models.Card.id == id).first()
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
         detail= f"Card with the id {id} is not available")
    return card