from sqlalchemy.orm import Session
from models.quiz import Quiz

def get_quizzes_by_scene_id(db: Session, scene_id: int):
    return db.query(Quiz).filter_by(scene_id=scene_id).all()

def get_quiz_by_id(db: Session, quiz_id: int):
    return db.query(Quiz).filter_by(id=quiz_id).first()
