from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.sql import func

from ..database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)

    createdAt = Column(DateTime(timezone=True),
                       server_default= func.now(),
                       nullable=False)
    
    updatedAt = Column(DateTime(timezone=True),
                       server_default=func.now(),
                       nullable=False,
                       onupdate=func.now())

