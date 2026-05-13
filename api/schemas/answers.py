from pydantic import BaseModel
from typing import Optional

class AnswerResponse(BaseModel):
    id: int
    text: str
    is_correct: bool
    explanation: Optional[str]
    question_id: int

    class Config:
        from_attributes = True
        