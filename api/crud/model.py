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

from sqlalchemy import select, union_all
from sqlalchemy.orm import aliased
from models.model import Model
from models.scene_model import SceneModel


def get_all_models_by_scene_id(db: Session, scene_id: int):
    base = (
        select(Model)
        .join(SceneModel, SceneModel.model_id == Model.id)
        .where(SceneModel.scene_id == scene_id)
    )

    cte = base.cte(name="model_tree", recursive=True)

    child = aliased(Model)

    recursive = (
        select(child)
        .join(cte, child.parent_id == cte.c.id)
    )

    cte = cte.union_all(recursive)

    stmt = select(Model).join(cte, Model.id == cte.c.id)

    return db.execute(stmt).scalars().all()
