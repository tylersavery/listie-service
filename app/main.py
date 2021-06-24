from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.put("/items/{id}", response_model=schemas.Item)
def update_item(item: schemas.ItemUpdate, id: int = id, db: Session = Depends(get_db)):
    return crud.update_item(db=db, id=id, item=item)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items


@app.get("/items/{id}", response_model=schemas.Item)
def read_item(id: int = id, db: Session = Depends(get_db)):
    item = crud.get_item(db, id=id)
    return item


@app.delete("/items/{id}")
def delete_item(id: int = id, db: Session = Depends(get_db)):
    item = crud.delete_item(db, id=id)
    return {}
