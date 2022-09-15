from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from ... import crud
from ...dependencies.database import get_db
from ...schemas.post import PostCreate, PostInDB

router = APIRouter()


@router.post("", response_model=PostInDB)
def create(request: PostCreate, db: Session = Depends(get_db)):
    post = crud.post.create(db=db, request=request)

    return post
