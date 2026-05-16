from pydantic import BaseModel, EmailStr, field_validator, ValidationInfo
from typing import Optional
from datetime import datetime

class UserCreateRequest(BaseModel):
    last_name: str
    first_name: str
    patronymic: Optional[str] = None
    email: EmailStr
    password: str
    role_id: int
    workplace: str

    @field_validator("last_name", "first_name", "email", "workplace", mode="before")
    @classmethod
    def validate_required_strings(cls, v, info: ValidationInfo):
        if not v or not v.strip():
            raise ValueError(f"Поле {info.field_name} не может быть пустым")
        return v.strip()

    @field_validator("patronymic", mode="before")
    @classmethod
    def validate_optional(cls, v):
        if v is None:
            return v
        return v.strip() or None
    
class UserCreateResponse(BaseModel):
    id: int
    last_name: str
    first_name: str
    patronymic: str | None
    email: str
    role_id: int
    workplace: str
    created_at: datetime

    class Config:
        from_attributes = True

class UserLoginRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email", mode="before")
    @classmethod
    def validate_required_strings(cls, v, info: ValidationInfo):
        if not v or not v.strip():
            raise ValueError(f"Поле {info.field_name} не может быть пустым")
        return v.strip()

class UserLoginResponse(BaseModel):
    access_token: str

    class Config:
        from_attributes = True
