import os
from dotenv import load_dotenv
load_dotenv()
from urllib.parse import quote_plus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_jwt_auth import AuthJWT

from app.schemas.user_schema import UserCreate, UserLogin, UserOut
from app.services.user_service import create_user, authenticate_user, get_user_by_email
from app.entity.user import Base

router = APIRouter()

# Config PostgreSQL
DB_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{quote_plus(os.getenv('POSTGRES_PASSWORD'))}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = create_user(db, user.username, user.email, user.password)
    return new_user

# LOGIN
@router.post("/login")
def login(user: UserLogin, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    access_token = Authorize.create_access_token(subject=db_user.email)
    refresh_token = Authorize.create_refresh_token(subject=db_user.email)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "username": db_user.username,
        "email": db_user.email
    }

# REFRESH
@router.post("/refresh")
def refresh(Authorize: AuthJWT = Depends()):
    Authorize.jwt_refresh_token_required()
    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}