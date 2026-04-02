from sqlalchemy.orm import Session
from models.role import Role

def get_roles(db: Session):
    return db.query(Role).all()
