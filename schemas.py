from pydantic import BaseModel
from typing import Literal


class UserRegister(BaseModel):
    username: str
    password: str
    role: Literal["admin", "worker", "client"]


class UserLogin(BaseModel):
    username: str
    password: str
