import os
import bcrypt
from jose import jwt
from datetime import datetime, timedelta

class SecurityService:
    __ALGORITHM = "HS256"
    __SECRET_KEY = os.getenv("SECRET_KEY")

    @staticmethod
    def hash_password(password: str) -> str:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')
    
    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @classmethod
    def create_jwt_token(cls, data: dict, expires_minutes: int = 120) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
        to_encode.update({"exp": expire})
        token = jwt.encode(to_encode, cls.__SECRET_KEY, algorithm=cls.__ALGORITHM)
        return token
    
    @classmethod
    def decode_jwt_token(cls, token: str) -> dict:
        try:
            payload = jwt.decode(token, cls.__SECRET_KEY, algorithms=[cls.__ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expired")
        except jwt.JWTError:
            raise ValueError("Invalid token")
