from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.model.user import User
from src.schema.user import UserCreate,Login
from src.utils.hash_password import hash_password, verify_password
from src.utils.token import create_access_token


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

    token =  create_access_token(new_user.id)

    return {
        "user": new_user,
        "access_token": token
    }



def login_service(user: Login, db: Session):
    user_check = db.scalar(
        select(User).where(User.email == user.email)
    )

    if not user_check:
        raise HTTPException(
            status_code=400,
            detail="User not found",
        )

    if not verify_password(
        user.password.get_secret_value(),
        user_check.password,
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid credentials",
        )

    token = create_access_token(user_check.id)

    return {
        "user": user_check,
        "access_token": token,
    }
