from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    author: str
    image_url: str
    content: str


class PostCreate(PostBase):
    pass


class PostInDB(PostBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
