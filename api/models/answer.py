from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(600), nullable=False)
    is_correct = Column(Boolean, nullable=False, default=False)
    explanation = Column(Text, nullable=True)

    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)

    question = relationship("Question", backref="answers")
