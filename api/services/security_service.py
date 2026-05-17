import os
import bcrypt
from jose import jwt
from datetime import datetime, timedelta

class SecurityService:
    __ALGORITHM = "HS256"
    __SECRET_KEY = os.getenv("SECRET_KEY")
    __ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    @staticmethod
    def hash_password(password: str) -> str:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed_password.decode('utf-8')
    
    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    @classmethod
    def create_jwt_token(cls, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=cls.__ACCESS_TOKEN_EXPIRE_MINUTES)
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
