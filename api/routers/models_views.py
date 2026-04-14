from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from dependencies.auth import get_current_user
from schemas.user_model_view import UserModelViewCreateRequest, UserModelViewResponse
from crud.user_model_view import create_user_model_view
from crud.scene import get_scene_by_id
from crud.model import get_model_by_id

router = APIRouter(prefix="/models-views", tags=["models-views"])

@router.post("/create", response_model=UserModelViewResponse)
def create_models_views(models_views_data: UserModelViewCreateRequest, 
                        db: Session = Depends(get_db), 
                        user: dict = Depends(get_current_user)):
    if not get_scene_by_id(db, models_views_data.scene_id):
        raise HTTPException(status_code=422, detail="Сцена с таким id не существует")
    
    if not get_model_by_id(db, models_views_data.model_id):
        raise HTTPException(status_code=422, detail="Модель с таким id не существует")

    return create_user_model_view(db, models_views_data, user["user_id"])
