from sqlalchemy.orm import Session
from models.result_detail import ResultDetail
from schemas.result_detail import ResultDetailRequest
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

def create_results_details(db: Session, data: list[ResultDetailRequest], user_id: int):
    try:
        results_details = []

        for item in data:
            result_detail = ResultDetail(
                created_at=item.created_at,
                user_id=user_id,
                result_id=item.result_id,
                question_id=item.question_id,
                answer_id=item.answer_id
            )

            db.add(result_detail)

            results_details.append(result_detail)

        db.commit()

        for item in results_details:
            db.refresh(item)

        return results_details
    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=422,
            detail="Некорректные внешние ключи или дублирующиеся данные"
        ) 
