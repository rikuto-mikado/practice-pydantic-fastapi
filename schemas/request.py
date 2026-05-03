from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    age: int = Field(None, ge=0, le=120)
