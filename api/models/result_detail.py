from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from db.session import Base

class ResultDetail(Base):
    __tablename__ = "results_details"
    
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    result_id = Column(Integer, ForeignKey("results.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    answer_id = Column(Integer, ForeignKey("answers.id"), nullable=False)

    user = relationship("User", backref="results_details")
    result = relationship("Result", backref="results_details")
    question = relationship("Question", backref="results_details")
    answer = relationship("Answer", backref="results_details")
    