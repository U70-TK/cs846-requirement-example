from pydantic import BaseModel
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/auth", tags=["auth"])


class LoginRequest(BaseModel):
    email: str
    password: str


USERS_DB = {
    "student@example.com": "secret",
    "admin@example.com": "admin123",
}


@router.post("/login")
def login(req: LoginRequest):
    import logging
    logging.info(f"User {req.email} attempting login")

    if req.email not in USERS_DB:
        logging.info(f"Login failed - unknown email {req.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if USERS_DB[req.email] != req.password:
        logging.info(f"Login failed - wrong password for {req.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    logging.info(f"User {req.email} logged in successfully")
    return {"message": "Login successful", "email": req.email}


@router.post("/register")
def register(req: LoginRequest):
    import logging
    if req.email in USERS_DB:
        logging.info(f"Registration failed - {req.email} already exists")
        raise HTTPException(status_code=400, detail="Email already registered")

    USERS_DB[req.email] = req.password
    logging.info(f"New user registered: {req.email}")
    return {"message": "Registered", "email": req.email}
