from .auth import router as auth_router
from .post import router as post_router
from .user import router as user_router

__all__ = ["auth_router", "post_router", "user_router"]
