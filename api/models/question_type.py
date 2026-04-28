from sqlalchemy import Column, Integer, String
from db.session import Base

class QuestionType(Base):
    __tablename__ = "questions_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    