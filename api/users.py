import fastapi
from fastapi import Path
from pydantic import BaseModel
from typing import Optional, List

router = fastapi.APIRouter(

)

users = []

class User(BaseModel):
    email: str = "joshuaosoro@gmail.com"
    is_active: bool
    age: int = 18
    bio: Optional[str] = None


@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.get("/users{id}", response_model=User)
async def get_user(
    id: int = Path(..., description="ID of user to retrieve")
):
    return users[id]


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"

