from pydantic import BaseModel
from datetime import datetime

class ResultResponse(BaseModel):
    id: int
    percent: int
    total_answers: int
    correct_answers: int
    created_at: datetime
    user_id: int
    quiz_id: int
