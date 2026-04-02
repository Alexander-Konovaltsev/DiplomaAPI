from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from crud.role import get_roles
from schemas.role import RoleOut

router = APIRouter()

@router.get("", response_model=list[RoleOut])
def read_roles(db: Session = Depends(get_db)):
    return get_roles(db)
