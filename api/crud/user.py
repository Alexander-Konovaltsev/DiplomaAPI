from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreateRequest
from services.security_service import SecurityService

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: UserCreateRequest):
    hashed_password = SecurityService.hash_password(user_data.password)

    db_user = User(
        last_name=user_data.last_name,
        first_name=user_data.first_name,
        patronymic=user_data.patronymic,
        email=user_data.email,
        password=hashed_password,
        role_id=user_data.role_id,
        workplace=user_data.workplace
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
