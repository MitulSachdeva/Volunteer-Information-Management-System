from fastapi import APIRouter
from ..auth import create_access_token

router = APIRouter()

@router.post("/login")
def login(data: dict):

    if (
        data["username"] == "admin"
        and data["password"] == "admin123"
    ):
        token = create_access_token(
            {"sub": "admin"}
        )

        return {
            "access_token": token
        }

    return {"error": "Invalid credentials"}