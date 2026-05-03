from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str = Field(exclude=True)

    class Config:
        from_attributes = True
