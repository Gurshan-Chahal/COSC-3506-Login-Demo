from fastapi import APIRouter

from app.schemas import LoginRequest, LoginResponse

router = APIRouter()


@router.post("/api/login", response_model=LoginResponse)
def login(request: LoginRequest):

    # Email validation
    if request.email.strip() == "":
        return {
            "message": "Email cannot be empty"
        }

    # Password validation
    if request.password.strip() == "":
        return {
            "message": "Password cannot be empty"
        }

    # Password length validation
    if len(request.password) < 8:
        return {
            "message": "Password is too short"
        }

    # Email validation
    if request.email != "student@example.com":
        return {
            "message": "Invalid email"
        }

    # Password validation
    if request.password != "Password123":
        return {
            "message": "Invalid password"
        }

    return {
        "message": "Login successful"
    }