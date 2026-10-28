from fastapi import FastAPI

from src.routers import auth_router, post_router, user_router

app = FastAPI()

app.include_router(post_router, prefix="/posts", tags=["posts"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
