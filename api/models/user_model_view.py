from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from db.session import Base

class UserModelView(Base):
    __tablename__ = "users_models_views"

    id = Column(Integer, primary_key=True, index=True)
    viewed_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    scene_id = Column(Integer, ForeignKey("scenes.id"), nullable=False)
    model_id = Column(Integer, ForeignKey("models.id"), nullable=False)

    user = relationship("User", backref="models_views")
    scene = relationship("Scene", backref="models_views")
    model = relationship("Model", backref="models_views")

    __table_args__ = (
        UniqueConstraint("user_id", "scene_id", "model_id", name="uq_user_scene_models"),
    )
