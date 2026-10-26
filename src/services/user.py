from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.model.user import User
from src.schema.user import UserCreate
from src.utils.hash_password import hash_password


def create_user_service(user: UserCreate, db: Session):
    user_already_exists = db.scalar(
        select(User).where(User.email == user.email)
    )

    if user_already_exists:
        raise HTTPException(
            status_code=400,
            detail="User already exists with this email",
        )

    hashed_password = hash_password(
        user.password.get_secret_value()
    )

    new_user = User(
        userName=user.userName,
        email=user.email,
        password=hashed_password,
        phone_number=str(user.phone_number),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user