from sqlalchemy import Column, Integer, String, Text
from db.session import Base

class Scene(Base):
    __tablename__ = "scenes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
