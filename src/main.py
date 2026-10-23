from fastapi import FastAPI

from src.routers import post_router

app = FastAPI()

app.include_router(post_router, prefix="/posts", tags=["posts"])
