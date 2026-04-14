from sqlalchemy.orm import Session
from models.scene import Scene

def get_scenes(db: Session):
    return db.query(Scene).all()

def get_scene_by_id(db: Session, scene_id: int):
    return db.query(Scene).filter(Scene.id == scene_id).first()
