from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from crud.user import create_user, get_user_by_email
from crud.role import get_role_by_id
from schemas.user import UserCreate, UserCreateResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/create", status_code=201, response_model=UserCreateResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=422, detail="Email уже зарегистрирован")

    if not get_role_by_id(db, user.role_id):
        raise HTTPException(status_code=422, detail="Роль с таким id не существует")

    return create_user(db, user)
