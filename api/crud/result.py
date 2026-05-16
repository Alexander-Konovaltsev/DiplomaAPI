from sqlalchemy.orm import Session
from models.result import Result
from schemas.result import ResultRequest
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def get_results_by_user_id(db: Session, user_id: int):
    return db.query(Result).filter_by(user_id=user_id).all()

def create_result(db: Session, data: ResultRequest, user_id: int):
    try:
        result = Result(
            percent=data.percent,
            total_answers=data.total_answers,
            correct_answers=data.correct_answers,
            user_id=user_id,
            quiz_id=data.quiz_id
        )

        db.add(result)
        db.commit()
        db.refresh(result)

        return result
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=422,
            detail="Некорректные внешние ключи или дублирующиеся данные"
        )   
