from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from crud.scene import get_scenes
from schemas.scene import SceneResponse
from dependencies.auth import get_current_user

router = APIRouter(prefix="/scenes", tags=["scenes"])

@router.get("", response_model=list[SceneResponse])
def read_scenes(db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    scenes = get_scenes(db)
    return scenes
