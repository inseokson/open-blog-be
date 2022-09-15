from fastapi import FastAPI

from .db.init_db import init_db


def get_application() -> FastAPI:
    init_db()
    application = FastAPI()

    return application


app = get_application()
