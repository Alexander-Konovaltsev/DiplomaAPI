from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from crud.scene import get_scenes
from crud.model import get_models_by_scene_id
from schemas.scene import SceneResponse
from schemas.model import ModelResponse
from dependencies.auth import get_current_user

router = APIRouter(prefix="/scenes", tags=["scenes"])

@router.get("", response_model=list[SceneResponse])
def read_scenes(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    scenes = get_scenes(db)
    return scenes

@router.get("/{scene_id}/models", response_model=list[ModelResponse])
def get_models_by_scene(scene_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    models = get_models_by_scene_id(db, scene_id)
    return models
