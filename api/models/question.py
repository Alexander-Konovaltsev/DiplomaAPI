from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String(600), nullable=False)

    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=True)
    question_type_id = Column(Integer, ForeignKey("questions_types.id"), nullable=False)

    quiz = relationship("Quiz", backref="questions")
    model = relationship("Model", backref="questions")
    question_type = relationship("QuestionType", backref="questions")
    