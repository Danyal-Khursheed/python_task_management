from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from src.database import get_db
from src.schema.post import PostCreate, PostListResponse, PostResponse
from src.services.post import create_post as create_post_service
from src.services.post import get_all_post_service

router = APIRouter()


@router.post("/", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return create_post_service(post, db)


@router.get("/", response_model=PostListResponse)
def get_all_post(
    db: Session = Depends(get_db),
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1, le=100),
):
    return get_all_post_service(db, page, limit)