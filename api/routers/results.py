from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from dependencies.auth import get_current_user
from schemas.result import ResultResponse, ResultRequest
from crud.result import get_results_by_user_id, create_result
from crud.quiz import get_quiz_by_id

router = APIRouter(prefix="/results", tags=["results"])

@router.get("", response_model=list[ResultResponse])
def read_results(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    results = get_results_by_user_id(db, user["user_id"])
    return results

@router.post("/create", response_model=ResultResponse)
def create(result_request_data: ResultRequest, 
           db: Session = Depends(get_db), 
           user: dict = Depends(get_current_user)):
    quiz = get_quiz_by_id(db, result_request_data.quiz_id)

    if not quiz:
        raise HTTPException(status_code=422, detail="Теста с таким id не существует")
    
    return create_result(db, result_request_data, user["user_id"])
