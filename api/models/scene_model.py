from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.session import Base

class SceneModel(Base):
    __tablename__ = "scenes_models"

    id = Column(Integer, primary_key=True, index=True)
    scene_id = Column(Integer, ForeignKey('scenes.id'), nullable=False)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    
    scene = relationship("Scene", backref="scene_models")
    model = relationship("Model", backref="scene_models")
    