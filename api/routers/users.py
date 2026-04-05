from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud.user import create_user, get_user_by_email
from crud.role import get_role_by_id
from schemas.user import UserCreateRequest, UserCreateResponse, UserLoginRequest, UserLoginResponse
from services.security_service import SecurityService

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create", status_code=201, response_model=UserCreateResponse)
def register_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=422, detail="Email уже зарегистрирован")

    if not get_role_by_id(db, user.role_id):
        raise HTTPException(status_code=422, detail="Роль с таким id не существует")

    return create_user(db, user)

@router.post("/login", response_model=UserLoginResponse)
def login_user(login_data: UserLoginRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, login_data.email)
    if not user:
        raise HTTPException(status_code=401, detail="Неверные учетные данные")

    if not SecurityService.check_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Неверные учетные данные")
    
    token_data = {"user_id": user.id, "email": user.email}
    token = SecurityService.create_jwt_token(token_data)
    return UserLoginResponse(access_token=token)
