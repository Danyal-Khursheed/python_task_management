from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.utils.token import verify_access_token

from src.database import get_db
from src.model.user import User

security = HTTPBearer()


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
        db: Session = Depends(get_db),
    ):
        token = credentials.credentials
        payload = verify_access_token(token)
        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token payload"
        )

        credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
 
        )

        try:
              user_id = int(user_id)
        except(ValueError,TypeError):
              raise HTTPException(
                    status_code =  status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid user ID"
              )
        
        user = db.scalar(
              select(User).where(User.id == user_id)
              )
        
        if not user:
              raise HTTPException(
                    status_code=401,
                    detail="User not found"
              )
        
        return user


        
    

    