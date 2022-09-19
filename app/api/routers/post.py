import shutil
from datetime import datetime
from pathlib import Path

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm.session import Session

from ... import crud
from ...dependencies.database import get_db
from ...schemas.post import PostCreate, PostInDB
from fastapi_pagination import Page, paginate, Params

router = APIRouter()


@router.get("", response_model=Page[PostInDB])
async def read_posts(db: Session = Depends(get_db), params: Params = Depends()):
    return paginate(crud.post.read_all(db=db), params)


@router.post("", response_model=PostInDB)
def create(request: PostCreate, db: Session = Depends(get_db)):
    post = crud.post.create(db=db, request=request)

    return post


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    post = crud.post.delete(db=db, id=id)

    return post


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    file_name = f"{datetime.utcnow()}_{image.filename}"
    file_path = Path(".") / "images" / file_name

    with open(file_path, "wb") as file:
        shutil.copyfileobj(image.file, file)

    return {"file_path": file_path}
