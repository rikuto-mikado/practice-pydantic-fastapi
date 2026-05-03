from fastapi import FastAPI, Depends
from schemas.request import UserCreate
from schemas.response import UserResponse
from schemas.params import FilterParams

app = FastAPI()

@app.post("/users", response_model=UserResponse)