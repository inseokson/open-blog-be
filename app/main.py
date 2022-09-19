from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .api.router import router
from .db.init_db import init_db


def get_application() -> FastAPI:
    init_db()
    application = FastAPI()
    application.include_router(router)

    path_image = Path(".") / "images"
    if not path_image.exists():
        path_image.mkdir()
    application.mount("/images", StaticFiles(directory="images"), name="images")

    origins = ["http://localhost:3000"]
    application.add_middleware(
        CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )

    return application


app = get_application()
