from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import UserCreate, UserOut
from app.db import get_db
from app.services.user_service import get_user, create_user
from app.auth.hashing import verify_password
from app.auth.jwt_handler import create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db())):
    if get_user(db, user.username):
        raise HTTPException(status_code=400, detail="Username already exists")
    return create_user(db, user.username, user.password)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db())):
    db_user = get_user(db, user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token(data={"sub": db_user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token": token, "token_type": "bearer"}
