from pydantic import BaseModel
from datetime import datetime

class ResultDetailRequest(BaseModel):
    created_at: datetime
    result_id: int
    question_id: int
    answer_id: int

class ResultDetailResponse(BaseModel):
    id: int
    created_at: datetime
    user_id: int
    result_id: int
    question_id: int
    answer_id: int

    class Config:
        from_attributes = True
