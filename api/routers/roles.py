from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from crud.role import get_roles
from schemas.role import GetRolesResponse

router = APIRouter(prefix="/roles", tags=["roles"])

@router.get("", response_model=list[GetRolesResponse])
def read_roles(db: Session = Depends(get_db)):
    return get_roles(db)
