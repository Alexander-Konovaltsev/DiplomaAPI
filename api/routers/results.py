from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from dependencies.auth import get_current_user
from schemas.result import ResultResponse
from crud.result import get_results_by_user_id

router = APIRouter(prefix="/results", tags=["results"])

@router.get("", response_model=list[ResultResponse])
def read_results(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    results = get_results_by_user_id(db, user["user_id"])
    return results
