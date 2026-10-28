from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.schema.user import Login
from src.services.user import login_service

router = APIRouter()


@router.post("/login")
def login(user: Login, db: Session = Depends(get_db)):
    return login_service(user, db)
