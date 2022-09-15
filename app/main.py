from fastapi import FastAPI

from .api.router import router
from .db.init_db import init_db


def get_application() -> FastAPI:
    init_db()
    application = FastAPI()
    application.include_router(router)

    return application


app = get_application()
