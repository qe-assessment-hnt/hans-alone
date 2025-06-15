# services/auth_service.py
from datetime import datetime, timedelta
from jose import jwt
from models.user import User

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "alice": {"username": "alice", "password": "secret", "role": "admin"},
    "bob": {"username": "bob", "password": "secret", "role": "client"},
}

def authenticate_user(username: str, password: str) -> User | None:
    user_dict = fake_users_db.get(username)
    if not user_dict or user_dict["password"] != password:
        return None
    return User(**user_dict)

def create_access_token(user: User) -> str:
    to_encode = {
        "sub": user.username,
        "role": user.role,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
