from sqlalchemy.orm import Session
from models.question import Question
from sqlalchemy.orm import joinedload

def get_questions_by_quiz_id(db: Session, quiz_id: int):
    questions = (
        db.query(Question)
        .options(
            joinedload(Question.question_type),
            joinedload(Question.answers)
        )
        .filter(Question.quiz_id == quiz_id)
        .all()
    )

    return questions
