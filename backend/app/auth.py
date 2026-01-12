from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import UserBase
from database_model import User
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError


# seperate from main.py file
router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

# add secret key
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

# use to hash password
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    # open database
    db = SessionLocal()
    try:
    # use database
        yield db
    # close database
    finally:
        db.close()



# create user router
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: UserBase, db: Session = Depends(get_db)):
    
    create_user_model = User(
        email=create_user_request.email, 
        password=bcrypt_context.hash(create_user_request.password)
        )

    db.add(create_user_model)
    db.commit()