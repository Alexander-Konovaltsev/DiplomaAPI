from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from dependencies.auth import get_current_user
from schemas.result_detail import ResultDetailRequest, ResultDetailResponse
from crud.result_detail import create_results_details

router = APIRouter(prefix="/results-details", tags=["results-details"])

@router.post("/create", response_model=list[ResultDetailResponse])
def create(results_details_request_data: list[ResultDetailRequest], 
           db: Session = Depends(get_db), 
           user: dict = Depends(get_current_user)):
    return create_results_details(db, results_details_request_data, user["user_id"])
