from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from dependencies.auth import get_current_user
from schemas.quiz import QuizResponse
from crud.quiz import get_quizzes_by_scene_id

router = APIRouter(prefix="/quizzes", tags=["quizzes"])

@router.get("/{scene_id}", response_model=list[QuizResponse])
def read_quizzes(scene_id: int, db: Session = Depends(get_db), user: dict = Depends(get_current_user)):
    scenes = get_quizzes_by_scene_id(db, scene_id)
    return scenes
