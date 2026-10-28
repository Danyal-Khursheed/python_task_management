from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.schema.user import UserCreate
from src.services.user import create_user_service
from src.dependencies.auth import get_current_user
from src.model.user import User

router = APIRouter()


@router.post("/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(user, db)


@router.get("/me")
def currentUser(current_user:User = Depends(get_current_user)):
    return current_user