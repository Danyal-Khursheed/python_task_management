from fastapi import APIRouter, Depends
from src.schema.user import UserCreate
from src.database import get_db
from sqlalchemy.orm import Session
from src.services.user import create_user_service

router = APIRouter()

@router.post("/")
def register(user:UserCreate, db:Session = Depends(get_db)):
    return create_user_service(user, db)