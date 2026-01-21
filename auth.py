from fastapi import APIRouter, HTTPException
from curd import get_user, create_user
from security import hash_password, verify_password, create_token
from schemas import UserRegister, UserLogin

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(data: UserRegister):
    """
    Register user with role: admin / worker / client
    """

    if get_user(data.username):
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    hashed_password = hash_password(data.password)

    create_user(
        username=data.username,
        password=hashed_password,
        role=data.role
    )

    return {
        "message": "User registered successfully",
        "role": data.role
    }


@router.post("/login")
def login(data: UserLogin):
    """
    Login and return JWT token with role
    """

    user = get_user(data.username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({
        "sub": user["username"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": user["role"]
    }


print("Auth router loaded")
