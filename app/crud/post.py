from datetime import datetime

from sqlalchemy.orm.session import Session

from ..models.post import Post
from ..schemas.post import PostCreate
from .base import Base


class CRUDPost(Base[Post, PostCreate]):
    def create(self, db: Session, *, request: PostCreate):
        obj = self._create(db, request=request, timestamp=datetime.utcnow())

        return obj

    def delete(self, db: Session, *, id: int):
        obj = self._delete(db, name="Post", id=id)

        return obj


post = CRUDPost(Post)
