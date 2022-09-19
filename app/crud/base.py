from typing import Generic, Type, TypeVar

from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.session import Session

from ..db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class Base(Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get_all(self, db: Session):
        return db.query(self.model).all()

    def _create(self, db: Session, *, request: SchemaType, **kwargs) -> ModelType:
        data = jsonable_encoder(request)
        if not kwargs:
            data.update(kwargs)

        obj = self.model(**data)
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return obj

    def _delete(self, db: Session, *, name: str, id: int):
        obj = db.query(self.model).get(id)
        if not obj:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"{name} with id {id} not found")
        try:
            db.delete(obj)
            db.commit()
        except SQLAlchemyError as e:
            db.rollback()
            raise e

        return obj
