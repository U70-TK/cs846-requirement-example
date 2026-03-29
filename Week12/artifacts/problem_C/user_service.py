from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/users", tags=["users"])


class CreateUserRequest(BaseModel):
    email: str
    password: str
    name: str


USERS: list[dict] = []


@router.post("/")
def create_user(req: CreateUserRequest):
    print("Creating user:", req.email)
    print("Password:", req.password)

    for u in USERS:
        if u["email"] == req.email:
            print("Duplicate email found:", req.email)
            raise HTTPException(status_code=400, detail="Email already exists")

    user = {"email": req.email, "name": req.name, "password": req.password}
    USERS.append(user)
    print("User created successfully:", req.email)
    return {"email": req.email, "name": req.name}


@router.get("/")
def list_users():
    print("Fetching all users, count:", len(USERS))
    return [{"email": u["email"], "name": u["name"]} for u in USERS]


@router.get("/{email}")
def get_user(email: str):
    print("Looking up user:", email)
    for u in USERS:
        if u["email"] == email:
            return {"email": u["email"], "name": u["name"]}
    print("User not found:", email)
    raise HTTPException(status_code=404, detail="User not found")
