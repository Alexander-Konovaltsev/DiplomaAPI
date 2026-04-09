from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from crud.model import get_model_children_by_id
from schemas.model import ModelResponse
from dependencies.auth import get_current_user

router = APIRouter(prefix="/models", tags=["models"])

@router.get("/{model_id}/children", response_model=list[ModelResponse])
def read_model_children(model_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    model_children = get_model_children_by_id(db, model_id)
    return model_children
