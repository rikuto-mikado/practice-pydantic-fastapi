from fastapi import FastAPI, Depends
from schemas.request import UserCreate
from schemas.response import UserResponse
from schemas.params import FilterParams

app = FastAPI()


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    return {
        "id": 1,
        "username": user.username,
        "email": user.email,
        "hashed_password": "secret_hash_value",
    }


@app.get("/items")
def list_items(filters: FilterParams = Depends()):
    return {"filters": filters.model_dump()}
