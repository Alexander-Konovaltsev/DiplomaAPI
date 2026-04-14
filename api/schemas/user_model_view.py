from pydantic import BaseModel
from datetime import datetime

class UserModelViewCreateRequest(BaseModel):
    scene_id: int
    model_id: int

class UserModelViewResponse(BaseModel):
    id: int
    user_id: int
    scene_id: int
    model_id: int
    viewed_at: datetime

    class Config:
        from_attributes = True
        