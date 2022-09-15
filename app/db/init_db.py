# Import the relevant models where you call Base.metadata.create_all
# for more details:
# https://stackoverflow.com/questions/54118182/sqlalchemy-not-creating-tables
from .base import Base, Post
from .session import engine


def init_db():
    Base.metadata.create_all(engine)
