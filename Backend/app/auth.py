from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import LoginRequest, LoginResponse
from app.security import verify_password

router = APIRouter()


@router.post("/api/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == request.email).first()

    if user and verify_password(request.password, user.password_hash):
        return {
            "message": "Login successful"
        }

    return {
        "message": "Invalid email or password"
    }