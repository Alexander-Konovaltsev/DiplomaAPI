from sqlalchemy import Column, Integer, String
from db.session import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    def __str__(self):
        return self.name
