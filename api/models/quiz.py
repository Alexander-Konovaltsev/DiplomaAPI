from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    attempts_count = Column(Integer, nullable=False)
    questions_count = Column(Integer, nullable=False)

    scene_id = Column(Integer, ForeignKey("scenes.id"), nullable=False)

    scene = relationship("Scene", backref="quizzes")
