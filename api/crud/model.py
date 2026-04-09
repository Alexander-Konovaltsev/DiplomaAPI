from sqlalchemy.orm import Session
from models.model import Model
from models.scene_model import SceneModel

def get_models_by_scene_id(db: Session, scene_id: int):
    return (
        db.query(Model)
        .join(SceneModel, SceneModel.model_id == Model.id)
        .filter(SceneModel.scene_id == scene_id)
        .all()
    )

def get_model_children_by_id(db: Session, model_id: int):
    return db.query(Model).filter(Model.parent_id == model_id).all()
