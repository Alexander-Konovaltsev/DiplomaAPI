from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    patronymic = Column(String(50), nullable=True)
    email = Column(String(50), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    workplace = Column(String(255), nullable=False)

    role = relationship("Role")
