from fastapi import APIRouter, HTTPException
from curd import get_user, create_user
from security import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(username: str, password: str, is_admin: bool = False):
    """
    Register a new user.
    Password can be any length (SHA256 → bcrypt handles it).
    """
    # Check if user exists
    if get_user(username):
        raise HTTPException(status_code=400, detail="User already exists")

    # Hash the password safely
    hashed = hash_password(password)  # SHA256 -> bcrypt inside security.py
    create_user(username, hashed, is_admin)

    return {"message": "User registered successfully"}

@router.post("/login")
def login(username: str, password: str):
    """
    Login user and return JWT token
    """
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Verify password (SHA256 -> bcrypt inside security.py)
    if not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create JWT token
    token = create_token({
        "sub": user["username"],
        "is_admin": user["is_admin"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }
