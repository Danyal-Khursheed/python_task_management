from pydantic import BaseModel, Field, ConfigDict

class PostCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=1, max_length=5000)


class PostResponse(BaseModel):
    id: int
    title:str
    description:str

    model_config = ConfigDict(from_attributes=True)