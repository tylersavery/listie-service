from sqlalchemy.orm import Session

from . import models, schemas


def get_items(db: Session):
    return db.query(models.Item).all()


def get_item(db: Session, id: int):
    return db.query(models.Item).get(id)


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_item(db: Session, id: int, item: schemas.ItemUpdate):
    db_item = db.query(models.Item).get(id)

    db_item.name = item.name
    db_item.category = item.category
    db_item.purchased = item.purchased

    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item(db: Session, id: int):
    db_item = db.query(models.Item).get(id)
    db.delete(db_item)
