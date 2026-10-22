from sqlalchemy import text
from src.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text('SELECT version()'))
        print("Database connected successfully")
        print(result.scalar())
except Exception as error:
    print("Error occuried while conencting to db")
    print(error)