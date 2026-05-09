from sqlalchemy.orm import Session
from models.result import Result

def get_results_by_user_id(db: Session, user_id: int):
    return db.query(Result).filter_by(user_id=user_id).all()
