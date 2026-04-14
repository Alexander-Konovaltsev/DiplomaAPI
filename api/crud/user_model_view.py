from sqlalchemy.orm import Session
from models.user_model_view import UserModelView
from schemas.user_model_view import UserModelViewCreateRequest
from sqlalchemy.exc import IntegrityError

def create_user_model_view(db: Session, data: UserModelViewCreateRequest, user_id: int):
    user_model_view = UserModelView(
        user_id=user_id,
        scene_id=data.scene_id,
        model_id=data.model_id
    )

    try:
        db.add(user_model_view)
        db.commit()
        db.refresh(user_model_view)
        return user_model_view

    except IntegrityError:
        db.rollback()

        return db.query(UserModelView).filter_by(
            user_id=user_id,
            scene_id=data.scene_id,
            model_id=data.model_id
        ).first()
    
def get_user_models_views_by_scene_id(db: Session, user_id: int, scene_id: int):
    return db.query(UserModelView).filter_by(
        user_id=user_id,
        scene_id=scene_id
    ).all();
