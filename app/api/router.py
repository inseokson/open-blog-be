from fastapi import APIRouter

from .routers.post import router as post_router

router = APIRouter()
router.include_router(post_router, prefix="/post", tags=["post"])
