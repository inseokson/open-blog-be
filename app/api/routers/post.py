from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from ... import crud
from ...dependencies.database import get_db
from ...schemas.post import PostCreate, PostInDB

router = APIRouter()


@router.get("/all")
def posts(db: Session = Depends(get_db)):
    return crud.post.get_all(db=db)


@router.post("", response_model=PostInDB)
def create(request: PostCreate, db: Session = Depends(get_db)):
    post = crud.post.create(db=db, request=request)

    return post


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    post = crud.post.delete(db=db, id=id)

    return post
