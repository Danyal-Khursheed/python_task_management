from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class PostCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=1, max_length=5000)


class PostResponse(BaseModel):
    id: int
    title: str
    description: str
    createdAt: datetime
    updatedAt: datetime

    model_config = ConfigDict(from_attributes=True)


class PaginationMeta(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int


class PostListResponse(BaseModel):
    data: list[PostResponse]
    metadata: PaginationMeta
