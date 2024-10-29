from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="Fast API",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "joshua osoro",
        "email": "joshuaosoro@gmail.com"
    }
)

users = []

class User(BaseModel):
    email: str = "joshuaosoro@gmail.com"
    is_active: bool
    age: int = 18
    bio: Optional[str] = None

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.get("/users{id}")
async def get_user(
    id: int = Path(..., description="ID of user to retrieve"),
    q: str = Query(None, max_length=5)
):
    return {"user": users[id], "q": q}


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"

