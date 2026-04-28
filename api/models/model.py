from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class Model(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    is_draggable = Column(Boolean, nullable=False, default=False)
    is_rotatable = Column(Boolean, nullable=False, default=False)
    is_assemblable = Column(Boolean, nullable=False, default=False)
    is_informational = Column(Boolean, nullable=False, default=False)
    
    parent_id = Column(Integer, ForeignKey("models.id"), nullable=True)

    parent = relationship("Model", remote_side=[id], backref="children")
