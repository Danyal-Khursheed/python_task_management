from pydantic import BaseModel, EmailStr, Field, SecretStr
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserCreate(BaseModel):
    userName: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone_number: PhoneNumber
    password: SecretStr = Field(min_length=8, max_length=128)


class Login(BaseModel):
    email:EmailStr
    password: SecretStr = Field(min_length=8, max_length=128)