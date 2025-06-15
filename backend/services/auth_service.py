# services/auth_service.py
from datetime import datetime, timedelta
from jose import jwt
from sqlalchemy.orm import Session
from models.user import User as UserModel
from models.user import User as UserSchema
from database import SessionLocal

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()

def authenticate_user(username: str, password: str) -> UserSchema | None:
    db = SessionLocal()
    user = get_user_by_username(db, username)
    if not user or user.hashed_password != password:
        return None
    return UserSchema(username=user.username, password=password, role=user.role)

def create_access_token(user: UserSchema) -> str:
    to_encode = {
        "sub": user.username,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
