from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from ..db.base_class import Base


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    image_url = Column(String)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
