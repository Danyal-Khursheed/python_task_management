import math

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.model.post import Post
from src.schema.post import PostCreate


def create_post(post: PostCreate, db: Session):
    new_post = Post(
        title=post.title,
        description=post.description,
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_post_service(db: Session, page: int, limit: int):
    offset = (page - 1) * limit

    statement = select(Post).order_by(Post.id).limit(limit).offset(offset)
    posts = db.scalars(statement).all()

    total = db.scalar(select(func.count()).select_from(Post)) or 0
    total_pages = math.ceil(total / limit) if limit else 0

    return {
        "data": posts,
        "metadata": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": total_pages,
        },
    }
