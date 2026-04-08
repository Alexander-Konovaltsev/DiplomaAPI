from sqlalchemy.orm import Session
from models.scene import Scene

def get_scenes(db: Session):
    return db.query(Scene).all()
