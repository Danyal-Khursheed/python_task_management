
from fastapi import HTTPException
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
import os
import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
TOKEN_EXPIRE_TIME = os.getenv("TOKEN_EXPIRE_TIME", "60")

if not SECRET_KEY:
    raise RuntimeError("Missing SECRET_KEY in .env")


def create_access_token(user_id: int):
    expires = datetime.now(timezone.utc) + timedelta(
        minutes=int(TOKEN_EXPIRE_TIME)
    )

    payload = {
        "sub": str(user_id),
        "exp": expires,
        "iat": datetime.now(timezone.utc)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token



def verify_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )

    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

